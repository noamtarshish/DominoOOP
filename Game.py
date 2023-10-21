from Board import Board
from Team import Team

class Game:
    def __init__(self, board, team1, team2):
        """
        Function that define the init for the class game
        :param board: board for the game
        :param team1: team of players
        :param team2: another team of players
        """
        self.board = board
        self.team1 = team1
        self.team2 = team2

    def play(self):
        """
        Method that generate the game. The first team to play will be team1 and after it team2. every team try to add
        domino tilt to the board in it line. The game will finish if there are no domino tilts for one of the groups.
        the board and the hand of the players update during the game.
        :return: string that define which team won the game. the winning team is the team that it score is lowest of
        the teams.
        """
        while len(self.board) != self.board.max_capacity or self.team1.has_dominoes_team() == False or self.team2.has_dominoes_team() == False:
            if self.team1.play(self.board) is False:
                break
            if self.team2.play(self.board) is False:
                break

        score_team1 = Team.score_team(self.team1)
        score_team2 = Team.score_team(self.team2)

        if score_team2 > score_team1:
            return "Team " + str(self.team1.name) + " wins Team " + str(self.team2.name)

        if score_team2 < score_team1:
            return "Team " + str(self.team2.name) + " wins Team " + str(self.team1.name)

        if score_team2 == score_team1:
            return "Draw!"


