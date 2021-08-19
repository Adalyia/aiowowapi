from datetime import datetime, timedelta
import aiohttp
import asyncio
from typing import Union

class API():
    """This is our core API class with methods for interacting with Battle.net's various APIs

    :param client_id: A Battle.net Project Client ID - Generated at https://develop.battle.net/access/clients
    :type client_id: str
    :param client_secret: A Battle.net Project Client Secret - Generated at https://develop.battle.net/access/clients
    :type client_secret: str
    :param client_region: The Battle.net/WoW API region which we submit requests to, defaults to 'us'
    :type client_region: str, optional
    :param client_locale: The locale used for API requests. Compatbility varies by region, see https://develop.battle.net/documentation/guides/regionality-and-apis, defaults to 'en_US'
    :type client_locale: str, optional
    :param max_parallel_requests: The maximum number of parallel aiohttp requests
    :type max_parallel_requests: int, optional
    :param max_request_retries: The maximum number of aiohttp request retries (min 1)
    :type max_request_retries: int, optional
    :param request_retry_delay: The delay between aiohttp request retries (min 0) (This value is in seconds)
    :type request_retry_delay: int, optional
    """

    def __init__(self, client_id:str, client_secret:str, client_region:str='us', client_locale:str='en_US', max_parallel_requests:int=50, max_request_retries:int=3, request_retry_delay:int=1):
        """Constructor method
        """
        self.api_regions = {
            'us': {
                'oauth_api_hostname': 'https://us.battle.net{api_endpoint}',
                'game_api_hostname': 'https://us.api.blizzard.com{api_endpoint}',
                'supported_locales': ['en_US', 'es_MX', 'pt_BR']
            },
            'eu': {
                'oauth_api_hostname': 'https://eu.battle.net{api_endpoint}',
                'game_api_hostname': 'https://eu.api.blizzard.com{api_endpoint}',
                'supported_locales': ['en_GB', 'es_ES', 'fr_FR', 'ru_RU', 'de_DE', 'pt_PT', 'it_IT']
            },
            'kr': {
                'oauth_api_hostname': 'https://kr.battle.net{api_endpoint}',
                'game_api_hostname': 'https://kr.api.blizzard.com{api_endpoint}',
                'supported_locales': ['ko_KR']
            },
            'tw': {
                'oauth_api_hostname': 'https://tw.battle.net{api_endpoint}',
                'game_api_hostname': 'https://tw.api.blizzard.com{api_endpoint}',
                'supported_locales': ['zh_TW']
            },
            'cn': {
                'oauth_api_hostname': 'https://www.battlenet.com.cn{api_endpoint}',
                'game_api_hostname': 'https://gateway.battlenet.com.cn{api_endpoint}',
                'supported_locales': ['zh_CN']
            }
        }

        self.client_id = client_id
        self.client_secret = client_secret
        self.client_region = None
        self.client_locale = None

        self.setRegion(client_region)
        self.setLocale(client_locale)

        self.access_tokens = {}
        
        self.semaphore = asyncio.Semaphore(max_parallel_requests)
        
        self.max_request_retries = max_request_retries if max_request_retries > 1 else 1
        
        self.request_retry_delay = request_retry_delay if request_retry_delay > 0 else 1
        

    async def getRegion(self) -> str:
        """Returns the current region being used for API requests

        :return: The current region being used for API requests
        :rtype: str
        """
        return self.client_region

    async def getLocale(self) -> str:
        """Returns the current locale being used for API requests

        :return: The current locale being used for API requests
        :rtype: str
        """
        return self.client_locale

    def setRegion(self, region:str) -> None:
        """Sets the region we'll use for API requests

        :param region: The desired region to be used for API requests
        :type region: str
        :raises InvalidRegionException: Raised when the provided region isn't in our supported regions dictionary
        """
        if region in self.api_regions:
            self.client_region = region
            self.client_locale = self.api_regions[region]['supported_locales'][0]
        else:
            raise InvalidRegionException('Invalid API Region {}, supported regions are {}'.format(
                region, list(self.api_regions.keys())))

    def setLocale(self, locale:str) -> None:
        """Sets the locale we'll use for API requests

        :param locale: The desired locale to be used for API requests.
        :type locale: str
        :raises InvalidLocaleException: Raised when the string given doesn't match any of the current region's supported locales
        """
        if locale and locale in self.api_regions[self.client_region]['supported_locales']:
            self.client_locale = locale
        else:
            raise InvalidLocaleException('Invalid Regional Locale {}, supported locales for {} are {}'.format(
                locale, self.client_region, self.api_regions[self.client_region]['supported_locales']))

    async def getHostname(self) -> str:
        """Returns the current region's hostname for Game API requests

        :return: The current region's hostname for Game API requests
        :rtype: str
        """
        return self.api_regions[self.client_region]['game_api_hostname']
    
    async def getOAuthHostname(self) -> str:
        """Returns the current region's hostname for OAuth API requests

        :return: The current region's hostname for OAuth API requests
        :rtype: str
        """
        return self.api_regions[self.client_region]['oauth_api_hostname']
    
    async def getAccessToken(self) -> str:
        """Returns and / or generates an API access token using the provided credentials in the class constructor

        :raises RequestException: Raised when we encounter an issue when making an aiohttp request.
        :return: A Battle.net OAuth Access Token
        :rtype: str
        """

        if self.access_tokens and self.access_tokens[self.client_region] and self.access_tokens[self.client_region]['Expires'] > datetime.now():
            return self.access_tokens[self.client_region]['Token']        
        else:
            endpoint = f"/oauth/token"

            hostname = await self.getOAuthHostname()
            
            params = {'grant_type': 'client_credentials'}
            
            data = await self.getResource(hostname, endpoint, params, auth=aiohttp.BasicAuth(self.client_id, self.client_secret), method="POST")
            
            if data is not None:
                expires = datetime.now() + timedelta(seconds=data['expires_in']-60)
                
                self.access_tokens[self.client_region] = {'Token': data['access_token'], 'Expires': expires}
                    
                return self.access_tokens[self.client_region]['Token']
            else:
                raise AccessTokenException('Failed to retrieve an access token, verify your credentials & internet connectivity.')

    async def multiRequest(self, requests:list) -> list:
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

        
    
    async def getResource(self, hostname:str, api_endpoint:str, params:dict=None, auth:aiohttp.BasicAuth=None, method:str='GET') -> Union[dict, None]:
        """Make an API request and return the response as a JSON dictionary

        :param api_endpoint: The API endpoint following the regional hostname we wish to send a request to.
        :type api_endpoint: str
        :param params: The additional arguments/parameters we need to send with the request, defaults to None
        :type params: dict, optional
        :param method: The HTTP request method to be used, defaults to 'GET'
        :type method: str, optional
        :raises RequestMethodException: Raised when an invalid HTTP request method is selected.
        :raises RequestException: Raised when we encounter an issue when making an aiohttp request.
        :return: The response from the API as a JSON dictionary
        :rtype: dict
        """
        
        
        result = None

        method = str(method).upper()

        api_request = hostname.format(
            api_endpoint=api_endpoint
        )
        
        async with self.semaphore:
            current_attempt = 1
            while current_attempt <= self.max_request_retries and not result:
                try:
                    print('Test')
                    async with aiohttp.ClientSession() as http_session:

                        supported_request_types = {
                            'GET': http_session.get,
                            'POST': http_session.post
                        }

                        if method in supported_request_types:
                            async with supported_request_types[method](api_request, params=params, auth=auth) as response:
                                
                                if response.status >= 200 and response.status < 300:
                                    result = await response.json()
                                response.raise_for_status()
                                
                                    
                        else:
                            raise RequestMethodException('Invalid request method {}, supported methods are {}'.format(
                                method, list(supported_request_types.keys())))
                except aiohttp.ClientError as e:
                    if current_attempt == self.max_request_retries:
                        raise
                    current_attempt += 1
                    await asyncio.sleep(self.request_retry_delay)
                # finally:
                #     if result is None:
                #         current_attempt += 1
                #         await asyncio.sleep(self.request_retry_delay)

        return result


