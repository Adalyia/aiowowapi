from typing import Union, Optional


class GameData:
    """This class contains all API endpoints for the GameData category of the Retail World of Warcraft API

    :param api: An instance of our generic API object
    :type api: API
    """

    def __init__(self, api):
        """Constructor method
        """
        self.api = api

    async def get_game_api_resource(self, namespace: str, endpoint: str, params: dict = None) -> Union[dict, None]:
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
        region = await self.api.get_region()
        locale = await self.api.get_locale()
        hostname = await self.api.get_hostname()
        token = await self.api.get_access_token()

        if params is None:
            params = {}

        params["namespace"] = namespace.format(region=region),
        params["locale"] = locale,
        params["access_token"] = token

        return await self.api.get_resource(hostname, endpoint, params)
# region Achievement API

    async def get_achievement_categories_index(self):
        """Returns an index of achievement categories.
        
        :return: Returns an index of achievement categories.
        :rtype: dict
        """
        endpoint = f"/data/wow/achievement-category/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_achievement_category(self, achievement_category_id: int):
        """Returns an achievement category by ID.
        
        :param achievement_category_id: The ID of the achievement category.
        :type achievement_category_id: int
        :return: Returns an achievement category by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/achievement-category/{achievement_category_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_achievements_index(self):
        """Returns an index of achievements.
        
        :return: Returns an index of achievements.
        :rtype: dict
        """
        endpoint = f"/data/wow/achievement/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_achievement(self, achievement_id: int):
        """Returns an achievement by ID.
        
        :param achievement_id: The ID of the achievement.
        :type achievement_id: int
        :return: Returns an achievement by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/achievement/{achievement_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_achievement_media(self, achievement_id: int):
        """Returns media for an achievement by ID.
        
        :param achievement_id: The ID of the achievement.
        :type achievement_id: int
        :return: Returns media for an achievement by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/achievement/{achievement_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Auction House API

    async def get_auctions(self, connected_realm_id: int):
        """Returns all active auctions for a connected realm.

See the Connected Realm API for information about retrieving a list of connected realm IDs.

Auction house data updates at a set interval. The value was initially set at 1 hour; however, it might change over time without notice.

Depending on the number of active auctions on the specified connected realm, the response from this endpoint may be rather large, sometimes exceeding 10 MB.
        
        :param connected_realm_id: The ID of the connected realm.
        :type connected_realm_id: int
        :return: Returns all active auctions for a connected realm.
        :rtype: dict
        """
        endpoint = f"/data/wow/connected-realm/{connected_realm_id}/auctions"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Azerite Essence API

    async def get_azerite_essences_index(self):
        """Returns an index of azerite essences.
        
        :return: Returns an index of azerite essences.
        :rtype: dict
        """
        endpoint = f"/data/wow/azerite-essence/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_azerite_essence(self, azerite_essence_id: str):
        """Returns an azerite essence by ID.
        
        :param azerite_essence_id: The ID of the azerite essence.
        :type azerite_essence_id: str
        :return: Returns an azerite essence by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/azerite-essence/{azerite_essence_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_azerite_essence_search(self, search_params: Optional[dict] = None):
        """Performs a search of azerite essences. The fields below are provided for example. For more detail see the Search Guide.
        
        :param search_params: Search parameters
        :type search_params: dict
        :return: Performs a search of azerite essences. The fields below are provided for example. For more detail see the Search Guide.
        :rtype: dict
        """
        endpoint = f"/data/wow/search/azerite-essence"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint, params=search_params)

    async def get_azerite_essence_media(self, azerite_essence_id: int):
        """Returns media for an azerite essence by ID.
        
        :param azerite_essence_id: The ID of the azerite essence.
        :type azerite_essence_id: int
        :return: Returns media for an azerite essence by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/azerite-essence/{azerite_essence_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Connected Realm API

    async def get_connected_realms_index(self):
        """Returns an index of connected realms.
        
        :return: Returns an index of connected realms.
        :rtype: dict
        """
        endpoint = f"/data/wow/connected-realm/index"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_connected_realm(self, connected_realm_id: int):
        """Returns a connected realm by ID.
        
        :param connected_realm_id: The ID of the connected realm.
        :type connected_realm_id: int
        :return: Returns a connected realm by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/connected-realm/{connected_realm_id}"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_connected_realms_search(self, search_params: Optional[dict] = None):
        """Performs a search of connected realms. The fields below are provided for example. For more detail see the Search Guide.
        
        :param search_params: Search parameters
        :type search_params: dict
        :return: Performs a search of connected realms. The fields below are provided for example. For more detail see the Search Guide.
        :rtype: dict
        """
        endpoint = f"/data/wow/search/connected-realm"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint, params=search_params)

