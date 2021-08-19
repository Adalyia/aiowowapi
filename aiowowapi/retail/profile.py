from typing import Union

class Profile():
    """This class contains all API endpoints for the Profile category of the Retail World of Warcraft API

    :param api: An instance of our generic API object
    :type api: API
    """
    def __init__(self, api):    
        """Constructor method
        """
        self.api = api
        
    async def getProfileApiResource(self, namespace:str, endpoint:str, params:dict=None) -> Union[dict, None]:
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
    
    #region Character Achievements API
    
    async def getCharAchievementsSummary(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a summary of the achievements a character has completed.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/achievements"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    async def getCharAchievementStatistics(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a character's statistics as they pertain to achievements.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/achievements/statistics"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion

    #region Character Appearance API
    
    async def getCharAppearanceSummary(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a summary of a character's appearance settings.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/appearance"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character Collections API
    
    async def getCharCollectionsIndex(self, character:str, realm:str) -> Union[dict, None]:
        """Returns an index of collection types for a character.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/collections"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    async def getCharMountsCollectionSummary(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a summary of the mounts a character has obtained.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/collections/mounts"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    async def getCharPetsCollectionSummary(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a summary of the battle pets a character has obtained.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/collections/pets"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character Encounters API
    
    async def getCharEncountersSummary(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a summary of a character's encounters.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/encounters"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    async def getCharDungeons(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a summary of a character's completed dungeons.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/encounters/dungeons"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    async def getCharRaids(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a summary of a character's completed raids.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/encounters/raids"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character Equipment API
    
    async def getCharEquipmentSummary(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a summary of the items equipped by a character.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/equipment"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character Hunter Pets API
    
    async def getCharHunterPetsSummary(self, character:str, realm:str) -> Union[dict, None]:
        """If the character is a hunter, returns a summary of the character's hunter pets. Otherwise, returns an HTTP 404 Not Found error.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/hunter-pets"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character Media API
    
    async def getCharMediaSummary(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a summary of the media assets available for a character (such as an avatar render).

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/character-media"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character Mythic Keystone Profile API
    
    async def getCharMythicKeystoneProfileIndex(self, character:str, realm:str) -> Union[dict, None]:
        """Returns the Mythic Keystone profile index for a character.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/mythic-keystone-profile"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    async def getCharMythicKeystoneSeasonDetails(self, character:str, realm:str, season_id:str) -> Union[dict, None]:
        """Returns the Mythic Keystone season details for a character.
        
        Returns a 404 Not Found for characters that have not yet completed a Mythic Keystone dungeon for the specified season.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :param season_id: The ID of the Mythic Keystone season.
        :type season_id: int
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/mythic-keystone-profile/season/{season_id}"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character Professions API
    
    async def getCharProfessionsSummary(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a summary of professions for a character.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/professions"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character Profile API
    
    async def getCharProfileSummary(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a profile summary for a character.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    async def getCharProfileStatus(self, character:str, realm:str) -> Union[dict, None]:
        """Returns the status and a unique ID for a character. A client should delete information about a character from their application if any of the following conditions occur:
        
        * an HTTP 404 Not Found error is returned
        * the is_valid value is false
        * the returned character ID doesn't match the previously recorded value for the character
        
        The following example illustrates how to use this endpoint:
        
        * A client requests and stores information about a character, including its unique character ID and the timestamp of the request.
        * After 30 days, the client makes a request to the status endpoint to verify if the character information is still valid.
        * If character cannot be found, is not valid, or the characters IDs do not match, the client removes the information from their application.
        * If the character is valid and the character IDs match, the client retains the data for another 30 days.
        
        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/status"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character PvP API
    
    async def getCharPvPBracketStatistics(self, character:str, realm:str, pvp_bracket:str) -> Union[dict, None]:
        """Returns the PvP bracket statistics for a character.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :param pvp_bracket: The PvP bracket type. (ex: 3v3, 2v2)
        :type pvp_bracket: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/pvp-bracket/{pvp_bracket}"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    async def getCharPvPSummary(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a PvP summary for a character.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/pvp-summary"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character Quests API
    
    async def getCharQuests(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a character's active quests as well as a link to the character's completed quests.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/quests"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    async def getCharCompletedQuests(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a list of quests that a character has completed.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/quests/completed"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character Reputations API
    
    async def getCharReputationsSummary(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a summary of a character's reputations.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/reputations"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character Soulbinds API
    
    async def getCharSoulbinds(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a character's soulbinds.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/soulbinds"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character Specializations API
    
    async def getCharSpecializationsSummary(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a summary of a character's specializations.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/specializations"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character Statistics API
    
    async def getCharStatisticsSummary(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a statistics summary for a character.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/statistics"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Character Titles API
    
    async def getCharTitlesSummary(self, character:str, realm:str) -> Union[dict, None]:
        """Returns a summary of titles a character has obtained.

        :param character: The lowercase name of the character.
        :type character: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/profile/wow/character/{str(realm).lower()}/{str(character).lower()}/titles"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    #region Guild API
    
    async def getGuild(self, guild:str, realm:str) -> Union[dict, None]:
        """Returns a single guild by its name and realm.

        :param guild: The slug of the guild.
        :type guild: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/guild/{str(realm).lower()}/{str(guild).lower()}"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    async def getGuildActivity(self, guild:str, realm:str) -> Union[dict, None]:
        """Returns a single guild's activity by name and realm.

        :param guild: The slug of the guild.
        :type guild: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/guild/{str(realm).lower()}/{str(guild).lower()}/activity"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    async def getGuildAchievements(self, guild:str, realm:str) -> Union[dict, None]:
        """Returns a single guild's achievements by name and realm.

        :param guild: The slug of the guild.
        :type guild: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/guild/{str(realm).lower()}/{str(guild).lower()}/achievements"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    async def getGuildRoster(self, guild:str, realm:str) -> Union[dict, None]:
        """Returns a single guild's roster by its name and realm.

        :param guild: The slug of the guild.
        :type guild: str
        :param realm: The slug of the realm.
        :type realm: str
        :return: The API response in JSON format/a dict object
        :rtype: dict
        """
        endpoint = f"/data/wow/guild/{str(realm).lower()}/{str(guild).lower()}/roster"
        
        namespace = 'profile-{region}'

        return await self.getProfileApiResource(namespace, endpoint)
    
    #endregion
    
    