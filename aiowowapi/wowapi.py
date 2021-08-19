import re
from typing import Union
from urllib.parse import *
from aiowowapi.api import API
from .retail.retail import RetailApi


class WowApi(API):
    """This class contains some useful functions/QoL features for working with the World of Warcraft API

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
    :param request_retry_delay: The delay between aiohttp request retries (min 1) (This value is in seconds)
    :type request_retry_delay: int, optional
    """

    def __init__(self, client_id:str, client_secret:str, client_region:str='us', client_locale:str='en_US', max_parallel_requests:int=50, max_request_retries:int=3, request_retry_delay:int=1):
        """Constructor method
        """
        super().__init__(client_id, client_secret, client_region, client_locale, max_parallel_requests, max_request_retries, request_retry_delay)

        self.Retail = RetailApi(super())
        
        self.realms = None
        

    async def parseArmoryLink(self, url:str) -> Union[str, None]:
        """Parses a World of Warcraft Armoury link and returns the character's name, realm, and region

        :param url: A World of Warcraft Armoury link such as https://worldofwarcraft.com/en-us/character/us/{slug}/{character}
        :type url: str
        :return: {'name': name, 'realm': realm_slug, 'region': region}
        :rtype: dict
        """
        string = unquote(str(url))

        found = re.search(
            r"\/(us|eu|kr|tw|cn)\/([0-9\-\w]*)\/([a-zA-Z\w]*)", string, re.U
        )

        if found and found.group() and len(found.groups()) == 3:
            name = found.group(3).lower()
            realm_slug = found.group(2).lower()
            region = found.group(1).lower()

            return {'name': name, 'realm': realm_slug, 'region': region}

        return None

    async def getRealmSlug(self, input:str) -> Union[str, None]:
        """Attempts to match user input with a WoW realm and return it's slug

        :param input: A string to query the realms index with (full name, id, short name, etc)
        :type input: str
        :return: A matching realm's slug
        :rtype: str
        """
        if self.realms:
            for realm in self.realms:
                input = str(input).lower()
                if input in str(realm['name']).lower() or input in str(realm['fixed']).lower() or input in str(realm['slug']).lower() or input == str(realm['id']).lower():
                    return realm['slug']
        else:
            data = await self.Retail.GameData.getRealmsIndex()
            
            if data:
                self.realms = []
                for realm in data['realms']:
                    self.realms.append({'name': realm['name'], 'fixed': str(realm['name']).replace(" ",""), 'slug': realm['slug'], 'id': realm['id']})
                return await self.getRealmSlug(input)
                    
        return None

    async def getMoney(self, input:int) -> str:
        """Converts a WoW money value to a formatted string of Gold, Silver, and Copper

        :param input: A WoW currency/money value in copper
        :type input: int
        :return: {}g {}s {}c
        :rtype: str
        """
        
        gold = int(input / 10000)
        silver = int((input % 10000) / 100)
        copper = int((input % 10000) % 100)
        
        return f'{gold:,}g {silver:,}s {copper:,}c'
