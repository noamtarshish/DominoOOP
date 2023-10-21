from unittest import TestCase

import Collection
from Exceptions import InvalidNumberException, EmptyBoardException
from Domino import Domino
from Exceptions import InvalidNumberException, FullBoardException
from Board import Board
from Game import Game
from Hand import Hand
from NaivePlayer import NaivePlayer
from Team import Team


class TestBoard(TestCase):
    def test_init(self):
        self.assertRaises(InvalidNumberException, Board, 30)
        self.assertRaises(InvalidNumberException, Board, 29)
        self.assertRaises(InvalidNumberException, Board, 31)
        self.assertEqual([], Board(1).get_collection())

    def test_in_left(self):
        a = Board(8)
        d = Domino(1,2)
        a.add(d)
        g = Domino(2,2)
        a.add(g)
        f = Domino(2,3)
        a.add(g)

        self.assertEqual(Board.in_left(a), 1)
        self.assertEqual(Board.in_left(a), 1)
        self.assertNotEqual(Board.in_left(a), 2)


    def test_in_right(self):
        a = Board(8)
        d = Domino(1, 2)
        a.add(d)
        g = Domino(2, 2)
        a.add(g)

        self.assertEqual(Board.in_right(a), 2)
        self.assertNotEqual(Board.in_right(a), 1)


    def test_add(self):
        a = Board(8)
        d = Domino(1, 2)
        a.add(d)
        g = Domino(2, 2)
        f = Domino(2, 3)
        h = Domino(1, 5)


        self.assertTrue(Board.add(a, g))
        self.assertTrue(Board.add(a, f))
        self.assertTrue(Board.add(a, h,False))


    def test_add_left(self):
        a = Board(8)
        d = Domino(1, 2)
        g = Domino(2, 1)
        h = Domino(1, 4)
        a.add_left(d)

        self.assertTrue(Board.add_left(a, g))
        self.assertFalse(Board.add_left(a, h))


    def test_add_right(self):
        a = Board(8)
        d = Domino(1, 2)
        g = Domino(2, 1)
        h = Domino(1, 4)
        r= Domino(6,6)
        a.add_right(d)

        self.assertTrue(Board.add_right(a, g))
        self.assertTrue(Board.add_right(a, h))
        self.assertFalse(Board.add_right(a,r))


        b2=Board(1)

        b2.add_right(d)

        self.assertFalse(Board.add_right(b2, d))

    def test_len(self):
        a = Board(8)
        d = Domino(1, 2)
        a.add(d)
        self.assertTrue(Board.__len__(a), 1)


    def test_str(self):
        a = Board(8)
        d = Domino(1, 2)
        a.add(d)
        g = Domino(2, 2)
        a.add(g)
        self.assertEqual(d.__str__(), '[1|2]')
        self.assertEqual(str(g), '[2|2]')


    def test_repr(self):
        a = Board(8)
        d = Domino(1, 2)
        a.add(d)
        g = Domino(2, 2)
        a.add(g)
        self.assertEqual(repr(d), '[1|2]')

    def test_eq(self):
        a = Board(8)
        b = Board(8)
        c = Board(8)

        d = Domino(1, 2)
        a.add(d)
        e = Domino(1, 2)
        b.add(e)
        c.add(d)
        c.add(e)

        self.assertTrue(Collection.__eq__(a), b)
        self.assertTrue(Collection.__eq__(a), c)



    def test_ne(self):
        a = Board(8)
        b = Board(8)
        d = Domino(1, 2)
        a.add(d)
        e = Domino(1, 3)
        b.add(e)

        self.assertTrue(Collection.__ne__(a), b)

    def test_getitem(self):
        a = Board(8)
        b = Board(8)
        d = Domino(1, 2)
        a.add(d)
        e = Domino(1, 3)
        b.add(e)

        self.assertTrue(Board.__getitem__(a,0), d)
        self.assertTrue(Board.__getitem__(b,0), e)

    def test_contains(self):
        a = Board(8)
        b = Board(8)
        d = Domino(1, 2)
        a.add(d)
        e = Domino(1, 3)
        b.add(e)

        self.assertTrue(Board.__contains__(a, d))
        self.assertTrue(Board.__contains__(b, e))
        self.assertFalse(Board.__contains__(b, d))
