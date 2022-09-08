from .game_data_classic import GameData


class ClassicApi:
    """This class just helps structure our wrapper, creates accessible API endpoint accessors for classic World of Warcraft

    :param api: An instance of our generic API object
    :type api: API
    """

    def __init__(self, api):
        """Constructor method
        """
        self.GameData = GameData(api)
