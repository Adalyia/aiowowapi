from .game_data_classic import GameData


class ClassicApi:
    def __init__(self, api):
        """This class adds structure to our wrapper, creating accessible API endpoint methods for classic World of Warcraft
        :param api: An instance of our generic API object
        :type api: API
        """
        self.GameData = GameData(api)
