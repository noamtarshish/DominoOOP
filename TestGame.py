from unittest import TestCase
from unittest import TestCase
from Board import Board
from Domino import Domino
from Hand import Hand
from NaivePlayer import NaivePlayer
from Team import Team
from Game import Game
from RandomPlayer import RandomPlayer



class TestGame(TestCase):
    def test_play(self):
        d1 = Domino(2, 2)
        d2 = Domino(3, 3)
        d3 = Domino(4, 5)
        d4 = Domino(5, 4)
        player_hand1 = Hand([d1, d2])
        player_hand2 = Hand([d1, d3, d4])

        p1 = NaivePlayer('Itay', 31, player_hand1)
        p2 = RandomPlayer('Ohad', 37, player_hand2)
        team1 = Team('Hawks', [p1])
        team2 = Team('Spurs', [p2])
        board1 = Board(10)

        g = Game(board1, team1, team2)

        self.assertEqual(10, team1.score_team())
        self.assertTrue(team1.has_dominoes_team())
        self.assertEqual(22, team2.score_team())
        self.assertTrue(team2.has_dominoes_team())
        self.assertEqual(g.play(), "Team Hawks wins Team Spurs")

        d1 = Domino(2, 2)
        d2 = Domino(3, 3)
        d3 = Domino(4, 5)
        d4 = Domino(5, 4)
        player_hand1 = Hand([d1, d2])
        player_hand2 = Hand([d1, d3, d4])

        p1 = NaivePlayer('Itay', 31, player_hand1)
        p2 = RandomPlayer('Ohad', 37, player_hand2)
        team1 = Team('Hawks', [p2])
        team2 = Team('Spurs', [p1])
        board1 = Board(10)

        g = Game(board1, team1, team2)
        self.assertEqual(g.play(), "Team Spurs wins Team Hawks")

        d1 = Domino(2, 2)
        d2 = Domino(3, 3)
        d3 = Domino(4, 5)
        d4 = Domino(5, 4)
        player_hand1 = Hand([d1, d2])
        player_hand2 = Hand([d1, d3, d4])

        p1 = NaivePlayer('Itay', 31, player_hand1)
        p2 = NaivePlayer('Ohad', 37, player_hand1)
        team1 = Team('Hawks', [p1])
        team2 = Team('Spurs', [p2])
        board1 = Board(10)

        g = Game(board1, team1, team2)
        self.assertEqual(g.play(), "Draw!")

