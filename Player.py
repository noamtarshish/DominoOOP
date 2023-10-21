from Domino import Domino


class Player:

    def __init__(self, name, age, hand):
        """
        Function that define the init for the class Player
        :param name: name of the player
        :param age: age of the player
        :param hand: the hand of the player
        """
        self.name = name
        self.age = age
        self.hand = hand

    def score(self):
        """
        Method that calculate the score of the player by the domino tilts in the hand of the player
        :return: int represent the score of the player
        """
        score = 0
        if len(self.hand) == 0:
            return 0
        else:
            for domino in self.hand.get_collection():
                score += Domino.get_left(domino) + Domino.get_right(domino)
            return score

    def has_dominoes(self):
        """
        Function that check if there is domino tilts in the hand of the player
        :return: True if there is domino tilts in the player and False if not.
        """
        if len(self.hand) != 0:
            return True
        else:
            return False

    def play(self, board):
        """
        Function that turn on the game strategy
        :param board: the board for the game
        :return: nothing
        """
        pass

    def __str__(self):
        """
        Function that return string that represent the player
        :return: string that represent the player
        """
        return "Name: " + str(self.name) + ", Age: " + str(self.age) + ", Hand: " + str(self.hand) + ", Score: " + str(self.score())

    def __repr__(self):
        """
        Function that return string that represent the player
        :return: string that represent the player
        """
        return "Name: " + str(self.name) + ", Age: " + str(self.age) + ", Hand: " + str(self.hand) + ", Score: " + str(self.score())






