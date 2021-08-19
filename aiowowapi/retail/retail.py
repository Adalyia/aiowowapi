from .game_data import GameData
from .profile import Profile


class RetailApi():
    """This class just helps structure our wrapper, creates accessible API endpoint accessors for retail World of Warcraft

    :param api: An instance of our generic API object
    :type api: API
    """
    def __init__(self, api):
        """Constructor method
        """
        self.GameData = GameData(api)
        self.Profile = Profile(api)