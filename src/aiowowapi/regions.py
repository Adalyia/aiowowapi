from enum import Enum


class APIRegion(Enum):
    US: dict = {
        'oauth_api_hostname': 'https://us.battle.net{api_endpoint}',
        'game_api_hostname': 'https://us.api.blizzard.com{api_endpoint}',
        'supported_locales': ['en_US', 'es_MX', 'pt_BR']
    }
    EU: dict = {
        'oauth_api_hostname': 'https://eu.battle.net{api_endpoint}',
        'game_api_hostname': 'https://eu.api.blizzard.com{api_endpoint}',
        'supported_locales': ['en_GB', 'es_ES', 'fr_FR', 'ru_RU', 'de_DE', 'pt_PT', 'it_IT']
    }
    KR: dict = {
        'oauth_api_hostname': 'https://kr.battle.net{api_endpoint}',
        'game_api_hostname': 'https://kr.api.blizzard.com{api_endpoint}',
        'supported_locales': ['ko_KR']
    }
    TW: dict = {
        'oauth_api_hostname': 'https://tw.battle.net{api_endpoint}',
        'game_api_hostname': 'https://tw.api.blizzard.com{api_endpoint}',
        'supported_locales': ['zh_TW']
    }
    CN: dict = {
        'oauth_api_hostname': 'https://www.battlenet.com.cn{api_endpoint}',
        'game_api_hostname': 'https://gateway.battlenet.com.cn{api_endpoint}',
        'supported_locales': ['zh_CN']
    }
