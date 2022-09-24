from typing import Optional


class Profile:
    def __init__(self, api):
        """This class contains all API endpoints for the Profile category of the Retail World of Warcraft API

        :param api: An instance of our generic API object
        :type api: API
        """
        self.api = api

    async def get_profile_api_resource(self, namespace: str, endpoint: str, params: dict = None) -> Optional[dict]:
        """Generic method for retrieving data from a Profile API endpoint

        :param namespace: The namespace of the resource we're trying to access
        :type namespace: str
        :param endpoint: The API endpoint of the resource we're trying to access
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
        params["access_token"] = token

        return await self.api.get_resource(hostname, endpoint, params)

    # region Character Achievements API

    async def get_character_achievements_summary(self, realm_slug: str, character_name: str):
        """Returns a summary of the achievements a character has completed.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a summary of the achievements a character has completed.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/achievements"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    async def get_character_achievement_statistics(self, realm_slug: str, character_name: str):
        """Returns a character's statistics as they pertain to achievements.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a character's statistics as they pertain to achievements.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/achievements/statistics"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Appearance API

    async def get_character_appearance_summary(self, realm_slug: str, character_name: str):
        """Returns a summary of a character's appearance settings.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a summary of a character's appearance settings.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/appearance"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Collections API

    async def get_character_collections_index(self, realm_slug: str, character_name: str):
        """Returns an index of collection types for a character.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns an index of collection types for a character.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/collections"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    async def get_character_mounts_collection_summary(self, realm_slug: str, character_name: str):
        """Returns a summary of the mounts a character has obtained.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a summary of the mounts a character has obtained.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/collections/mounts"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    async def get_character_pets_collection_summary(self, realm_slug: str, character_name: str):
        """Returns a summary of the battle pets a character has obtained.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a summary of the battle pets a character has obtained.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/collections/pets"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Encounters API

    async def get_character_encounters_summary(self, realm_slug: str, character_name: str):
        """Returns a summary of a character's encounters.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a summary of a character's encounters.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/encounters"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    async def get_character_dungeons(self, realm_slug: str, character_name: str):
        """Returns a summary of a character's completed dungeons.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a summary of a character's completed dungeons.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/encounters/dungeons"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    async def get_character_raids(self, realm_slug: str, character_name: str):
        """Returns a summary of a character's completed raids.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a summary of a character's completed raids.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/encounters/raids"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Equipment API

    async def get_character_equipment_summary(self, realm_slug: str, character_name: str):
        """Returns a summary of the items equipped by a character.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a summary of the items equipped by a character.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/equipment"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Hunter Pets API

    async def get_character_hunter_pets_summary(self, realm_slug: str, character_name: str):
        """If the character is a hunter, returns a summary of the character's hunter pets. Otherwise, returns an HTTP 404 Not Found error.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: If the character is a hunter, returns a summary of the character's hunter pets. Otherwise, returns an HTTP 404 Not Found error.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/hunter-pets"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Media API

    async def get_character_media_summary(self, realm_slug: str, character_name: str):
        """Returns a summary of the media assets available for a character (such as an avatar render).

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a summary of the media assets available for a character (such as an avatar render).
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/character-media"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Mythic Keystone Profile API

    async def get_character_mythic_keystone_profile_index(self, realm_slug: str, character_name: str):
        """Returns the Mythic Keystone profile index for a character.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns the Mythic Keystone profile index for a character.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/mythic-keystone-profile"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    async def get_character_mythic_keystone_season_details(self, realm_slug: str, character_name: str, season_id: str):
        """Returns the Mythic Keystone season details for a character.

Returns a 404 Not Found for characters that have not yet completed a Mythic Keystone dungeon for the specified season.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :param season_id: The ID of the Mythic Keystone season.
        :type season_id: str
        :return: Returns the Mythic Keystone season details for a character.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/mythic-keystone-profile/season/{season_id}"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Professions API

    async def get_character_professions_summary(self, realm_slug: str, character_name: str):
        """Returns a summary of professions for a character.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a summary of professions for a character.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/professions"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Profile API

    async def get_character_profile_summary(self, realm_slug: str, character_name: str):
        """Returns a profile summary for a character.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a profile summary for a character.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    async def get_character_profile_status(self, realm_slug: str, character_name: str):
        """Returns the status and a unique ID for a character. A client should delete information about a character from their application if any of the following conditions occur:
