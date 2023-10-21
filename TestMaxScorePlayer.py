from unittest import TestCase
from Player import Player
from Domino import Domino
from Exceptions import InvalidNumberException, FullBoardException
from Board import Board
from Game import Game
from Hand import Hand
from NaivePlayer import NaivePlayer
from MaxScorePlayer import MaxScorePlayer
from Team import Team



class TestMaxScorePlayer(TestCase):

    def test_score(self):
        d1 = Domino(1, 2)
        d2 = Domino(1, 3)
        d3 = Domino(1, 4)
        d4 = Domino(1, 5)
        h = Hand([d1, d2, d3])
        z = Hand([d1, d2, d3, d4])
        p1 = MaxScorePlayer("Itay", 31, h)
        p2 = MaxScorePlayer("Ohad", 37, z)

        self.assertTrue(MaxScorePlayer.score(p1), 12)
        self.assertTrue(MaxScorePlayer.score(p2), 18)

    def test_play(self):
        d1 = Domino(1, 2)
        d2 = Domino(1, 1)
        d3 = Domino(1, 4)
        d4 = Domino(1, 5)
        a = Board(8)


        h = Hand([d1, d2, d3])
        p1 = MaxScorePlayer("Itay", 31, h)

        self.assertTrue(p1.play(a))
        self.assertTrue(p1.play(a))

    def test_has_dominoes(self):
        d1 = Domino(1, 2)
        d2 = Domino(1, 3)
        d3 = Domino(1, 4)
        d4 = Domino(1, 5)

        h = Hand([d1, d2, d3])
        p1 = MaxScorePlayer("Itay", 31, h)

        self.assertTrue(MaxScorePlayer.has_dominoes(p1))

    def test_str(self):
        d1 = Domino(1, 2)
        d2 = Domino(1, 3)
        d3 = Domino(1, 4)
        d4 = Domino(1, 5)
        z = Hand([d1, d2, d3, d4])
        h = Hand([d1, d2, d3])
        p1 = MaxScorePlayer("Itay", 31, h)
        p2 = MaxScorePlayer("Ohad", 37, z)

        self.assertEqual(str(p1), "Name: Itay, Age: 31, Hand: [1|2][1|3][1|4], Score: 12")
        self.assertEqual(str(p2), "Name: Ohad, Age: 37, Hand: [1|2][1|3][1|4][1|5], Score: 18")
        self.assertNotEqual(str(p2), "Name: Ohad, Age: 37, Hand: [1|2][1|3][1|4][1|5], Score: 12")

    def test_repr(self):
        d1 = Domino(1, 2)
        d2 = Domino(1, 3)
        d3 = Domino(1, 4)
        d4 = Domino(1, 5)
        z = Hand([d1, d2, d3, d4])
        h = Hand([d1, d2, d3])
        p1 = MaxScorePlayer("Itay", 31, h)
        p2 = MaxScorePlayer("Ohad", 37, z)

        self.assertEqual(repr(p1), "Name: Itay, Age: 31, Hand: [1|2][1|3][1|4], Score: 12")
        self.assertEqual(repr(p2), "Name: Ohad, Age: 37, Hand: [1|2][1|3][1|4][1|5], Score: 18")
        self.assertNotEqual(repr(p2), "Name: Ohad, Age: 37, Hand: [1|2][1|3][1|4][1|5], Score: 12")



