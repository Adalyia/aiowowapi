import asyncio
from datetime import datetime, timedelta
from types import TracebackType
from typing import Union, Optional, Type, Dict, Any

import aiohttp

from .regions import APIRegion


class API:
    def __init__(self, client_id: str, client_secret: str,
                 client_region: Union[APIRegion, str], *,
                 max_parallel_requests: Optional[int] = None,
                 max_request_retries: Optional[int] = None,
                 request_retry_delay: Optional[int] = None,
                 request_debugging: Optional[bool] = None):
        """A class with methods for interacting with Battle.net's various APIs

        :param client_id: Battle.net Project Client ID -
            Generated at https://develop.battle.net/access/clients
        :type client_id: str
        :param client_secret: Battle.net Project Client Secret -
            Generated at https://develop.battle.net/access/clients
        :type client_secret: str
        :param client_region: The Battle.net/WoW API region which we submit
            requests to, defaults to APIRegion.US
        :type client_region: str, APIRegion, optional
        :param max_parallel_requests: The maximum number of parallel aiohttp
            requests (Default: 50)
        :type max_parallel_requests: int, optional
        :param max_request_retries: The maximum number of aiohttp request
            retries (min 1) (Default: 3)
        :type max_request_retries: int, optional
        :param request_retry_delay: The delay between aiohttp request retries
            (Seconds - min 0)(Default: 1)
        :type request_retry_delay: int, optional
        :param request_debugging: Whether aiohttp request exceptions are
            or return None (Default: False)
        :type request_debugging: bool, optional
        """

        self.__client_id: str = client_id
        self.__client_secret: str = client_secret
        self.__client_region: APIRegion = self.set_region(client_region)
        self.__client_locale: str = \
            self.__client_region.value['supported_locales'][0]

        self.__access_tokens: Dict[str, Dict[str, Any]] = {}

        self.__semaphore: asyncio.Semaphore = asyncio.Semaphore(
            max_parallel_requests if max_parallel_requests is not None else 50
        )

        self.__max_request_retries: int = max_request_retries if \
            (max_request_retries is not None) and (max_request_retries > 1) \
            else 3

        self.__request_retry_delay: int = request_retry_delay if \
            (request_retry_delay is not None) and (request_retry_delay > 0) \
            else 1

        self.__request_debugging: bool = request_debugging if \
            (request_debugging is not None) else True

        self.__session: Optional[aiohttp.ClientSession] = None

        self.__is_context_manager: bool = False

    def __enter__(self) -> None:
        raise TypeError("Use 'async with' instead")

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> None:
        pass

    async def __aenter__(self) -> 'API':
        self.__session = aiohttp.ClientSession()
        self.__is_context_manager = True
        return self

    async def __aexit__(self, exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType]) -> None:
        if self.__session is not None and self.__session.closed is False:
            await self.__session.close()

    def get_region(self) -> str:
        """Returns the current region being used for API requests

        :return: The current region being used for API requests
        :rtype: str
        """
        return self.__client_region.name

    def get_locale(self) -> str:
        """Returns the current locale being used for API requests

        :return: The current locale being used for API requests
        :rtype: str
        """
        return self.__client_locale

    def set_region(self, region: Union[APIRegion, str]) -> APIRegion:
        """Sets the region to be used for API requests

        :param region: The desired region to be used for API requests
        :type region: str, APIRegion
        :raises InvalidRegionException: Raised when the provided region isn't
            supported/found
        :return: The API object
        :rtype: API
        """
        if region in list(APIRegion) and isinstance(region, APIRegion):
            self.__client_region = region
            self.__client_locale = region.value['supported_locales'][0]
            return region
        elif isinstance(region, str):
            for i in list(APIRegion):
                if i.name.lower() == region.lower():
                    self.__client_region = i
                    self.__client_locale = i.value['supported_locales'][0]
                    return i
            raise InvalidRegionException(
                'Invalid API Region {}, supported regions are {}'.format(
                    region, list(APIRegion.__members__.keys())))
        else:
            raise InvalidRegionException(
                'Invalid API Region {}, supported regions are {}'.format(
                    region, list(APIRegion.__members__.keys())))

    def set_locale(self, locale: str) -> str:
        """Sets the locale we'll use for API requests

        :param locale: The desired locale to be used for API requests.
        :type locale: str
        :raises InvalidLocaleException: Raised the input doesn't match any of
            the current region's supported locales
        :return: The current locale being used for API requests
        :rtype: str
        """
        if locale and \
                (locale in self.__client_region.value['supported_locales']):
            self.__client_locale = locale
        else:
            raise InvalidLocaleException(
                'Invalid Regional Locale {}, supported locales for {} are {}'
                .format(
                    locale, self.__client_region.name,
                    self.__client_region.value['supported_locales']))

        return self.__client_locale

    def get_hostname(self) -> str:
        """Returns the current region's hostname for Game API requests

        :return: The current region's hostname for Game API requests
        :rtype: str
        """
        return self.__client_region.value['game_api_hostname']

    def get_oauth_hostname(self) -> str:
        """Returns the current region's hostname for OAuth API requests

        :return: The current region's hostname for OAuth API requests
        :rtype: str
        """
        return self.__client_region.value['oauth_api_hostname']

    async def get_access_token(self) -> str:
        """Returns and / or generates an API access token using the provided
        credentials in the class constructor

        :raises RequestException: Raised when we encounter an issue when making
            an aiohttp request.
        :return: A Battle.net OAuth Access Token
        :rtype: str
        """

        if self.__client_region.name in self.__access_tokens and \
                self.__access_tokens[self.__client_region.name][
                    'Expires'] > datetime.now():
            return self.__access_tokens[self.__client_region.name]['Token']
        else:
            endpoint = f"/oauth/token"

            hostname = self.get_oauth_hostname()

            params = {'grant_type': 'client_credentials'}

            data = await self.get_resource(hostname, endpoint, params,
                                           auth=aiohttp.BasicAuth(
                                               self.__client_id,
                                               self.__client_secret),
                                           method="POST")

            if data is None:
                raise AccessTokenException(
                    'Failed to retrieve an access token, verify your '
                    'credentials & internet connectivity.')

            expires = datetime.now() + timedelta(
                seconds=data['expires_in'] - 60)

            self.__access_tokens[self.__client_region.name] = {
                'Token': data['access_token'], 'Expires': expires}

            return self.__access_tokens[self.__client_region.name]['Token']

    @staticmethod
    async def multi_request(requests: list) -> Optional[Union[tuple, list]]:
        """Make several API requests in parallel

        :param requests: A list of API request coroutines
        :type requests: list
        :return: The API responses as a list of dicts
        :rtype: list
        """
        data = await asyncio.gather(*requests)
        if data:
            return data
        else:
            return None

    async def get_resource(self,
                           hostname: str, api_endpoint: str,
                           params: Optional[dict] = None,
                           auth: Optional[aiohttp.BasicAuth] = None,
                           method: Optional[str] = None,
                           ) -> Optional[dict]:
        """Make an API request and return the response as a JSON dictionary

        :param hostname: The hostname to make the request to
        :type hostname: str
        :param api_endpoint: The API endpoint following the regional hostname
            we wish to send a request to.
        :type api_endpoint: str
        :param params: The additional arguments/parameters we need to send with
            the request, defaults to None
        :type params: dict, optional
        :param auth: The aiohttp BasicAuth object to use for authentication,
            defaults to None
        :type auth: aiohttp.BasicAuth, optional
        :param method: The HTTP method to use for the request,
            defaults to "GET"
        :type method: str, optional
        :raises RequestMethodException: Raised when an invalid HTTP request
            method is selected.
        :raises RequestException: Raised when we encounter an issue when making
            an aiohttp request.
        :return: The response from the API as a JSON dictionary
        :rtype: dict, none
        """

        if method is None:
            method = "GET"

        async with self.__semaphore:
            current_attempt: int = 1
            local_session: Optional[
                aiohttp.ClientSession] = aiohttp.ClientSession() if \
                self.__is_context_manager is False else None

            if self.__is_context_manager is True and (
                    self.__session is None or self.__session.closed):
                self.__session = aiohttp.ClientSession()
            result: Optional[Dict] = None
            while (current_attempt <= self.__max_request_retries) and \
                    (result is None):
                try:

                    supported_methods = {
                        "GET": local_session.get if
                        (self.__is_context_manager is False and
                         local_session is not None)
                        else self.__session.get,
                        "POST": local_session.post if
                        (self.__is_context_manager is False and
                         local_session is not None)
                        else self.__session.post,
                    }

                    if method.upper() not in supported_methods:
                        raise RequestMethodException(
                            'Invalid HTTP request method {}, supported '
                            'methods are {}'.format(
                                method, list(supported_methods.keys())))

                    async with supported_methods[method](
                            hostname.format(api_endpoint=api_endpoint),
                            params=params,
                            auth=auth
                    ) as response:

                        if response.status == 200:
                            result = await response.json()

                        response.raise_for_status()

                    if (local_session is not None) and \
                            (local_session.closed is False):
                        await local_session.close()

                except aiohttp.ClientError:
                    if current_attempt == self.__max_request_retries:
                        if self.__request_debugging:
                            raise
                        return result
                    current_attempt += 1
                    await asyncio.sleep(self.__request_retry_delay)
            return result


