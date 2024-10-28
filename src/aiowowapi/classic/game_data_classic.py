from typing import Union, Optional


class GameData:
    """This class contains all API endpoints for the GameData category of the
    Classic World of Warcraft API

    :param api: An instance of our generic API object
    :type api: API
    """

    def __init__(self, api):
        """Constructor method
        """
        self.api = api

    async def get_game_api_resource(self,
                                    namespace: str,
                                    endpoint: str,
                                    params: dict = None
                                    ) -> Union[dict, None]:
        """Generic method for retrieving data from a Game Data API endpoint

        :param namespace: The namespace of the resource we're trying to access
        :type namespace: str
        :param endpoint: The endpoint of the resource we're trying to access
        :type endpoint: str
        :param params: Parameters to send with the request, defaults to None
        :type params: dict, optional
        :return: The result of the API request (Warning: Can be None/Null)
        :rtype: dict
        """
        region = self.api.get_region()
        locale = self.api.get_locale()
        hostname = self.api.get_hostname()
        token = await self.api.get_access_token()

        if params is None:
            params = {}

        params["namespace"] = namespace.format(region=region),
        params["locale"] = locale,

        # Thank you to https://github.com/karlsbjorn and https://github.com/mty22
        # https://github.com/Adalyia/aiowowapi/pull/2
        headers = {"Authorization": f"Bearer {token}"}


        return await self.api.get_resource(hostname, endpoint, params, headers)

# region Auction House API

    async def get_auction_house_index(self,
                                      connected_realm_id: int
                                      ):
        """Returns an index of auction houses for a connected realm.

See the Connected Realm API for information about retrieving a list of connected realm IDs.
        
        :param connected_realm_id: The ID of the connected realm.
        :type connected_realm_id: int
        :return: Returns an index of auction houses for a connected realm.
        :rtype: dict
        """
        endpoint = f"/data/wow/connected-realm/{connected_realm_id}/auctions/index"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_auctions(self,
                           connected_realm_id: int,
                           auction_house_id: int
                           ):
        """Returns all active auctions for a specific auction house on a connected realm.

See the Connected Realm API for information about retrieving a list of connected realm IDs.

Auction house data updates at a set interval. The value was initially set at 1 hour; however, it might change over time without notice.

Depending on the number of active auctions on the specified connected realm, the response from this endpoint may be rather large, sometimes exceeding 10 MB.
        
        :param connected_realm_id: The ID of the connected realm.
        :type connected_realm_id: int
        :param auction_house_id: The ID of the auction house.
        :type auction_house_id: int
        :return: Returns all active auctions for a specific auction house on a connected realm.
        :rtype: dict
        """
        endpoint = f"/data/wow/connected-realm/{connected_realm_id}/auctions/{auction_house_id}"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

