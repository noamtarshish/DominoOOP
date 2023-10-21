from unittest import TestCase

from Player import Player
from Domino import Domino
from Exceptions import InvalidNumberException, FullBoardException
from Board import Board
from Game import Game
from Hand import Hand
from NaivePlayer import NaivePlayer
from Team import Team



class TestPlayer(TestCase):

    def test_score(self):
        d1 = Domino(1, 2)
        d2 = Domino(1, 3)
        d3 = Domino(1, 4)
        d4 = Domino(1, 5)
        h = Hand([d1, d2, d3])
        z = Hand([d1, d2, d3, d4])
        p1 = Player("Itay", 31, h)
        p2 = Player("Ohad", 37, z)


        self.assertEqual(Player.score(p1), 12)
        self.assertEqual(Player.score(p2), 18)
        self.assertNotEqual(Player.score(p2), 10)



    def test_play(self):
        d1 = Domino(1, 2)
        d2 = Domino(1, 3)
        d3 = Domino(1, 4)
        d4 = Domino(1, 5)
        a = Board(8)


        h = Hand([d1, d2, d3])
        p1 = Player("Itay", 31, h)

        self.assertFalse(p1.play(a))

    def test_has_dominoes(self):
        d1 = Domino(1, 2)
        d2 = Domino(1, 3)
        d3 = Domino(1, 4)
        d4 = Domino(1, 5)

        h = Hand([d1, d2, d3])
        p1 = Player("Itay", 31, h)

        self.assertTrue(Player.has_dominoes(p1))

    def test_str(self):
        d1 = Domino(1, 2)
        d2 = Domino(1, 3)
        d3 = Domino(1, 4)
        d4 = Domino(1, 5)
        z = Hand([d1, d2, d3, d4])
        h = Hand([d1, d2, d3])
        p1 = Player("Itay", 31, h)
        p2 = Player("Ohad", 37, z)


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
        p1 = Player("Itay", 31, h)
        p2 = Player("Ohad", 37, z)


        self.assertEqual(repr(p1), "Name: Itay, Age: 31, Hand: [1|2][1|3][1|4], Score: 12")
        self.assertEqual(repr(p2), "Name: Ohad, Age: 37, Hand: [1|2][1|3][1|4][1|5], Score: 18")
        self.assertNotEqual(repr(p2), "Name: Ohad, Age: 37, Hand: [1|2][1|3][1|4][1|5], Score: 12")


