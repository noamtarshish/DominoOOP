from NaivePlayer import *
from RandomPlayer import *
from MaxScorePlayer import*
from Player import Player

class Team:
    def __init__(self, name, players):
        """
        Function that define the init for the class Team
        :param name: name of the team
        :param players: list of the players of the team
        """
        self.name = name
        self.__players = players

    def get_team(self):
        """
        Function that returns the list of the team players
        :return: list of the team players
        """
        return self.__players

    def score_team(self):
        """
        Method that calculate the score of the team by the domino tilts in the hand of the players
        :return: int represent the score of the team
        """
        score_team = 0
        for player in self.__players:
            score_team += Player.score(player)

        return score_team

    def has_dominoes_team(self):
        """
        Function that check if there is domino tilts in the hand of the team
        :return: True if there is domino tilts in the team and False if not.
        """
        if not self.__players == []:
            return True
        else:
            return False

    def play(self, board):
        """
        Function that check the play strategy for the team. every player try to add domino tilt to the board in his
        line. if the players succeed to add domino tilt the board update and the domino tilt removed from the hand
        of the player.
        :param board: board for the game
        :return: bool, True if the team succeed to add domino to the board and False if not.
        """
        for i in self.get_team():
            if i.play(board) is True:
                return True
        else:
            return False

    def __str__(self):
        """
        Function that return string that represent the team
        :return: string that represent the team
        """

        team_str = "Name " + str(self.name) + ", Score team: " + str(self.score_team()) + ", Players:"
        players_str = ''

        for i in range(len(self.__players)):
            players_str = players_str + " "+ Player.__str__(self.__players[i])

        team_str += players_str

        return team_str



    def __repr__(self):
        """
        Function that return string that represent the team
        :return: string that represent the team
        """
        team_str = "Name " + str(self.name) + ", Score team: " + str(self.score_team()) + ", Players:"
        players_str = ''

        for i in range(len(self.__players)):
            players_str = players_str + " " + Player.__str__(self.__players[i])

        team_str += players_str

        return team_str