# endregion
# region Connected Realm API

    async def get_connected_realms_index(self):
        """Returns an index of connected realms.
        
        :return: Returns an index of connected realms.
        :rtype: dict
        """
        endpoint = f"/data/wow/connected-realm/index"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_connected_realm(self,
                                  connected_realm_id: int
                                  ):
        """Returns a connected realm by ID.
        
        :param connected_realm_id: The ID of the connected realm.
        :type connected_realm_id: int
        :return: Returns a connected realm by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/connected-realm/{connected_realm_id}"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_connected_realms_search(self,
                                          search_params: Optional[dict] = None
                                          ):
        """Performs a search of connected realms. The fields below are provided for example. For more detail see the Search Guide.
        
        :param search_params: Search parameters
        :type search_params: dict
        :return: Performs a search of connected realms. The fields below are provided for example. For more detail see the Search Guide.
        :rtype: dict
        """
        endpoint = f"/data/wow/search/connected-realm"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint, 
                                                params=search_params)

# endregion
# region Creature API

    async def get_creature_families_index(self):
        """Returns an index of creature families.
        
        :return: Returns an index of creature families.
        :rtype: dict
        """
        endpoint = f"/data/wow/creature-family/index"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_creature_family(self,
                                  creature_family_id: int
                                  ):
        """Returns a creature family by ID.
        
        :param creature_family_id: The ID of the creature family.
        :type creature_family_id: int
        :return: Returns a creature family by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/creature-family/{creature_family_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_creature_types_index(self):
        """Returns an index of creature types.
        
        :return: Returns an index of creature types.
        :rtype: dict
        """
        endpoint = f"/data/wow/creature-type/index"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_creature_type(self,
                                creature_type_id: int
                                ):
        """Returns a creature type by ID.
        
        :param creature_type_id: The ID of the creature type.
        :type creature_type_id: int
        :return: Returns a creature type by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/creature-type/{creature_type_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_creature(self,
                           creature_id: int
                           ):
        """Returns a creature by ID.
        
        :param creature_id: The ID of the creature.
        :type creature_id: int
        :return: Returns a creature by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/creature/{creature_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_creature_search(self,
                                  search_params: Optional[dict] = None
                                  ):
        """Performs a search of creatures. The fields below are provided for example. For more detail see the Search Guide.
        
        :param search_params: Search parameters
        :type search_params: dict
        :return: Performs a search of creatures. The fields below are provided for example. For more detail see the Search Guide.
        :rtype: dict
        """
        endpoint = f"/data/wow/search/creature"
        namespace = "static-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint, 
                                                params=search_params)

    async def get_creature_display_media(self,
                                         creature_display_id: int
                                         ):
        """Returns media for a creature display by ID.
        
        :param creature_display_id: The ID of the creature display.
        :type creature_display_id: int
        :return: Returns media for a creature display by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/creature-display/{creature_display_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_creature_family_media(self,
                                        creature_family_id: int
                                        ):
        """Returns media for a creature family by ID.
        
        :param creature_family_id: The ID of the creature family.
        :type creature_family_id: int
        :return: Returns media for a creature family by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/creature-family/{creature_family_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

# endregion
# region Guild Crest API

    async def get_guild_crest_components_index(self):
        """Returns an index of guild crest media.
        
        :return: Returns an index of guild crest media.
        :rtype: dict
        """
        endpoint = f"/data/wow/guild-crest/index"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_guild_crest_border_media(self,
                                           border_id: int
                                           ):
        """Returns media for a guild crest border by ID.
        
        :param border_id: The ID of the guild crest border.
        :type border_id: int
        :return: Returns media for a guild crest border by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/guild-crest/border/{border_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_guild_crest_emblem_media(self,
                                           emblem_id: int
                                           ):
        """Returns media for a guild crest emblem by ID.
        
        :param emblem_id: The ID of the guild crest emblem.
        :type emblem_id: int
        :return: Returns media for a guild crest emblem by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/guild-crest/emblem/{emblem_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

# endregion
# region Item API

    async def get_item_classes_index(self):
        """Returns an index of item classes.
        
        :return: Returns an index of item classes.
        :rtype: dict
        """
        endpoint = f"/data/wow/item-class/index"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_item_class(self,
                             item_class_id: str
                             ):
        """Returns an item class by ID.
        
        :param item_class_id: The ID of the item class.
        :type item_class_id: str
        :return: Returns an item class by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/item-class/{item_class_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_item_subclass(self,
                                item_class_id: str,
                                item_subclass_id: str
                                ):
        """Returns an item subclass by ID.
        
        :param item_class_id: The ID of the item class.
        :type item_class_id: str
        :param item_subclass_id: The ID of the item subclass.
        :type item_subclass_id: str
        :return: Returns an item subclass by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/item-class/{item_class_id}/item-subclass/{item_subclass_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_item(self,
                       item_id: str
                       ):
        """Returns an item by ID.
        
        :param item_id: The ID of the item.
        :type item_id: str
        :return: Returns an item by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/item/{item_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_item_media(self,
                             item_id: int
                             ):
        """Returns media for an item by ID.
        
        :param item_id: The ID of the item.
        :type item_id: int
        :return: Returns media for an item by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/item/{item_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_item_search(self,
                              search_params: Optional[dict] = None
                              ):
        """Performs a search of items. The fields below are provided for example. For more detail see the Search Guide.
        
        :param search_params: Search parameters
        :type search_params: dict
        :return: Performs a search of items. The fields below are provided for example. For more detail see the Search Guide.
        :rtype: dict
        """
        endpoint = f"/data/wow/search/item"
        namespace = "static-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint, 
                                                params=search_params)

# endregion
# region Media Search API

    async def get_media_search(self,
                               search_params: Optional[dict] = None
                               ):
        """Performs a search of all types of media documents. The fields below are provided for example. For more detail see the Search Guide.
        
        :param search_params: Search parameters
        :type search_params: dict
        :return: Performs a search of all types of media documents. The fields below are provided for example. For more detail see the Search Guide.
        :rtype: dict
        """
        endpoint = f"/data/wow/search/media"
        namespace = "static-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint, 
                                                params=search_params)

# endregion
# region Playable Class API

    async def get_playable_classes_index(self):
        """Returns an index of playable classes.
        
        :return: Returns an index of playable classes.
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-class/index"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_playable_class(self,
                                 class_id: int
                                 ):
        """Returns a playable class by ID.
        
        :param class_id: The ID of the playable class.
        :type class_id: int
        :return: Returns a playable class by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-class/{class_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_playable_class_media(self,
                                       playable_class_id: int
                                       ):
        """Returns media for a playable class by ID.
        
        :param playable_class_id: The ID of the playable class.
        :type playable_class_id: int
        :return: Returns media for a playable class by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/playable-class/{playable_class_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

# endregion
# region Playable Race API

    async def get_playable_races_index(self):
        """Returns an index of playable races.
        
        :return: Returns an index of playable races.
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-race/index"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_playable_race(self,
                                playable_race_id: int
                                ):
        """Returns a playable race by ID.
        
        :param playable_race_id: The ID of the playable race.
        :type playable_race_id: int
        :return: Returns a playable race by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-race/{playable_race_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

# endregion
# region Power Type API

    async def get_power_types_index(self):
        """Returns an index of power types.
        
        :return: Returns an index of power types.
        :rtype: dict
        """
        endpoint = f"/data/wow/power-type/index"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_power_type(self,
                             power_type_id: int
                             ):
        """Returns a power type by ID.
        
        :param power_type_id: The ID of the power type.
        :type power_type_id: int
        :return: Returns a power type by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/power-type/{power_type_id}"
        namespace = "static-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

# endregion
# region PvP Season API

    async def get_pvp_seasons_index(self):
        """Returns an index of PvP seasons.
        
        :return: Returns an index of PvP seasons.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-season/index"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_pvp_season(self,
                             pvp_season_id: int
                             ):
        """Returns a PvP season by ID.
        
        :param pvp_season_id: The ID of the PvP season.
        :type pvp_season_id: int
        :return: Returns a PvP season by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-season/{pvp_season_id}"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_pvp_region_index(self):
        """Returns an index of PvP Regions.
        
        :return: Returns an index of PvP Regions.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-region/index"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_pvp_regional_season_index(self,
                                            pvp_region_id: int
                                            ):
        """Returns an index of PvP Seasons in a PvP region.
        
        :param pvp_region_id: The ID of the PvP region.
        :type pvp_region_id: int
        :return: Returns an index of PvP Seasons in a PvP region.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-region/{pvp_region_id}/pvp-season/index"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_pvp_regional_season(self,
                                      pvp_region_id: int,
                                      pvp_season_id: int
                                      ):
        """Returns a PvP season by region ID and season ID.
        
        :param pvp_region_id: The ID of the PvP region.
        :type pvp_region_id: int
        :param pvp_season_id: The ID of the PvP season.
        :type pvp_season_id: int
        :return: Returns a PvP season by region ID and season ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-region/{pvp_region_id}/pvp-season/{pvp_season_id}"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_pvp_leaderboards_index(self,
                                         pvp_region_id: int,
                                         pvp_season_id: int
                                         ):
        """Returns an index of PvP leaderboards for a PvP season in a given PvP region.
        
        :param pvp_region_id: The ID of the PvP region.
        :type pvp_region_id: int
        :param pvp_season_id: The ID of the PvP season.
        :type pvp_season_id: int
        :return: Returns an index of PvP leaderboards for a PvP season in a given PvP region.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-region/{pvp_region_id}/pvp-season/{pvp_season_id}/pvp-leaderboard/index"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_pvp_leaderboard(self,
                                  pvp_region_id: int,
                                  pvp_season_id: int,
                                  pvp_bracket: str
                                  ):
        """Returns the PvP leaderboard of a specific PvP bracket for a PvP season in a given PvP region.
        
        :param pvp_region_id: The ID of the PvP region.
        :type pvp_region_id: int
        :param pvp_season_id: The ID of the PvP season.
        :type pvp_season_id: int
        :param pvp_bracket: The PvP bracket type.
        :type pvp_bracket: str
        :return: Returns the PvP leaderboard of a specific PvP bracket for a PvP season in a given PvP region.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-region/{pvp_region_id}/pvp-season/{pvp_season_id}/pvp-leaderboard/{pvp_bracket}"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_pvp_rewards_index(self,
                                    pvp_region_id: int,
                                    pvp_season_id: int
                                    ):
        """Returns an index of PvP rewards for a PvP season in a given PvP region.
        
        :param pvp_region_id: The ID of the PvP region.
        :type pvp_region_id: int
        :param pvp_season_id: The ID of the PvP season.
        :type pvp_season_id: int
        :return: Returns an index of PvP rewards for a PvP season in a given PvP region.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-region/{pvp_region_id}/pvp-season/{pvp_season_id}/pvp-reward/index"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

# endregion
# region Realm API

    async def get_realms_index(self):
        """Returns an index of realms.
        
        :return: Returns an index of realms.
        :rtype: dict
        """
        endpoint = f"/data/wow/realm/index"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_realm(self,
                        realm_slug: str
                        ):
        """Returns a single realm by slug or ID.
        
        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :return: Returns a single realm by slug or ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/realm/{realm_slug}"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_realm_search(self,
                               search_params: Optional[dict] = None
                               ):
        """Performs a search of realms. The fields below are examples only. For more detail see the Search Guide.
        
        :param search_params: Search parameters
        :type search_params: dict
        :return: Performs a search of realms. The fields below are examples only. For more detail see the Search Guide.
        :rtype: dict
        """
        endpoint = f"/data/wow/search/realm"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint, 
                                                params=search_params)

# endregion
# region Region API

    async def get_regions_index(self):
        """Returns an index of regions.
        
        :return: Returns an index of regions.
        :rtype: dict
        """
        endpoint = f"/data/wow/region/index"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

    async def get_region(self,
                         region_id: int
                         ):
        """Returns a region by ID.
        
        :param region_id: The ID of the region.
        :type region_id: int
        :return: Returns a region by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/region/{region_id}"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

# endregion
# region WoW Token API

    async def get_wow_token_index_cn(self):
        """Returns the WoW Token index.
        
        :return: Returns the WoW Token index.
        :rtype: dict
        """
        endpoint = f"/data/wow/token/index"
        namespace = "dynamic-classic-{region}"

        return await self.get_game_api_resource(
                                                namespace, 
                                                endpoint)

# endregion