class WoWApiException(Exception):
    """Generic exception type for our API

    :param message: Description of the occurring error
    :type message: str, optional
    """

    def __init__(self, message:str="An error was encountered with wowapi"):
        super().__init__(message)


class AccessTokenException(WoWApiException):
    """Exception thrown when a null access token is provided

    :param message: Description of the occurring error
    :type message: str, optional
    """

    def __init__(self, message:str="An error was encountered retrieving an API access token"):
        super().__init__(message)
        
class RequestException(WoWApiException):
    """Exception thrown when something goes wrong with an HTTP API request

    :param message: Description of the occurring error
    :type message: str, optional
    """

    def __init__(self, message:str="Error making API request"):
        super().__init__(message)
    
class RequestMethodException(RequestException):
    """Exception thrown when an invalid HTTP request method is provided

    :param message: Description of the occurring error
    :type message: str, optional
    """

    def __init__(self, message:str="Invalid Request Method Provided"):
        super().__init__(message)


class InvalidRegionException(WoWApiException):
    """Exception thrown when an invalid/unsupported API Region is provided

    :param message: Description of the occurring error
    :type message: str, optional
    """

    def __init__(self, message:str="Invalid API Region"):
        super().__init__(message)


class InvalidLocaleException(WoWApiException):
    """Exception thrown when an invalid/unsupported API Locale is provided

    :param message: Description of the occurring error
    :type message: str, optional
    """

    def __init__(self, message:str="Invalid API Locale"):
        super().__init__(message)
