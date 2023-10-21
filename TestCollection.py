import array
from unittest import TestCase
from Collection import Collection

class TestCollection(TestCase):

    def test_get_collection(self):
        a = [1, 2 ,3 ,4]
        array_a = Collection(a)
        self.assertEqual(Collection.get_collection(array_a), [1,2,3,4])

    def test_getitem(self):
         a = [1, 2, 3 ,4]
         array_a = Collection(a)
         self.assertEqual(Collection.__getitem__(array_a,2), 3)

    def test_eq(self):
        a = [1, 2 ,3 ,4]
        b = [1, 2 ,5 ,3]
        c = [1, 2 ,3 ,4]
        col1 = Collection(a)
        col2 = Collection(b)
        col3 = Collection(c)
        self.assertFalse(Collection.__eq__(col1,col2))
        self.assertTrue(Collection.__eq__(col1,col3))

    def test_ne(self):
        a = [1, 2, 3, 4]
        b = [1, 2, 5, 3]
        c = [1, 2, 3, 4]
        col1 = Collection(a)
        col2 = Collection(b)
        col3 = Collection(c)
        self.assertTrue(Collection.__ne__(col1, col2))
        self.assertFalse(Collection.__ne__(col1, col3))

    def test_len(self):
        a = [1, 2, 3, 4]
        b = [1, 2, 5, 3]
        c = [1, 2, 3, 4]
        col1 = Collection(a)
        col2 = Collection(b)
        col3 = Collection(c)

        self.assertEqual(Collection.__len__(col1), 4)
        self.assertNotEqual(Collection.__len__(col1), 3)

    def test_contains(self):
        b = [1, 2, 5, 3]
        col2 = Collection(b)

        self.assertTrue(Collection.__contains__(col2, 2))
        self.assertFalse(Collection.__contains__(col2, 7))

    def test_str(self):
        a = Collection([1,2,3,4])
        self.assertEqual(str(a), '1234')

    def test_repr(self):
        a = Collection([1,2,3,4])
        self.assertEqual(repr(a), '1234')