class ApiException(Exception):
    """Generic exception type for our API

    :param message: Description of the occurring error
    :type message: str, optional
    """

    def __init__(self,
                 message: str = "An error was encountered in the API class."):
        super().__init__(message)


class AccessTokenException(ApiException):
    """Exception thrown when a null access token is provided

    :param message: Description of the occurring error
    :type message: str, optional
    """

    def __init__(self,
                 message: str = "An error was encountered retrieving an API "
                                "access token"):
        super().__init__(message)


class RequestException(ApiException):
    """Exception thrown when something goes wrong with an HTTP API request

    :param message: Description of the occurring error
    :type message: str, optional
    """

    def __init__(self, message: str = "Error making API request"):
        super().__init__(message)


class RequestMethodException(ApiException):
    """Exception thrown when an invalid request method is given

    :param message: Description of the occurring error
    :type message: str, optional
    """

    def __init__(self, message: str = "Invalid request method"):
        super().__init__(message)


class InvalidRegionException(ApiException):
    """Exception thrown when an invalid/unsupported API Region is provided

    :param message: Description of the occurring error
    :type message: str, optional
    """

    def __init__(self, message: str = "Invalid API Region"):
        super().__init__(message)


class InvalidLocaleException(ApiException):
    """Exception thrown when an invalid/unsupported API Locale is provided

    :param message: Description of the occurring error
    :type message: str, optional
    """

    def __init__(self, message: str = "Invalid API Locale"):
        super().__init__(message)