an HTTP 404 Not Found error is returned
the is_valid value is false
the returned character ID doesn't match the previously recorded value for the character
The following example illustrates how to use this endpoint:
A client requests and stores information about a character, including its unique character ID and the timestamp of the request.
After 30 days, the client makes a request to the status endpoint to verify if the character information is still valid.
If character cannot be found, is not valid, or the characters IDs do not match, the client removes the information from their application.
If the character is valid and the character IDs match, the client retains the data for another 30 days.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns the status and a unique ID for a character. A client should delete information about a character from their application if any of the following conditions occur:
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/status"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character PvP API

    async def get_character_pvp_bracket_statistics(self, realm_slug: str, character_name: str, pvp_bracket: str):
        """Returns the PvP bracket statistics for a character.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :param pvp_bracket: The PvP bracket type.
        :type pvp_bracket: str
        :return: Returns the PvP bracket statistics for a character.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/pvp-bracket/{pvp_bracket}"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    async def get_character_pvp_summary(self, realm_slug: str, character_name: str):
        """Returns a PvP summary for a character.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a PvP summary for a character.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/pvp-summary"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Quests API

    async def get_character_quests(self, realm_slug: str, character_name: str):
        """Returns a character's active quests as well as a link to the character's completed quests.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a character's active quests as well as a link to the character's completed quests.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/quests"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    async def get_character_completed_quests(self, realm_slug: str, character_name: str):
        """Returns a list of quests that a character has completed.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a list of quests that a character has completed.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/quests/completed"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Reputations API

    async def get_character_reputations_summary(self, realm_slug: str, character_name: str):
        """Returns a summary of a character's reputations.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a summary of a character's reputations.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/reputations"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Soulbinds API

    async def get_character_soulbinds(self, realm_slug: str, character_name: str):
        """Returns a character's soulbinds.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a character's soulbinds.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/soulbinds"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Specializations API

    async def get_character_specializations_summary(self, realm_slug: str, character_name: str):
        """Returns a summary of a character's specializations.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a summary of a character's specializations.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/specializations"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Statistics API

    async def get_character_statistics_summary(self, realm_slug: str, character_name: str):
        """Returns a statistics summary for a character.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a statistics summary for a character.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/statistics"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Character Titles API

    async def get_character_titles_summary(self, realm_slug: str, character_name: str):
        """Returns a summary of titles a character has obtained.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param character_name: The lowercase name of the character.
        :type character_name: str
        :return: Returns a summary of titles a character has obtained.
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{realm_slug}/{character_name}/titles"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
    # region Guild API

    async def get_guild(self, realm_slug: str, name_slug: str):
        """Returns a single guild by its name and realm.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param name_slug: The slug of the guild.
        :type name_slug: str
        :return: Returns a single guild by its name and realm.
        :rtype: dict
        """
        endpoint = f"/data/wow/guild/{realm_slug}/{name_slug}"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    async def get_guild_activity(self, realm_slug: str, name_slug: str):
        """Returns a single guild's activity by name and realm.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param name_slug: The slug of the guild.
        :type name_slug: str
        :return: Returns a single guild's activity by name and realm.
        :rtype: dict
        """
        endpoint = f"/data/wow/guild/{realm_slug}/{name_slug}/activity"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    async def get_guild_achievements(self, realm_slug: str, name_slug: str):
        """Returns a single guild's achievements by name and realm.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param name_slug: The slug of the guild.
        :type name_slug: str
        :return: Returns a single guild's achievements by name and realm.
        :rtype: dict
        """
        endpoint = f"/data/wow/guild/{realm_slug}/{name_slug}/achievements"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    async def get_guild_roster(self, realm_slug: str, name_slug: str):
        """Returns a single guild's roster by its name and realm.

        :param realm_slug: The slug of the realm.
        :type realm_slug: str
        :param name_slug: The slug of the guild.
        :type name_slug: str
        :return: Returns a single guild's roster by its name and realm.
        :rtype: dict
        """
        endpoint = f"/data/wow/guild/{realm_slug}/{name_slug}/roster"
        namespace = "profile-{region}"

        return await self.get_profile_api_resource(namespace, endpoint)

    # endregion
