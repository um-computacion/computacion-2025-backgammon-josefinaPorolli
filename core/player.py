class Player:
    # CONSTRUCTOR
    # The constructor in every class sets the initial state of the object and its attributes
    def __init__(self, name:str, colour:str):
        self.__name__ = name # Each player will introduce themselves with their names before playing
        self.__colour__ = colour # The game will assign a colour to each player

    # SETTERS

    # This function receives the player's name before starting the game.
    # The purpose of this function is to set the player's name.
    # The function does not return any values, since it is a setter
    def set_name(self, name:str):
        self.__name__ = name

    # At the beginning of the game, the colours of each player are set.
    # The purpose of this function is to set the player's colour.
    # The function does not return any values, since it is a setter
    def set_colour(self, colour:str):
        self.__colour__ = colour

    # GETTERS

    # This function does not receive any parameters, for it is just a getter.
    # The purpose of this function is to get the player's name during the game for messages like: "Juan Carlos, it's your turn" or "Pepita wins!"
    # This function returns a string, which corresponds to the player's name, which was introduced before playing.
    def get_name(self) -> str:
        return self.__name__
    
    # This function does not receive any parameters, for it is just a getter.
    # The purpose of this function is to get the player's colour during the game for messages like: "Ricky Martin, your colour is BLACK"
    # This function returns a string, which corresponds to the player's colour, which was introduced before playing.
    def get_colour(self) -> str:
        return self.__colour__