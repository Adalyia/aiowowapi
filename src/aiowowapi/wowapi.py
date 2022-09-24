import re
from typing import Union, Dict, Optional
from urllib.parse import *

from . import API
from .classic.classic import ClassicApi
from .retail.retail import RetailApi


class WowApi(API):
    def __init__(self, *args, **kwargs):
        """This class contains some useful functions/QoL features for working with the World of Warcraft API.
        For additional arguments see the API class documentation.
        """
        super().__init__(*args, **kwargs)

        self.Retail = RetailApi(super())
        self.Classic = ClassicApi(super())

        self.__realms = None

    @staticmethod
    async def parse_armory_link(url: str) -> Optional[Dict[str, str]]:
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

    async def get_realm_slug(self, realm_name: str) -> Optional[str]:
        """Attempts to match user input with a WoW realm and return its slug

        :param realm_name: A string to query the realms index with (full name, id, short name, etc)
        :type realm_name: str
        :return: A matching realm's slug
        :rtype: str
        """
        if self.__realms:
            for realm in self.__realms:
                realm_name = str(realm_name).lower()
                if realm_name in str(realm['name']).lower() or realm_name in str(
                        realm['fixed']).lower() or realm_name in str(
                        realm['slug']).lower() or realm_name == str(realm['id']).lower():
                    return realm['slug']
        else:
            data = await self.Retail.GameData.get_realms_index()

            if data:
                self.__realms = []
                for realm in data['realms']:
                    self.__realms.append(
                        {'name': realm['name'], 'fixed': str(realm['name']).replace(" ", ""), 'slug': realm['slug'],
                         'id': realm['id']})
                return await self.get_realm_slug(realm_name)

        return None

    @staticmethod
    async def format_wow_gold(money: int) -> str:
        """Converts a WoW money value to a formatted string of Gold, Silver, and Copper

        :param money: A WoW currency/money value in copper
        :type money: int
        :return: {}g {}s {}c
        :rtype: str
        """

        gold = int(money / 10000)
        silver = int((money % 10000) / 100)
        copper = int((money % 10000) % 100)

        return f'{gold:,}g {silver:,}s {copper:,}c'
