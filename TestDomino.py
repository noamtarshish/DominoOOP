from unittest import TestCase

from Domino import Domino



class TestDomino(TestCase):

    def test_get_left(self):
        g = Domino(1,2)
        f = Domino(2,1)
        self.assertEqual(Domino.get_left(g), 1)
        self.assertEqual(Domino.get_left(f), 2)

    def test_get_right(self):
        g = Domino(1, 2)
        f = Domino(2, 1)
        self.assertEqual(Domino.get_right(g), 2)
        self.assertEqual(Domino.get_right(f), 1)

    def test_str_Domino(self):
        a = Domino(1, 5)
        b = Domino(3, 5)
        c = Domino(4, 5)
        d = Domino(5, 5)
        e = Domino(6, 5)
        g = Domino(2, 2)
        f = Domino(2, 5)

        self.assertEqual(str(a), '[1|5]')
        self.assertEqual(str(b), '[3|5]')
        self.assertEqual(str(c), '[4|5]')
        self.assertEqual(str(d), '[5|5]')
        self.assertEqual(str(e), '[6|5]')
        self.assertEqual(str(g), '[2|2]')
        self.assertEqual(str(f), '[2|5]')

    def test_repr(self):
        g = Domino(2, 2)
        f = Domino(2, 5)
        a = Domino(1, 5)
        b = Domino(3, 5)
        c = Domino(4, 5)
        d = Domino(5, 5)
        e = Domino(6, 5)

        self.assertEqual(repr(a), '[1|5]')
        self.assertEqual(repr(b), '[3|5]')
        self.assertEqual(repr(c), '[4|5]')
        self.assertEqual(repr(d), '[5|5]')
        self.assertEqual(repr(e), '[6|5]')
        self.assertEqual(repr(g), '[2|2]')
        self.assertEqual(repr(f), '[2|5]')


    def test_eq(self):
        g = Domino(2,2)
        f = Domino(2,2)
        h = Domino(3,3)
        self.assertEqual(Domino.__eq__(g,f), True)
        self.assertEqual(Domino.__eq__(g,h), False)


    def test_ne(self):
        g = Domino(3, 3)
        f = Domino(2, 2)
        h = Domino(3, 3)
        self.assertEqual(Domino.__ne__(g, f), True)
        self.assertEqual(Domino.__ne__(g, h), False)
        self.assertEqual(Domino.__ne__(f, h), True)



    def test_gt(self):
        g = Domino(3, 3)
        f = Domino(2, 2)
        self.assertEqual(Domino.__gt__(g, f), True)
        self.assertEqual(Domino.__gt__(f, g), False)


    def test_contains(self):
        g = Domino(3, 3)
        f = Domino(2, 2)
        self.assertEqual(Domino.__contains__(g,1), False)
        self.assertEqual(Domino.__contains__(g,3), True)
        self.assertEqual(Domino.__contains__(f,2), True)
        self.assertEqual(Domino.__contains__(f,3), False)

    def test_flip(self):
        g = Domino(3,2)
        f = Domino(2,3)
        self.assertEqual(Domino.flip(g), f)

