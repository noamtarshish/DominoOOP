from Collection import Collection
import Exceptions

class Hand(Collection):

    def __init__(self, dominoes):
        """
        Function that define the init for the class hand
        :param dominoes: list of domino tilts
        """
        Collection.__init__(self, dominoes)

    def add(self, domino, index=None):
        """
        Function that have a method that add domino tilt to the array in specific index
        :param domino: domino tilt
        :param index: index
        :return: the updated array after the add.
        """
        if index is None:
            self.array.append(domino)
            return self.array
        else:
            self.array.insert(index, domino)
            return self.array

    def remove_domino(self, domino):
        """
        Function that have a method to remove domino tilt from the array and return the index of the domino tilt.
        the domino tilts will equal by __eq__ method. if the domino tilt does not found in the board the method raise
        exception from type "NoSuchDominoException".
        :param domino: domino tilt
        :return: index of the domino tilt in array / exception if it is not possible to remove the domino tilt.
        """
        for i in range(len(self.array)):
            if domino.__eq__(self.__getitem__(i)) is True:
                self.array.pop(i)
                return i
        raise Exceptions.NoSuchDominoException("The Domino is not in board")

    def __getitem__(self, i):
        """
        Function that return the argument in index i in array
        :param i: index
        :return: object in place i
        """
        return Collection.__getitem__(self, i)

    def __contains__(self, key):
        """
        Function that check if item is in array by method __eq__
        :param item: object
        :return: bool, True if item is in array and False if not
        """
        return Collection.__contains__(self, key)

    def __eq__(self, other):
        """
        Function that check if self object equal to other object
        :param other: object to check equal
        :return: Bool, True if equal and False if not
        """
        return Collection.__eq__(self, other)

    def __ne__(self, other):
        """
        Function that check if self object not equal to other object
        :param other: object to check equal
        :return: Bool, True if not equal and False if equal
        """
        return Collection.__ne__(self, other)

    def __len__(self):
        """
        Function that return the numbers of objects in array.
        :return: the numbers of object in array
        """
        return Collection.__len__(self)

    def __str__(self):
        """
        Function that return string representing the current Collection
        :return: string
        """
        return Collection.__str__(self)

    def __repr__(self):
        """
        Function that return string representing the current Collection
        :return: string
        """
        return Collection.__repr__(self)





