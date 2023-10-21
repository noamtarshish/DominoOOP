from unittest import TestCase

from Domino import Domino
from Exceptions import InvalidNumberException, FullBoardException
from Board import Board
from Game import Game
from Hand import Hand
from NaivePlayer import NaivePlayer
from Team import Team
from Collection import Collection


class TestHand(TestCase):

    def test_add(self):
        a = Domino(1, 2)
        b = Domino(2, 2)
        c = Domino(3, 3)
        d = Domino(0, 1)
        lst1 = [a, b, c]
        dominoes1 = Hand(lst1)

        self.assertEqual(Hand.add(dominoes1,d), [a, b, c, d])
        self.assertEqual(Hand.add(dominoes1, d, 0), [d, a, b, c, d])


    def test_remove_domino(self):
        a = Domino(1, 2)
        b = Domino(2, 2)
        c = Domino(3, 3)
        lst1 = [a, b, c]
        dominoes1 = Hand(lst1)


        self.assertTrue(Hand.remove_domino(dominoes1, c))
        self.assertTrue(Hand.remove_domino(dominoes1, b))

    def test_getitem(self):
        a = Domino(1, 2)
        b = Domino(2, 2)
        c = Domino(3, 3)
        lst1 = [a, b, c]
        d = Domino(2, 1)
        e = Domino(2, 2)
        f = Domino(3, 3)
        lst2 = [d, e, f]
        g = Domino(4, 4)

        dominoes1 = Hand(lst1)
        dominoes2 = Hand(lst2)

        self.assertTrue(Hand.__getitem__(dominoes1, 0), a)
        self.assertTrue(Hand.__getitem__(dominoes1, 1), b)
        self.assertTrue(Hand.__getitem__(dominoes2, 0), d)


    def test_contains(self):
        a = Domino(1, 2)
        b = Domino(2, 2)
        c = Domino(3, 3)
        lst1 = [a, b, c]
        d = Domino(2, 1)
        e = Domino(2, 2)
        f = Domino(3, 3)
        lst2 = [d, e, f]
        g = Domino(4, 4)

        dominoes1 = Hand(lst1)
        dominoes2 = Hand(lst2)

        self.assertTrue(Hand.__contains__(dominoes1, a))
        self.assertFalse(Hand.__contains__(dominoes1, g))
        self.assertTrue(Hand.__contains__(dominoes2, a))


    def test_eq(self):
        a = Domino(1, 2)
        b = Domino(2, 2)
        c = Domino(3, 3)
        lst1 = [a, b, c]
        d = Domino(2, 1)
        e = Domino(2, 2)
        f = Domino(3, 3)
        lst2 = [d, e, f]

        dominoes1 = Hand(lst1)
        dominoes2 = Hand(lst2)

        self.assertTrue(Hand.__eq__(dominoes1, dominoes2))

    def test_ne(self):
        a = Domino(1, 2)
        b = Domino(2, 2)
        c = Domino(3, 3)
        lst1 = [a, b, c]
        d = Domino(2, 1)
        e = Domino(2, 2)
        f = Domino(3, 3)
        lst2 = [d, e, f]

        dominoes1 = Hand(lst1)
        dominoes2 = Hand(lst2)

        self.assertFalse(Hand.__ne__(dominoes1,dominoes2))


    def test_len(self):
        a = Domino(1, 2)
        b = Domino(2, 2)
        c = Domino(3, 3)
        lst = [a, b, c]
        dominoes = Hand(lst)

        self.assertTrue(Collection.__len__(dominoes), 3)

    def test_str(self):
        a = Domino(1, 2)
        b = Domino(2, 2)
        c = Domino(3, 3)
        lst = [a, b, c]
        dominoes = Hand(lst)

        self.assertEqual(str(dominoes), '[1|2][2|2][3|3]')

    def test_repr(self):
        a = Domino(1, 2)
        b = Domino(2, 2)
        c = Domino(3, 3)
        lst = [a ,b, c]
        dominoes = Hand(lst)

        self.assertEqual(repr(dominoes), '[1|2][2|2][3|3]')




