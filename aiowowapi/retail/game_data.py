from typing import Union

class GameData():
    """This class contains all API endpoints for the GameData category of the Retail World of Warcraft API

    :param api: An instance of our generic API object
    :type api: API
    """
    def __init__(self, api):    
        """Constructor method
        """
        self.api = api
        
    
    async def getGameApiResource(self, namespace:str, endpoint:str, params:dict=None) -> Union[dict, None]:
        """Generic method for retrieving data from a Game Data API endpoint

        :param namespace: The namespace of the resource we're trying to access
        :type namespace: str
        :param endpoint: The API endpoint of the resource we're trying to access
        :type endpoint: str
        :param params: Parameters to send with the request, defaults to None
        :type params: dict, optional
        :return: The result of the API request (Warning: Can be None/Null)
        :rtype: dict
        """
        region = await self.api.getRegion()
        locale = await self.api.getLocale()
        hostname = await self.api.getHostname()
        token = await self.api.getAccessToken()
        
        if params is None:
            params = {}
       
        params["namespace"] =  namespace.format(region=region),
        params["locale"] = locale,
        params["access_token"] = token
        
        
        return await self.api.getResource(hostname, endpoint, params)
    
        
    #region Achievement API
    
    async def getAchievementCategoriesIndex(self) -> Union[dict, None]:
        """Returns an index of achievement categories.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/achievement-category/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getAchievementCategory(self, achievement_category_id:int) -> Union[dict, None]:
        """Returns an achievement category by ID.

        :param achievement_category_id: The ID of the achievement category.
        :type achievement_category_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/achievement-category/{achievement_category_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getAchievementsIndex(self) -> Union[dict, None]:
        """Returns an index of achievements.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/achievement/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getAchievement(self, achievement_id:int) -> Union[dict, None]:
        """Returns an achievement by ID.

        :param achievement_id: The ID of the achievement.
        :type achievement_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/achievement/{achievement_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getAchievementMedia(self, achievement_id:int) -> Union[dict, None]:
        """Returns media for an achievement by ID.

        :param achievement_id: The ID of the achievement.
        :type achievement_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/achievement/{achievement_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Auction House API
    
    async def getAuctions(self, connected_realm_id:int) -> Union[dict, None]:
        """Returns all active auctions for a connected realm.
        
        See the Connected Realm API for information about retrieving a list of connected realm IDs.
        
        Auction house data updates at a set interval. The value was initially set at 1 hour; however, it might change over time without notice.

        Depending on the number of active auctions on the specified connected realm, the response from this endpoint may be rather large, sometimes exceeding 10 MB.

        :param connected_realm_id: The ID of the connected realm.
        :type connected_realm_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/connected-realm/{connected_realm_id}/auctions"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Azerite Essence API
    
    async def getAzeriteEssencesIndex(self) -> Union[dict, None]:
        """Returns an index of azerite essences.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/azerite-essence/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getAzeriteEssence(self, azerite_essence_id:int) -> Union[dict, None]:
        """Returns an azerite essence by ID.

        :param azerite_essence_id: The ID of the azerite essence.
        :type azerite_essence_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/azerite-essence/{azerite_essence_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getAzeriteEssenceSearch(self, search_params:dict=None) -> Union[dict, None]:
        """Performs a search of azerite essences. For more detail/examples see the `Search Guide <https://develop.battle.net/documentation/world-of-warcraft/guides/search>`_

        :param search_params: Search parameters passed in the form of a dictionary, defaults to {}
        :type search_params: dict, optional
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/search/azerite-essence"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint, params=search_params)
    
    async def getAzeriteEssenceMedia(self, azerite_essence_id:int) -> Union[dict, None]:
        """Returns media for an azerite essence by ID.

        :param azerite_essence_id: The ID of the azerite essence.
        :type azerite_essence_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/azerite-essence/{azerite_essence_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Connected Realm API
    
    async def getConnectedRealmsIndex(self) -> Union[dict, None]:
        """Returns an index of connected realms.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/connected-realm/index"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getConnectedRealm(self, connected_realm_id:int) -> Union[dict, None]:
        """Returns a connected realm by ID.

        :param connected_realm_id: The ID of the connected realm.
        :type connected_realm_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/connected-realm/{connected_realm_id}"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getConnectedRealmsSearch(self, search_params:dict=None) -> Union[dict, None]:
        """Performs a search of connected realms. For more detail/examples see the `Search Guide <https://develop.battle.net/documentation/world-of-warcraft/guides/search>`_

        :param search_params: Search parameters passed in the form of a dictionary, defaults to {}
        :type search_params: dict, optional
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/search/connected-realm"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint, params=search_params)
    
    #endregion
    
    #region Covenant API
    
    async def getCovenantIndex(self) -> Union[dict, None]:
        """Returns an index of covenants.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/covenant/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getCovenant(self, covenant_id:int) -> Union[dict, None]:
        """Returns a covenant by ID.

        :param covenant_id: The ID of the covenant.
        :type covenant_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/covenant/{covenant_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getCovenantMedia(self, covenant_id:int) -> Union[dict, None]:
        """Returns media for a covenant by ID.

        :param covenant_id: The ID of the covenant.
        :type covenant_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/covenant/{covenant_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getSoulbindIndex(self) -> Union[dict, None]:
        """Returns an index of soulbinds.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/covenant/soulbind/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getSoulbind(self, soulbind_id:int) -> Union[dict, None]:
        """Returns a soulbind by ID.

        :param soulbind_id: The ID of the soulbind.
        :type soulbind_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/covenant/soulbind/{soulbind_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getConduitIndex(self) -> Union[dict, None]:
        """Returns an index of conduits.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/covenant/conduit/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getConduit(self, conduit_id:int) -> Union[dict, None]:
        """Returns a conduit by ID.

        :param conduit_id: The ID of the conduit.
        :type conduit_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/covenant/conduit/{conduit_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Creature API
    
    async def getCreatureFamiliesIndex(self) -> Union[dict, None]:
        """Returns an index of creature families.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/creature-family/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getCreatureFamily(self, creature_family_id:int) -> Union[dict, None]:
        """Returns a creature family by ID.

        :param creature_family_id: The ID of the creature family.
        :type creature_family_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/creature-family/{creature_family_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getCreatureTypesIndex(self) -> Union[dict, None]:
        """Returns an index of creature types.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/creature-type/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getCreatureType(self, creature_type_id:int) -> Union[dict, None]:
        """Returns a creature type by ID.

        :param creature_type_id: The ID of the creature type.
        :type creature_type_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/creature-type/{creature_type_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getCreature(self, creature_id:int) -> Union[dict, None]:
        """Returns a creature by ID.

        :param creature_id: The ID of the creature.
        :type creature_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/creature/{creature_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getCreatureSearch(self, search_params:dict=None) -> Union[dict, None]:
        """Performs a search of creatures. For more detail/examples see the `Search Guide <https://develop.battle.net/documentation/world-of-warcraft/guides/search>`_

        :param search_params: Search parameters passed in the form of a dictionary, defaults to {}
        :type search_params: dict, optional
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/search/creature"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint, params=search_params)
    
    async def getCreatureDisplayMedia(self, creature_display_id:int) -> Union[dict, None]:
        """Returns media for a creature display by ID.

        :param creature_display_id: The ID of the creature.
        :type creature_display_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/creature-display/{creature_display_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getCreatureFamilyMedia(self, creature_family_id:int) -> Union[dict, None]:
        """Returns media for a creature family by ID.

        :param creature_family_id: The ID of the creature.
        :type creature_family_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/creature-family/{creature_family_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Guild Crest API
    
    async def getGuildCrestComponentsIndex(self) -> Union[dict, None]:
        """Returns an index of guild crest media.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/guild-crest/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getGuildCrestBorderMedia(self, border_id:int) -> Union[dict, None]:
        """Returns media for a guild crest border by ID.

        :param border_id: The ID of the guild crest border.
        :type border_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/guild-crest/border/{border_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getGuildCrestEmblemMedia(self, emblem_id:int) -> Union[dict, None]:
        """Returns media for a guild crest emblem by ID.

        :param emblem_id: The ID of the guild crest emblem.
        :type emblem_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/guild-crest/emblem/{emblem_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Item API
    
    async def getItemClassesIndex(self) -> Union[dict, None]:
        """Returns an index of item classes.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/item-class/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getItemClass(self, item_class_id:int) -> Union[dict, None]:
        """Returns an item class by ID.

        :param item_class_id: The ID of the item class.
        :type item_class_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/item-class/{item_class_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getItemSetsIndex(self) -> Union[dict, None]:
        """Returns an index of item sets.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/item-set/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getItemSet(self, item_set_id:int) -> Union[dict, None]:
        """Returns an item set by ID.

        :param item_set_id: The ID of the item set.
        :type item_set_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/item-set/{item_set_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getItemSubclass(self, item_class_id:int, item_subclass_id:int) -> Union[dict, None]:
        """Returns an item subclass by ID.

        :param item_class_id: The ID of the item class.
        :type item_class_id: int
        :param item_subclass_id: The ID of the item subclass.
        :type item_subclass_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/item-class/{item_class_id}/item-subclass/{item_subclass_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getItem(self, item_id:int) -> Union[dict, None]:
        """Returns an item by ID.

        :param item_class_id: The ID of the item.
        :type item_class_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/item/{item_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getItemMedia(self, item_id:int) -> Union[dict, None]:
        """Returns media for an item by ID.

        :param item_class_id: The ID of the item.
        :type item_class_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/item/{item_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getItemSearch(self, search_params:dict=None) -> Union[dict, None]:
        """Performs a search of items. For more detail/examples see the `Search Guide <https://develop.battle.net/documentation/world-of-warcraft/guides/search>`_

        :param search_params: Search parameters passed in the form of a dictionary, defaults to {}
        :type search_params: dict, optional
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/search/item"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint, params=search_params)
    
    #endregion
    
    #region Journal API
    
    async def getJournalExpansionsIndex(self) -> Union[dict, None]:
        """Returns an index of journal expansions.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/journal-expansion/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getJournalExpansion(self, journal_expansion_id:int) -> Union[dict, None]:
        """Returns a journal expansion by ID.

        :param journal_expansion_id: The ID of the journal expansion.
        :type journal_expansion_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/journal-expansion/{journal_expansion_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getJournalEncountersIndex(self) -> Union[dict, None]:
        """Returns an index of journal encounters.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/journal-encounter/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getJournalEncounter(self, journal_encounter_id:int) -> Union[dict, None]:
        """Returns a journal encounter by ID.

        :param journal_encounter_id: The ID of the journal encounter.
        :type journal_encounter_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/journal-encounter/{journal_encounter_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getJournalEncounterSearch(self, search_params:dict=None) -> Union[dict, None]:
        """Performs a search of journal encounters. For more detail/examples see the `Search Guide <https://develop.battle.net/documentation/world-of-warcraft/guides/search>`_

        :param search_params: Search parameters passed in the form of a dictionary, defaults to {}
        :type search_params: dict, optional
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/search/journal-encounter"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint, params=search_params)
    
    async def getJournalInstancesIndex(self) -> Union[dict, None]:
        """Returns an index of journal instances.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/journal-instance/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getJournalInstance(self, journal_instance_id:int) -> Union[dict, None]:
        """Returns a journal instance.

        :param journal_instance_id: The ID of the journal instance.
        :type journal_instance_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/journal-instance/{journal_instance_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getJournalInstanceMedia(self, journal_instance_id:int) -> Union[dict, None]:
        """Returns media for a journal instance by ID.

        :param journal_instance_id: The ID of the journal instance.
        :type journal_instance_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/journal-instance/{journal_instance_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Media Search API
    
    async def getMediaSearch(self, search_params:dict=None) -> Union[dict, None]:
        """Performs a search of all types of media documents. For more detail/examples see the `Search Guide <https://develop.battle.net/documentation/world-of-warcraft/guides/search>`_

        :param search_params: Search parameters passed in the form of a dictionary, defaults to {}
        :type search_params: dict, optional
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/search/media"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint, params=search_params)
    
    #endregion
    
    #region Modified Crafting API
    
    async def getModifiedCraftingIndex(self) -> Union[dict, None]:
        """Returns the parent index for Modified Crafting.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/modified-crafting/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getModifiedCraftingCategoryIndex(self) -> Union[dict, None]:
        """Returns the index of Modified Crafting categories.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/modified-crafting/category/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getModifiedCraftingCategory(self, category_id:int) -> Union[dict, None]:
        """Returns a Modified Crafting category by ID.

        :param category_id: The ID of the Modified Crafting category.
        :type category_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/modified-crafting/category/{category_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getModifiedCraftingReagentSlotTypeIndex(self) -> Union[dict, None]:
        """Returns the index of Modified Crafting reagent slot types.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/modified-crafting/reagent-slot-type/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getModifiedCraftingReagentSlotType(self, slot_type_id:int) -> Union[dict, None]:
        """Returns a Modified Crafting reagent slot type by ID.
        
        :param slot_type_id: The ID of the Modified Crafting reagent slot type.
        :type slot_type_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/modified-crafting/reagent-slot-type/{slot_type_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Mount API
    
    async def getMountsIndex(self) -> Union[dict, None]:
        """Returns an index of mounts.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/mount/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getMount(self, mount_id:int) -> Union[dict, None]:
        """Returns a mount by ID.

        :param mount_id: The ID of the mount.
        :type mount_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/mount/{mount_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getMountSearch(self, search_params:dict=None) -> Union[dict, None]:
        """Performs a search of mounts. For more detail/examples see the `Search Guide <https://develop.battle.net/documentation/world-of-warcraft/guides/search>`_

        :param search_params: Search parameters passed in the form of a dictionary, defaults to {}
        :type search_params: dict, optional
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/search/mount"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint, params=search_params)
    
    #endregion
    
    #region Mythic Keystone Affix API
    
    async def getMythicKeystoneAffixesIndex(self) -> Union[dict, None]:
        """Returns an index of mythic keystone affixes.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/keystone-affix/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getMythicKeystoneAffix(self, keystone_affix_id:int) -> Union[dict, None]:
        """Returns a mythic keystone affix by ID.

        :param keystone_affix_id: The ID of the mythic keystone affix.
        :type keystone_affix_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/keystone-affix/{keystone_affix_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getMythicKeystoneAffixMedia(self, keystone_affix_id:int) -> Union[dict, None]:
        """Returns media for a mythic keystone affix by ID.

        :param keystone_affix_id: The ID of the mythic keystone affix.
        :type keystone_affix_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/keystone-affix/{keystone_affix_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Mythic Keystone Dungeon API
    
    async def getMythicKeystoneDungeonsIndex(self) -> Union[dict, None]:
        """Returns an index of Mythic Keystone dungeons.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/mythic-keystone/dungeon/index"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getMythicKeystoneDungeon(self, dungeon_id:int) -> Union[dict, None]:
        """Returns a Mythic Keystone dungeon by ID.

        :param dungeon_id: The ID of the dungeon.
        :type dungeon_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/mythic-keystone/dungeon/{dungeon_id}"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getMythicKeystoneIndex(self) -> Union[dict, None]:
        """Returns an index of Mythic Keystones.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/mythic-keystone/index"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getMythicKeystonePeriodsIndex(self) -> Union[dict, None]:
        """Returns an index of Mythic Keystone periods.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/mythic-keystone/period/index"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getMythicKeystonePeriod(self, period_id:int) -> Union[dict, None]:
        """Returns a Mythic Keystone period by ID.

        :param period_id: The ID of the Mythic Keystone season period.
        :type period_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/mythic-keystone/period/{period_id}"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getMythicKeystoneSeasonsIndex(self) -> Union[dict, None]:
        """Returns an index of Mythic Keystone seasons.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/mythic-keystone/season/index"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getMythicKeystoneSeason(self, season_id:int) -> Union[dict, None]:
        """Returns a Mythic Keystone season by ID.

        :param season_id: The ID of the Mythic Keystone season.
        :type season_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/mythic-keystone/season/{season_id}"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Mythic Keystone Leaderboard API
    
    async def getMythicKeystoneLeaderboardsIndex(self, connected_realm_id:int) -> Union[dict, None]:
        """Returns an index of Mythic Keystone Leaderboard dungeon instances for a connected realm.

        :param connected_realm_id: The ID of the connected realm.
        :type connected_realm_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/index"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getMythicKeystoneLeaderboard(self, connected_realm_id:int, dungeon_id:int, period_id:int) -> Union[dict, None]:
        """Returns a weekly Mythic Keystone Leaderboard by period.

        :param connected_realm_id: The ID of the connected realm.
        :type connected_realm_id: int
        :param dungeon_id: The ID of the dungeon.
        :type dungeon_id: int
        :param period_id: The unique identifier for the leaderboard period.
        :type period_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/{dungeon_id}/period/{period_id}"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Mythic Raid Leaderboard API
    
    async def getMythicRaidLeaderboard(self, raid:str, faction:str) -> Union[dict, None]:
        """Returns the leaderboard for a given raid and faction.

        :param raid: The raid for a leaderboard.
        :type raid: string
        :param faction: Player faction (alliance or horde).
        :type faction: string
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/leaderboard/hall-of-fame/{raid}/{faction}"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Pet API
    
    async def getPetsIndex(self) -> Union[dict, None]:
        """Returns an index of battle pets.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/pet/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPet(self, pet_id:int) -> Union[dict, None]:
        """Returns a battle pet by ID.

        :param pet_id: The ID of the pet.
        :type pet_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/pet/{pet_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPetMedia(self, pet_id:int) -> Union[dict, None]:
        """Returns media for a battle pet by ID.

        :param pet_id: The ID of the pet.
        :type pet_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/pet/{pet_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPetAbilitiesIndex(self) -> Union[dict, None]:
        """Returns an index of pet abilities.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/pet-ability/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPetAbility(self, pet_ability_id:int) -> Union[dict, None]:
        """Returns a pet ability by ID.

        :param pet_ability_id: The ID of the pet ability.
        :type pet_ability_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/pet-ability/{pet_ability_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPetAbilityMedia(self, pet_ability_id:int) -> Union[dict, None]:
        """Returns media for a pet ability by ID.

        :param pet_ability_id: The ID of the pet ability.
        :type pet_ability_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/pet-ability/{pet_ability_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Playable Class API
    
    async def getPlayableClassesIndex(self) -> Union[dict, None]:
        """Returns an index of playable classes.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-class/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPlayableClass(self, playable_class_id:int) -> Union[dict, None]:
        """Returns a playable class by ID.

        :param playable_class_id: The ID of the playable class.
        :type playable_class_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-class/{playable_class_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPlayableClassMedia(self, playable_class_id:int) -> Union[dict, None]:
        """Returns media for a playable class by ID.

        :param playable_class_id: The ID of the playable class.
        :type playable_class_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/playable-class/{playable_class_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPvPTalentSlots(self, playable_class_id:int) -> Union[dict, None]:
        """Returns the PvP talent slots for a playable class by ID.

        :param playable_class_id: The ID of the playable class.
        :type playable_class_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-class/{playable_class_id}/pvp-talent-slots"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Playable Race API
    
    async def getPlayableRacesIndex(self) -> Union[dict, None]:
        """Returns an index of playable races.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-race/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPlayableRace(self, playable_race_id:int) -> Union[dict, None]:
        """Returns a playable race by ID.

        :param playable_race_id: The ID of the playable race.
        :type playable_race_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-race/{playable_race_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Playable Specialization API
    
    async def getPlayableSpecializationIndex(self) -> Union[dict, None]:
        """Returns an index of playable specializations.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-specialization/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPlayableSpecialization(self, playable_specialization_id:int) -> Union[dict, None]:
        """Returns a playable specialization by ID.

        :param playable_specialization_id: The ID of the playable specialization.
        :type playable_specialization_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-specialization/{playable_specialization_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPlayableSpecializationMedia(self, playable_specialization_id:int) -> Union[dict, None]:
        """Returns media for a playable specialization by ID.

        :param playable_specialization_id: The ID of the playable specialization.
        :type playable_specialization_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/playable-specialization/{playable_specialization_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Power Type API
    
    async def getPowerTypesIndex(self) -> Union[dict, None]:
        """Returns an index of power types.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/power-type/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPowerType(self, power_type_id:int) -> Union[dict, None]:
        """Returns a power type by ID.

        :param power_type_id: The ID of the power type.
        :type power_type_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/power-type/{power_type_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Profession API
    
    async def getProfessionsIndex(self) -> Union[dict, None]:
        """Returns an index of professions.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/profession/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getProfession(self, profession_id:int) -> Union[dict, None]:
        """Returns a profession by ID.

        :param profession_id: The ID of the profession.
        :type profession_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/profession/{profession_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getProfessionMedia(self, profession_id:int) -> Union[dict, None]:
        """Returns media for a profession by ID.

        :param profession_id: The ID of the profession.
        :type profession_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/profession/{profession_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getProfessionSkillTier(self, profession_id:int, skill_tier_id:int) -> Union[dict, None]:
        """Returns a skill tier for a profession by ID.

        :param profession_id: The ID of the profession.
        :type profession_id: int
        :param skill_tier_id: The ID of the skill tier.
        :type skill_tier_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/profession/{profession_id}/skill-tier/{skill_tier_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getRecipe(self, recipe_id:int) -> Union[dict, None]:
        """Returns a recipe by ID.

        :param recipe_id: The ID of the recipe.
        :type recipe_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/recipe/{recipe_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getRecipeMedia(self, recipe_id:int) -> Union[dict, None]:
        """Returns media for a recipe by ID.

        :param recipe_id: The ID of the recipe.
        :type recipe_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/recipe/{recipe_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region PvP Season API
    
    async def getPvPSeasonsIndex(self) -> Union[dict, None]:
        """Returns an index of PvP seasons.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-season/index"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPvPSeason(self, pvp_season_id:int) -> Union[dict, None]:
        """Returns a PvP season by ID.

        :param pvp_season_id: The ID of the PvP season.
        :type pvp_season_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-season/{pvp_season_id}"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPvPLeaderboardsIndex(self, pvp_season_id:int) -> Union[dict, None]:
        """Returns an index of PvP leaderboards for a PvP season.

        :param pvp_season_id: The ID of the PvP season.
        :type pvp_season_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/index"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPvPLeaderboard(self, pvp_season_id:int, pvp_bracket) -> Union[dict, None]:
        """Returns a PvP season by ID.

        :param pvp_season_id: The ID of the PvP season.
        :type pvp_season_id: int
        :param pvp_bracket: The PvP bracket type. (ex: 3v3, 2v2)
        :type pvp_bracket: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/{pvp_bracket}"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPvPRewardsIndex(self, pvp_season_id:int) -> Union[dict, None]:
        """Returns an index of PvP rewards for a PvP season.

        :param pvp_season_id: The ID of the PvP season.
        :type pvp_season_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-season/{pvp_season_id}/pvp-reward/index"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region PvP Tier API
    
    async def getPvPTiersIndex(self) -> Union[dict, None]:
        """Returns an index of PvP tiers.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-tier/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPvPTier(self, pvp_tier_id:int) -> Union[dict, None]:
        """Returns a PvP tier by ID.

        :param pvp_tier_id: The ID of the PvP tier.
        :type pvp_tier_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-tier/{pvp_tier_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPvPTierMedia(self, pvp_tier_id:int) -> Union[dict, None]:
        """Returns media for a PvP tier by ID.

        :param pvp_tier_id: The ID of the PvP tier.
        :type pvp_tier_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/pvp-tier/{pvp_tier_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Quest API
    
    async def getQuestsIndex(self) -> Union[dict, None]:
        """Returns the parent index for quests.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getQuest(self, quest_id:int) -> Union[dict, None]:
        """Returns a quest by ID.

        :param quest_id: The ID of the quest.
        :type quest_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/{quest_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getQuestCategoriesIndex(self) -> Union[dict, None]:
        """Returns an index of quest categories (such as quests for a specific class, profession, or storyline).

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/category/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getQuestCategory(self, quest_category_id:int) -> Union[dict, None]:
        """Returns a quest category by ID.

        :param quest_category_id: The ID of the quest category.
        :type quest_category_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/category/{quest_category_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getQuestAreasIndex(self) -> Union[dict, None]:
        """Returns an index of quest areas.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/area/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getQuestArea(self, quest_area_id:int) -> Union[dict, None]:
        """Returns a quest area by ID.

        :param quest_area_id: The ID of the quest area.
        :type quest_area_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/area/{quest_area_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getQuestTypesIndex(self) -> Union[dict, None]:
        """Returns an index of quest types (such as PvP quests, raid quests, or account quests).

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/type/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getQuestType(self, quest_type_id:int) -> Union[dict, None]:
        """Returns a quest type by ID.

        :param quest_type_id: The ID of the quest area.
        :type quest_type_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/type/{quest_type_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Realm API
    
    async def getRealmsIndex(self) -> Union[dict, None]:
        """Returns an index of realms.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/realm/index"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getRealm(self, realm_slug:str) -> Union[dict, None]:
        """Returns a single realm by slug or numerical ID.

        :param realm_slug: The slug/id of the realm.
        :type realm_slug: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/realm/{realm_slug}"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getRealmSearch(self, search_params:dict=None) -> Union[dict, None]:
        """Performs a search of realms. For more detail/examples see the `Search Guide <https://develop.battle.net/documentation/world-of-warcraft/guides/search>`_

        :param search_params: Search parameters passed in the form of a dictionary, defaults to {}
        :type search_params: dict, optional
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/search/realm"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint, params=search_params)
    
    #endregion
    
    #region Region API
    
    async def getRegionsIndex(self) -> Union[dict, None]:
        """Returns an index of regions.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/region/index"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getRegion(self, region_id:int) -> Union[dict, None]:
        """Returns a region by ID.

        :param region_id: The ID of the region.
        :type region_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/region/{region_id}"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Reputations API
    
    async def getReputationFactionsIndex(self) -> Union[dict, None]:
        """Returns an index of reputation factions.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/reputation-faction/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getReputationFaction(self, reputation_faction_id:int) -> Union[dict, None]:
        """Returns a single reputation faction by ID.

        :param reputation_faction_id: The ID of the reputation faction.
        :type reputation_faction_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/reputation-faction/{reputation_faction_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getReputationTiersIndex(self) -> Union[dict, None]:
        """Returns an index of reputation tiers.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/reputation-tiers/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getReputationTiers(self, reputation_tiers_id:int) -> Union[dict, None]:
        """Returns a single set of reputation tiers by ID.

        :param reputation_tiers_id: The ID of the set of reputation tiers.
        :type reputation_tiers_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/reputation-tiers/{reputation_tiers_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Spell API
    
    async def getSpell(self, spell_id:int) -> Union[dict, None]:
        """Returns a spell by ID.

        :param spell_id: The ID of the spell.
        :type spell_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/spell/{spell_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getSpellMedia(self, spell_id:int) -> Union[dict, None]:
        """Returns media for a spell by ID.

        :param spell_id: The ID of the spell.
        :type spell_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/spell/{spell_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getSpellSearch(self, search_params:dict=None) -> Union[dict, None]:
        """Performs a search of spells. For more detail/examples see the `Search Guide <https://develop.battle.net/documentation/world-of-warcraft/guides/search>`_

        :param search_params: Search parameters passed in the form of a dictionary, defaults to {}
        :type search_params: dict, optional
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/search/spell"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint, params=search_params)
    
    #endregion
    
    #region Talent API
    
    async def getTalentsIndex(self) -> Union[dict, None]:
        """Returns an index of talents.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/talent/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getTalent(self, talent_id:int) -> Union[dict, None]:
        """Returns a talent by ID.

        :param talent_id: The ID of the talent.
        :type talent_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/talent/{talent_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPvPTalentsIndex(self) -> Union[dict, None]:
        """Returns an index of PvP talents.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-talent/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getPvPTalent(self, pvp_talent_id:int) -> Union[dict, None]:
        """Returns a PvP talent by ID.

        :param pvp_talent_id: The ID of the PvP talent.
        :type pvp_talent_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-talent/{pvp_talent_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Tech Talent API
    
    async def getTechTalentTreeIndex(self) -> Union[dict, None]:
        """Returns an index of tech talent trees.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/tech-talent-tree/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getTechTalentTree(self, tech_talent_tree_id:int) -> Union[dict, None]:
        """Returns a tech talent tree by ID.

        :param tech_talent_tree_id: The ID of the tech talent tree.
        :type tech_talent_tree_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/tech-talent-tree/{tech_talent_tree_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getTechTalentIndex(self) -> Union[dict, None]:
        """Returns an index of tech talents.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/tech-talent/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getTechTalent(self, tech_talent_id:int) -> Union[dict, None]:
        """Returns a tech talent by ID.

        :param tech_talent_id: The ID of the tech talent.
        :type tech_talent_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/tech-talent/{tech_talent_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getTechTalentMedia(self, tech_talent_id:int) -> Union[dict, None]:
        """Returns media for a tech talent by ID.

        :param tech_talent_id: The ID of the tech talent.
        :type tech_talent_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/media/tech-talent/{tech_talent_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region Title API
    
    async def getTitlesIndex(self) -> Union[dict, None]:
        """Returns an index of titles.



        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/title/index"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    async def getTitle(self, title_id:int) -> Union[dict, None]:
        """Returns a title by ID.

        :param title_id: The ID of the title.
        :type title_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/title/{title_id}"
        
        namespace = 'static-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion
    
    #region WoW Token API
    
    async def getWoWTokenIndex(self) -> Union[dict, None]:
        """Returns the WoW Token index.

        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/token/index"
        
        namespace = 'dynamic-{region}'
        
        return await self.getGameApiResource(namespace, endpoint)
    
    #endregion