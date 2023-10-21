from Player import Player
import copy


class MaxScorePlayer(Player):
    def __init__(self, name, age, hand):
        """
        Function that define the init for the class Player
        :param name: name of the player
        :param age: age of the player
        :param hand: the hand of the player
        """
        super().__init__(name, age, hand)
        self.name = name
        self.age = age
        self.hand = hand

    def score(self):
        """
        Method that calculate the score of the player by the domino tilts in the hand of the player
        :return: int represent the score of the player
        """
        return Player.score(self)

    def has_dominoes(self):
        """
        Function that check if there is domino tilts in the hand of the player
        :return: True if there is domino tilts in the player and False if not.
        """
        return Player.has_dominoes(self)

    def play(self, board):
        """
        Function that turn on the game strategy for the MaxScorePlayer. The MaxScorePlayer add the first domino tilt that
        he can to the board. First, he try to add the domino tilt from the right side of the board and if he fail he
        try to add the domino tilt to the left side of the board. If he succeed the board will update and the domino
        tilt will remove from the hand of the MaxScorePlayer.
        """
        copied_max_hand = copy.deepcopy(self.hand.get_collection())
        copied_max_hand.sort()
        copied_max_hand.reverse()

        for i in range(len(copied_max_hand)):
            if board.add_right(copied_max_hand[i]) is True:
                self.hand.remove_domino(copied_max_hand[i])
                return True

            if board.add_left(copied_max_hand[i]) is True:
                self.hand.remove_domino(copied_max_hand[i])
                return True

        return False


    def __str__(self):
        """
        Function that return string that represent the player
        :return: string that represent the player
        """
        return Player.__str__(self)

    def __repr__(self):
        """
        Function that return string that represent the player
        :return: string that represent the player
        """
        return Player.__repr__(self)
