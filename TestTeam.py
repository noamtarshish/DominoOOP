from unittest import TestCase
from unittest import TestCase
from Board import Board
from Domino import Domino
from Hand import Hand
from NaivePlayer import NaivePlayer
from RandomPlayer import RandomPlayer
from Team import Team


class TestTeam(TestCase):

    def test_get_team(self):
        d1 = Domino(2, 2)
        d2 = Domino(3, 3)
        player_hand = Hand([d1, d2])
        p1 = NaivePlayer('Itay', 31, player_hand)
        team1 = Team('Hawks', [d1,d2])
        self.assertTrue(team1.get_team(), ('Itay', 31, player_hand))

    def test_score_team(self):
        d1 = Domino(2, 2)
        d2 = Domino(3, 3)

        player_hand = Hand([d1,d2])
        p1 = NaivePlayer('Itay', 31, player_hand)
        team1 = Team('Hawks', [p1])
        self.assertEqual(team1.score_team(), 10)

    def test_has_dominoes_team(self):
        d1 = Domino(2, 2)
        d2 = Domino(3, 3)
        player_hand = Hand([d1,d2])
        p1 = NaivePlayer('Itay', 31, player_hand)
        team1 = Team('Hawks', [p1])
        self.assertEqual(team1.has_dominoes_team(), True)

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
        board = Board(10)
        self.assertTrue(team1.play(board), True)
        self.assertTrue(team2.play(board), True)


    def test_str(self):
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

        self.assertEqual(team1.__str__(),'Name Hawks, Score team: 10, Players: Name: Itay, Age: 31, Hand: [2|2][3|3], ''Score: 10')
        self.assertEqual(team2.__str__(),'Name Spurs, Score team: 22, Players: Name: Ohad, Age: 37, Hand: [2|2][4|5][5|4], ''Score: 22')

    def test_repr(self):
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

        self.assertEqual(team1.__repr__(),'Name Hawks, Score team: 10, Players: Name: Itay, Age: 31, Hand: [2|2][3|3], ''Score: 10')
        self.assertEqual(team2.__repr__(),'Name Spurs, Score team: 22, Players: Name: Ohad, Age: 37, Hand: [2|2][4|5][5|4], ''Score: 22')