# endregion
# region Covenant API

    async def get_covenant_index(self):
        """Returns an index of covenants.
        
        :return: Returns an index of covenants.
        :rtype: dict
        """
        endpoint = f"/data/wow/covenant/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_covenant(self, covenant_id: int):
        """Returns a covenant by ID.
        
        :param covenant_id: The ID of the covenant.
        :type covenant_id: int
        :return: Returns a covenant by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/covenant/{covenant_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_covenant_media(self, covenant_id: int):
        """Returns media for a covenant by ID.
        
        :param covenant_id: The ID of the covenant.
        :type covenant_id: int
        :return: Returns media for a covenant by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/covenant/{covenant_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_soulbind_index(self):
        """Returns an index of soulbinds.
        
        :return: Returns an index of soulbinds.
        :rtype: dict
        """
        endpoint = f"/data/wow/covenant/soulbind/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_soulbind(self, soulbind_id: int):
        """Returns a soulbind by ID.
        
        :param soulbind_id: The ID of the soulbind.
        :type soulbind_id: int
        :return: Returns a soulbind by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/covenant/soulbind/{soulbind_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_conduit_index(self):
        """Returns an index of conduits.
        
        :return: Returns an index of conduits.
        :rtype: dict
        """
        endpoint = f"/data/wow/covenant/conduit/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_conduit(self, conduit_id: int):
        """Returns a conduit by ID.
        
        :param conduit_id: The ID of the conduit.
        :type conduit_id: int
        :return: Returns a conduit by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/covenant/conduit/{conduit_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Creature API

    async def get_creature_families_index(self):
        """Returns an index of creature families.
        
        :return: Returns an index of creature families.
        :rtype: dict
        """
        endpoint = f"/data/wow/creature-family/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_creature_family(self, creature_family_id: int):
        """Returns a creature family by ID.
        
        :param creature_family_id: The ID of the creature family.
        :type creature_family_id: int
        :return: Returns a creature family by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/creature-family/{creature_family_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_creature_types_index(self):
        """Returns an index of creature types.
        
        :return: Returns an index of creature types.
        :rtype: dict
        """
        endpoint = f"/data/wow/creature-type/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_creature_type(self, creature_type_id: int):
        """Returns a creature type by ID.
        
        :param creature_type_id: The ID of the creature type.
        :type creature_type_id: int
        :return: Returns a creature type by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/creature-type/{creature_type_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_creature(self, creature_id: int):
        """Returns a creature by ID.
        
        :param creature_id: The ID of the creature.
        :type creature_id: int
        :return: Returns a creature by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/creature/{creature_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_creature_search(self, search_params: Optional[dict] = None):
        """Performs a search of creatures. The fields below are provided for example. For more detail see the Search Guide.
        
        :param search_params: Search parameters
        :type search_params: dict
        :return: Performs a search of creatures. The fields below are provided for example. For more detail see the Search Guide.
        :rtype: dict
        """
        endpoint = f"/data/wow/search/creature"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint, params=search_params)

    async def get_creature_display_media(self, creature_display_id: int):
        """Returns media for a creature display by ID.
        
        :param creature_display_id: The ID of the creature display.
        :type creature_display_id: int
        :return: Returns media for a creature display by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/creature-display/{creature_display_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_creature_family_media(self, creature_family_id: int):
        """Returns media for a creature family by ID.
        
        :param creature_family_id: The ID of the creature family.
        :type creature_family_id: int
        :return: Returns media for a creature family by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/creature-family/{creature_family_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Guild Crest API

    async def get_guild_crest_components_index(self):
        """Returns an index of guild crest media.
        
        :return: Returns an index of guild crest media.
        :rtype: dict
        """
        endpoint = f"/data/wow/guild-crest/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_guild_crest_border_media(self, border_id: int):
        """Returns media for a guild crest border by ID.
        
        :param border_id: The ID of the guild crest border.
        :type border_id: int
        :return: Returns media for a guild crest border by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/guild-crest/border/{border_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_guild_crest_emblem_media(self, emblem_id: int):
        """Returns media for a guild crest emblem by ID.
        
        :param emblem_id: The ID of the guild crest emblem.
        :type emblem_id: int
        :return: Returns media for a guild crest emblem by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/guild-crest/emblem/{emblem_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Item API

    async def get_item_classes_index(self):
        """Returns an index of item classes.
        
        :return: Returns an index of item classes.
        :rtype: dict
        """
        endpoint = f"/data/wow/item-class/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_item_class(self, item_class_id: str):
        """Returns an item class by ID.
        
        :param item_class_id: The ID of the item class.
        :type item_class_id: str
        :return: Returns an item class by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/item-class/{item_class_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_item_sets_index(self):
        """Returns an index of item sets.
        
        :return: Returns an index of item sets.
        :rtype: dict
        """
        endpoint = f"/data/wow/item-set/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_item_set(self, item_set_id: int):
        """Returns an item set by ID.
        
        :param item_set_id: The ID of the item set.
        :type item_set_id: int
        :return: Returns an item set by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/item-set/{item_set_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_item_subclass(self, item_class_id: str, item_subclass_id: str):
        """Returns an item subclass by ID.
        
        :param item_class_id: The ID of the item class.
        :type item_class_id: str
        :param item_subclass_id: The ID of the item subclass.
        :type item_subclass_id: str
        :return: Returns an item subclass by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/item-class/{item_class_id}/item-subclass/{item_subclass_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_item(self, item_id: str):
        """Returns an item by ID.
        
        :param item_id: The ID of the item.
        :type item_id: str
        :return: Returns an item by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/item/{item_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_item_media(self, item_id: int):
        """Returns media for an item by ID.
        
        :param item_id: The ID of the item.
        :type item_id: int
        :return: Returns media for an item by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/item/{item_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_item_search(self, search_params: Optional[dict] = None):
        """Performs a search of items. The fields below are provided for example. For more detail see the Search Guide.
        
        :param search_params: Search parameters
        :type search_params: dict
        :return: Performs a search of items. The fields below are provided for example. For more detail see the Search Guide.
        :rtype: dict
        """
        endpoint = f"/data/wow/search/item"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint, params=search_params)

# endregion
# region Journal API

    async def get_journal_expansions_index(self):
        """Returns an index of journal expansions.
        
        :return: Returns an index of journal expansions.
        :rtype: dict
        """
        endpoint = f"/data/wow/journal-expansion/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_journal_expansion(self, journal_expansion_id: int):
        """Returns a journal expansion by ID.
        
        :param journal_expansion_id: The ID of the journal expansion.
        :type journal_expansion_id: int
        :return: Returns a journal expansion by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/journal-expansion/{journal_expansion_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_journal_encounters_index(self):
        """Returns an index of journal encounters.
        
        :return: Returns an index of journal encounters.
        :rtype: dict
        """
        endpoint = f"/data/wow/journal-encounter/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_journal_encounter(self, journal_encounter_id: int):
        """Returns a journal encounter by ID.
        
        :param journal_encounter_id: The ID of the journal encounter.
        :type journal_encounter_id: int
        :return: Returns a journal encounter by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/journal-encounter/{journal_encounter_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_journal_encounter_search(self, search_params: Optional[dict] = None):
        """Performs a search of journal encounters. The fields below are provided for example. For more detail see the Search Guide.
        
        :param search_params: Search parameters
        :type search_params: dict
        :return: Performs a search of journal encounters. The fields below are provided for example. For more detail see the Search Guide.
        :rtype: dict
        """
        endpoint = f"/data/wow/search/journal-encounter"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint, params=search_params)

    async def get_journal_instances_index(self):
        """Returns an index of journal instances.
        
        :return: Returns an index of journal instances.
        :rtype: dict
        """
        endpoint = f"/data/wow/journal-instance/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_journal_instance(self, journal_instance_id: int):
        """Returns a journal instance.
        
        :param journal_instance_id: The ID of the journal instance.
        :type journal_instance_id: int
        :return: Returns a journal instance.
        :rtype: dict
        """
        endpoint = f"/data/wow/journal-instance/{journal_instance_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_journal_instance_media(self, journal_instance_id: int):
        """Returns media for a journal instance by ID.
        
        :param journal_instance_id: The ID of the journal instance.
        :type journal_instance_id: int
        :return: Returns media for a journal instance by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/journal-instance/{journal_instance_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Media Search API

    async def get_media_search(self, tags: Optional[str] = None, orderby: Optional[str] = None, _page: Optional[int] = None):
        """Performs a search of all types of media documents. The fields below are provided for example. For more detail see the Search Guide.
        
        :param tags: The media document type as derived from the URL. For example, /wow/media/item/{id} will have tag 'item'. (example search field)
        :type tags: str
        :param orderby: The field to sort the result set by.
        :type orderby: str
        :param _page: The result page number.
        :type _page: int
        :return: Performs a search of all types of media documents. The fields below are provided for example. For more detail see the Search Guide.
        :rtype: dict
        """
        endpoint = f"/data/wow/search/media"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Modified Crafting API

    async def get_modified_crafting_index(self):
        """Returns the parent index for Modified Crafting.
        
        :return: Returns the parent index for Modified Crafting.
        :rtype: dict
        """
        endpoint = f"/data/wow/modified-crafting/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_modified_crafting_category_index(self):
        """Returns the index of Modified Crafting categories.
        
        :return: Returns the index of Modified Crafting categories.
        :rtype: dict
        """
        endpoint = f"/data/wow/modified-crafting/category/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_modified_crafting_category(self, category_id: int):
        """Returns a Modified Crafting category by ID.
        
        :param category_id: The ID of the Modified Crafting category.
        :type category_id: int
        :return: Returns a Modified Crafting category by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/modified-crafting/category/{category_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_modified_crafting_reagent_slot_type_index(self):
        """Returns the index of Modified Crafting reagent slot types.
        
        :return: Returns the index of Modified Crafting reagent slot types.
        :rtype: dict
        """
        endpoint = f"/data/wow/modified-crafting/reagent-slot-type/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_modified_crafting_reagent_slot_type(self, slot_type_id: int):
        """Returns a Modified Crafting reagent slot type by ID.
        
        :param slot_type_id: The ID of the Modified Crafting reagent slot type.
        :type slot_type_id: int
        :return: Returns a Modified Crafting reagent slot type by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/modified-crafting/reagent-slot-type/{slot_type_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Mount API

    async def get_mounts_index(self):
        """Returns an index of mounts.
        
        :return: Returns an index of mounts.
        :rtype: dict
        """
        endpoint = f"/data/wow/mount/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_mount(self, mount_id: int):
        """Returns a mount by ID.
        
        :param mount_id: The ID of the mount.
        :type mount_id: int
        :return: Returns a mount by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/mount/{mount_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_mount_search(self, search_params: Optional[dict] = None):
        """Performs a search of mounts. The fields below are provided for example. For more detail see the Search Guide.
        
        :param search_params: Search parameters
        :type search_params: dict
        :return: Performs a search of mounts. The fields below are provided for example. For more detail see the Search Guide.
        :rtype: dict
        """
        endpoint = f"/data/wow/search/mount"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint, params=search_params)

# endregion
# region Mythic Keystone Affix API

    async def get_mythic_keystone_affixes_index(self):
        """Returns an index of mythic keystone affixes.
        
        :return: Returns an index of mythic keystone affixes.
        :rtype: dict
        """
        endpoint = f"/data/wow/keystone-affix/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_mythic_keystone_affix(self, keystone_affix_id: int):
        """Returns a mythic keystone affix by ID.
        
        :param keystone_affix_id: The ID of the mythic keystone affix.
        :type keystone_affix_id: int
        :return: Returns a mythic keystone affix by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/keystone-affix/{keystone_affix_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_mythic_keystone_affix_media(self, keystone_affix_id: int):
        """Returns media for a mythic keystone affix by ID.
        
        :param keystone_affix_id: The ID of the mythic keystone affix.
        :type keystone_affix_id: int
        :return: Returns media for a mythic keystone affix by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/keystone-affix/{keystone_affix_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Mythic Keystone Dungeon API

    async def get_mythic_keystone_dungeons_index(self):
        """Returns an index of Mythic Keystone dungeons.
        
        :return: Returns an index of Mythic Keystone dungeons.
        :rtype: dict
        """
        endpoint = f"/data/wow/mythic-keystone/dungeon/index"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_mythic_keystone_dungeon(self, dungeon_id: int):
        """Returns a Mythic Keystone dungeon by ID.
        
        :param dungeon_id: The ID of the dungeon.
        :type dungeon_id: int
        :return: Returns a Mythic Keystone dungeon by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/mythic-keystone/dungeon/{dungeon_id}"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_mythic_keystone_index(self):
        """Returns an index of links to other documents related to Mythic Keystone dungeons.
        
        :return: Returns an index of links to other documents related to Mythic Keystone dungeons.
        :rtype: dict
        """
        endpoint = f"/data/wow/mythic-keystone/index"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_mythic_keystone_periods_index(self):
        """Returns an index of Mythic Keystone periods.
        
        :return: Returns an index of Mythic Keystone periods.
        :rtype: dict
        """
        endpoint = f"/data/wow/mythic-keystone/period/index"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_mythic_keystone_period(self, period_id: int):
        """Returns a Mythic Keystone period by ID.
        
        :param period_id: The ID of the Mythic Keystone season period.
        :type period_id: int
        :return: Returns a Mythic Keystone period by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/mythic-keystone/period/{period_id}"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_mythic_keystone_seasons_index(self):
        """Returns an index of Mythic Keystone seasons.
        
        :return: Returns an index of Mythic Keystone seasons.
        :rtype: dict
        """
        endpoint = f"/data/wow/mythic-keystone/season/index"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_mythic_keystone_season(self, season_id: int):
        """Returns a Mythic Keystone season by ID.
        
        :param season_id: The ID of the Mythic Keystone season.
        :type season_id: int
        :return: Returns a Mythic Keystone season by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/mythic-keystone/season/{season_id}"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Mythic Keystone Leaderboard API

    async def get_mythic_keystone_leaderboards_index(self, connected_realm_id: int):
        """Returns an index of Mythic Keystone Leaderboard dungeon instances for a connected realm.
        
        :param connected_realm_id: The ID of the connected realm.
        :type connected_realm_id: int
        :return: Returns an index of Mythic Keystone Leaderboard dungeon instances for a connected realm.
        :rtype: dict
        """
        endpoint = f"/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/index"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_mythic_keystone_leaderboard(self, connected_realm_id: int, dungeon_id: int, period: int):
        """Returns a weekly Mythic Keystone Leaderboard by period.
        
        :param connected_realm_id: The ID of the connected realm.
        :type connected_realm_id: int
        :param dungeon_id: The ID of the dungeon.
        :type dungeon_id: int
        :param period: The unique identifier for the leaderboard period.
        :type period: int
        :return: Returns a weekly Mythic Keystone Leaderboard by period.
        :rtype: dict
        """
        endpoint = f"/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/{dungeon_id}/period/{period}"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Mythic Raid Leaderboard API

    async def get_mythic_raid_leaderboard(self, raid: str, faction: str):
        """Returns the leaderboard for a given raid and faction.
        
        :param raid: The raid for a leaderboard.
        :type raid: str
        :param faction: Player faction (alliance or horde).
        :type faction: str
        :return: Returns the leaderboard for a given raid and faction.
        :rtype: dict
        """
        endpoint = f"/data/wow/leaderboard/hall-of-fame/{raid}/{faction}"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Pet API

    async def get_pets_index(self):
        """Returns an index of battle pets.
        
        :return: Returns an index of battle pets.
        :rtype: dict
        """
        endpoint = f"/data/wow/pet/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_pet(self, pet_id: int):
        """Returns a battle pets by ID.
        
        :param pet_id: The ID of the pet.
        :type pet_id: int
        :return: Returns a battle pets by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/pet/{pet_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_pet_media(self, pet_id: int):
        """Returns media for a battle pet by ID.
        
        :param pet_id: The ID of the pet.
        :type pet_id: int
        :return: Returns media for a battle pet by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/pet/{pet_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_pet_abilities_index(self):
        """Returns an index of pet abilities.
        
        :return: Returns an index of pet abilities.
        :rtype: dict
        """
        endpoint = f"/data/wow/pet-ability/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_pet_ability(self, pet_ability_id: int):
        """Returns a pet ability by ID.
        
        :param pet_ability_id: The ID of the pet ability.
        :type pet_ability_id: int
        :return: Returns a pet ability by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/pet-ability/{pet_ability_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_pet_ability_media(self, pet_ability_id: int):
        """Returns media for a pet ability by ID.
        
        :param pet_ability_id: The ID of the pet ability.
        :type pet_ability_id: int
        :return: Returns media for a pet ability by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/pet-ability/{pet_ability_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Playable Class API

    async def get_playable_classes_index(self):
        """Returns an index of playable classes.
        
        :return: Returns an index of playable classes.
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-class/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_playable_class(self, class_id: int):
        """Returns a playable class by ID.
        
        :param class_id: The ID of the playable class.
        :type class_id: int
        :return: Returns a playable class by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-class/{class_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_playable_class_media(self, playable_class_id: int):
        """Returns media for a playable class by ID.
        
        :param playable_class_id: The ID of the playable class.
        :type playable_class_id: int
        :return: Returns media for a playable class by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/playable-class/{playable_class_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_pvp_talent_slots(self, class_id: int):
        """Returns the PvP talent slots for a playable class by ID.
        
        :param class_id: The ID of the playable class.
        :type class_id: int
        :return: Returns the PvP talent slots for a playable class by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-class/{class_id}/pvp-talent-slots"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Playable Race API

    async def get_playable_races_index(self):
        """Returns an index of playable races.
        
        :return: Returns an index of playable races.
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-race/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_playable_race(self, playable_race_id: int):
        """Returns a playable race by ID.
        
        :param playable_race_id: The ID of the playable race.
        :type playable_race_id: int
        :return: Returns a playable race by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-race/{playable_race_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Playable Specialization API

    async def get_playable_specializations_index(self):
        """Returns an index of playable specializations.
        
        :return: Returns an index of playable specializations.
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-specialization/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_playable_specialization(self, spec_id: int):
        """Returns a playable specialization by ID.
        
        :param spec_id: The ID of the playable specialization.
        :type spec_id: int
        :return: Returns a playable specialization by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/playable-specialization/{spec_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_playable_specialization_media(self, spec_id: int):
        """Returns media for a playable specialization by ID.
        
        :param spec_id: The ID of the playable specialization.
        :type spec_id: int
        :return: Returns media for a playable specialization by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/playable-specialization/{spec_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Power Type API

    async def get_power_types_index(self):
        """Returns an index of power types.
        
        :return: Returns an index of power types.
        :rtype: dict
        """
        endpoint = f"/data/wow/power-type/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_power_type(self, power_type_id: int):
        """Returns a power type by ID.
        
        :param power_type_id: The ID of the power type.
        :type power_type_id: int
        :return: Returns a power type by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/power-type/{power_type_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Profession API

    async def get_professions_index(self):
        """Returns an index of professions.
        
        :return: Returns an index of professions.
        :rtype: dict
        """
        endpoint = f"/data/wow/profession/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_profession(self, profession_id: int):
        """Returns a profession by ID.
        
        :param profession_id: The ID of the profession.
        :type profession_id: int
        :return: Returns a profession by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/profession/{profession_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_profession_media(self, profession_id: int):
        """Returns media for a profession by ID.
        
        :param profession_id: The ID of the profession.
        :type profession_id: int
        :return: Returns media for a profession by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/profession/{profession_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_profession_skill_tier(self, profession_id: int, skill_tier_id: int):
        """Returns a skill tier for a profession by ID.
        
        :param profession_id: The ID of the profession.
        :type profession_id: int
        :param skill_tier_id: The ID of the skill tier.
        :type skill_tier_id: int
        :return: Returns a skill tier for a profession by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/profession/{profession_id}/skill-tier/{skill_tier_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_recipe(self, recipe_id: int):
        """Returns a recipe by ID.
        
        :param recipe_id: The ID of the recipe.
        :type recipe_id: int
        :return: Returns a recipe by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/recipe/{recipe_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_recipe_media(self, recipe_id: int):
        """Returns media for a recipe by ID.
        
        :param recipe_id: The ID of the recipe.
        :type recipe_id: int
        :return: Returns media for a recipe by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/recipe/{recipe_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region PvP Season API

    async def get_pvp_seasons_index(self):
        """Returns an index of PvP seasons.
        
        :return: Returns an index of PvP seasons.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-season/index"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_pvp_season(self, pvp_season_id: int):
        """Returns a PvP season by ID.
        
        :param pvp_season_id: The ID of the PvP season.
        :type pvp_season_id: int
        :return: Returns a PvP season by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-season/{pvp_season_id}"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_pvp_leaderboards_index(self, pvp_season_id: int):
        """Returns an index of PvP leaderboards for a PvP season.
        
        :param pvp_season_id: The ID of the PvP season.
        :type pvp_season_id: int
        :return: Returns an index of PvP leaderboards for a PvP season.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/index"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_pvp_leaderboard(self, pvp_season_id: int, pvp_bracket: str):
        """Returns the PvP leaderboard of a specific PvP bracket for a PvP season.
        
        :param pvp_season_id: The ID of the PvP season.
        :type pvp_season_id: int
        :param pvp_bracket: The PvP bracket type.
        :type pvp_bracket: str
        :return: Returns the PvP leaderboard of a specific PvP bracket for a PvP season.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/{pvp_bracket}"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_pvp_rewards_index(self, pvp_season_id: int):
        """Returns an index of PvP rewards for a PvP season.
        
        :param pvp_season_id: The ID of the PvP season.
        :type pvp_season_id: int
        :return: Returns an index of PvP rewards for a PvP season.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-season/{pvp_season_id}/pvp-reward/index"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region PvP Tier API

    async def get_pvp_tier_media(self, pvp_tier_id: int):
        """Returns media for a PvP tier by ID.
        
        :param pvp_tier_id: The ID of the PvP tier.
        :type pvp_tier_id: int
        :return: Returns media for a PvP tier by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/pvp-tier/{pvp_tier_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_pvp_tiers_index(self):
        """Returns an index of PvP tiers.
        
        :return: Returns an index of PvP tiers.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-tier/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_pvp_tier(self, pvp_tier_id: int):
        """Returns a PvP tier by ID.
        
        :param pvp_tier_id: The ID of the PvP tier.
        :type pvp_tier_id: int
        :return: Returns a PvP tier by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-tier/{pvp_tier_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Quest API

    async def get_quests_index(self):
        """Returns the parent index for quests.
        
        :return: Returns the parent index for quests.
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_quest(self, quest_id: int):
        """Returns a quest by ID.
        
        :param quest_id: The ID of the quest.
        :type quest_id: int
        :return: Returns a quest by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/{quest_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_quest_categories_index(self):
        """Returns an index of quest categories (such as quests for a specific class, profession, or storyline).
        
        :return: Returns an index of quest categories (such as quests for a specific class, profession, or storyline).
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/category/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_quest_category(self, quest_category_id: str):
        """Returns a quest category by ID.
        
        :param quest_category_id: The ID of the quest category.
        :type quest_category_id: str
        :return: Returns a quest category by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/category/{quest_category_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_quest_areas_index(self):
        """Returns an index of quest areas.
        
        :return: Returns an index of quest areas.
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/area/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_quest_area(self, quest_area_id: str):
        """Returns a quest area by ID.
        
        :param quest_area_id: The ID of the quest area.
        :type quest_area_id: str
        :return: Returns a quest area by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/area/{quest_area_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_quest_types_index(self):
        """Returns an index of quest types (such as PvP quests, raid quests, or account quests).
        
        :return: Returns an index of quest types (such as PvP quests, raid quests, or account quests).
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/type/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_quest_type(self, quest_type_id: str):
        """Returns a quest type by ID.
        
        :param quest_type_id: The ID of the quest type.
        :type quest_type_id: str
        :return: Returns a quest type by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/quest/type/{quest_type_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Realm API

    async def get_realms_index(self):
        """Returns an index of realms.
        
        :return: Returns an index of realms.
        :rtype: dict
        """
        endpoint = f"/data/wow/realm/index"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_realm(self, realm_slug: str):
        """Returns a single realm by slug or ID.
        
        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :return: Returns a single realm by slug or ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/realm/{realm_slug}"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_realm_search(self, timezone: Optional[str] = None, orderby: Optional[str] = None, _page: Optional[int] = None):
        """Performs a search of realms. The fields below are provided for example. For more detail see the Search Guide.
        
        :param timezone: The timezone of the realm. (example search field)
        :type timezone: str
        :param orderby: The field to sort the result set by.
        :type orderby: str
        :param _page: The result page number.
        :type _page: int
        :return: Performs a search of realms. The fields below are provided for example. For more detail see the Search Guide.
        :rtype: dict
        """
        endpoint = f"/data/wow/search/realm"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Region API

    async def get_regions_index(self):
        """Returns an index of regions.
        
        :return: Returns an index of regions.
        :rtype: dict
        """
        endpoint = f"/data/wow/region/index"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_region(self, region_id: int):
        """Returns a region by ID.
        
        :param region_id: The ID of the region.
        :type region_id: int
        :return: Returns a region by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/region/{region_id}"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Reputations API

    async def get_reputation_factions_index(self):
        """Returns an index of reputation factions.
        
        :return: Returns an index of reputation factions.
        :rtype: dict
        """
        endpoint = f"/data/wow/reputation-faction/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_reputation_faction(self, reputation_faction_id: int):
        """Returns a single reputation faction by ID.
        
        :param reputation_faction_id: The ID of the reputation faction.
        :type reputation_faction_id: int
        :return: Returns a single reputation faction by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/reputation-faction/{reputation_faction_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_reputation_tiers_index(self):
        """Returns an index of reputation tiers.
        
        :return: Returns an index of reputation tiers.
        :rtype: dict
        """
        endpoint = f"/data/wow/reputation-tiers/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_reputation_tiers(self, reputation_tiers_id: int):
        """Returns a single set of reputation tiers by ID.
        
        :param reputation_tiers_id: The ID of the set of reputation tiers.
        :type reputation_tiers_id: int
        :return: Returns a single set of reputation tiers by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/reputation-tiers/{reputation_tiers_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Spell API

    async def get_spell(self, spell_id: int):
        """Returns a spell by ID.
        
        :param spell_id: The ID of the spell.
        :type spell_id: int
        :return: Returns a spell by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/spell/{spell_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_spell_media(self, spell_id: int):
        """Returns media for a spell by ID.
        
        :param spell_id: The ID of the spell.
        :type spell_id: int
        :return: Returns media for a spell by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/spell/{spell_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_spell_search(self, search_params: Optional[dict] = None):
        """Performs a search of spells. The fields below are provided for example. For more detail see the Search Guide.
        
        :param search_params: Search parameters
        :type search_params: dict
        :return: Performs a search of spells. The fields below are provided for example. For more detail see the Search Guide.
        :rtype: dict
        """
        endpoint = f"/data/wow/search/spell"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint, params=search_params)

# endregion
# region Talent API

    async def get_talents_index(self):
        """Returns an index of talents.
        
        :return: Returns an index of talents.
        :rtype: dict
        """
        endpoint = f"/data/wow/talent/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_talent(self, talent_id: int):
        """Returns a talent by ID.
        
        :param talent_id: The ID of the talent.
        :type talent_id: int
        :return: Returns a talent by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/talent/{talent_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_pvp_talents_index(self):
        """Returns an index of PvP talents.
        
        :return: Returns an index of PvP talents.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-talent/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_pvp_talent(self, pvp_talent_id: int):
        """Returns a PvP talent by ID.
        
        :param pvp_talent_id: The ID of the PvP talent.
        :type pvp_talent_id: int
        :return: Returns a PvP talent by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/pvp-talent/{pvp_talent_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Tech Talent API

    async def get_tech_talent_tree_index(self):
        """Returns an index of tech talent trees.
        
        :return: Returns an index of tech talent trees.
        :rtype: dict
        """
        endpoint = f"/data/wow/tech-talent-tree/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_tech_talent_tree(self, tech_talent_tree_id: int):
        """Returns a tech talent tree by ID.
        
        :param tech_talent_tree_id: The ID of the tech talent tree.
        :type tech_talent_tree_id: int
        :return: Returns a tech talent tree by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/tech-talent-tree/{tech_talent_tree_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_tech_talent_index(self):
        """Returns an index of tech talents.
        
        :return: Returns an index of tech talents.
        :rtype: dict
        """
        endpoint = f"/data/wow/tech-talent/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_tech_talent(self, tech_talent_id: int):
        """Returns a tech talent by ID.
        
        :param tech_talent_id: The ID of the tech talent.
        :type tech_talent_id: int
        :return: Returns a tech talent by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/tech-talent/{tech_talent_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_tech_talent_media(self, tech_talent_id: int):
        """Returns media for a tech talent by ID.
        
        :param tech_talent_id: The ID of the tech talent.
        :type tech_talent_id: int
        :return: Returns media for a tech talent by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/media/tech-talent/{tech_talent_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region Title API

    async def get_titles_index(self):
        """Returns an index of titles.
        
        :return: Returns an index of titles.
        :rtype: dict
        """
        endpoint = f"/data/wow/title/index"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_title(self, title_id: int):
        """Returns a title by ID.
        
        :param title_id: The ID of the title.
        :type title_id: int
        :return: Returns a title by ID.
        :rtype: dict
        """
        endpoint = f"/data/wow/title/{title_id}"
        namespace = "static-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
# region WoW Token API

    async def get_wow_token_index(self):
        """Returns the WoW Token index.
        
        :return: Returns the WoW Token index.
        :rtype: dict
        """
        endpoint = f"/data/wow/token/index"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

    async def get_wow_token_index_cn(self):
        """Returns the WoW Token index.
        
        :return: Returns the WoW Token index.
        :rtype: dict
        """
        endpoint = f"/data/wow/token/index"
        namespace = "dynamic-{region}"

        return await self.get_game_api_resource(namespace, endpoint)

# endregion
