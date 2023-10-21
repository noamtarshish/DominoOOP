import Exceptions

class Domino:
    def __init__(self, left, right):
        """
        Function that define the array for the class Domino
        :param left: integer number in range 0 to 6
        :param right: integer number in range 0 to 6
        """
        if left not in range(0,7):
            raise Exceptions.InvalidNumberException("The number should be between 0 and 6")
        if right not in range(0,7):
            raise Exceptions.InvalidNumberException("The number should be between 0 and 6")
        self.__left = left
        self.__right = right

    def get_left(self):
        """
        Function that return the left side in the domino tilt.
        :return: the left side in the domino tilt
        """
        return self.__left

    def get_right(self):
        """
        Function that return the right side in the domino tilt.
        :return: the right side in the domino tilt
        """
        return self.__right

    def __str__(self):
        """
        Function that return string representing the current domino tilt
        :return: string
        """
        return "[" + str(self.__left) + "|" + str(self.__right) + "]"

    def __repr__(self):
        """
        Function that return string representing the current domino tilt
        :return: string
        """
        return "[" + str(self.__left) + "|" + str(self.__right) + "]"

    def __eq__(self, other):
        """
        Function that check if self object equal to other object
        :param other: object to check equal
        :return: Bool, True if equal and False if not
        """
        return (self.__left == other.__right and self.__right == other.__left) or (self.__left == other.__left and self.__right == other.__right)

    def __ne__(self, other):
        """
        Function that check if self object not equal to other object
        :param other: object to check equal
        :return: Bool, True if not equal and False if equal
        """
        return (self.__left != other.__right or self.__right != other.__left) and (self.__left != other.__left or self.__right != other.__right)

    def __gt__(self, other):
        """
        Function that check if the current domino tilt is greater than object other
        :param other: object
        :return: bool if self greater than other, False if not
        """
        return self.__left + self.__right > other.__left + other.__right

    def __contains__(self, key):
        """
        Function that check if key is in one of the sides in domino tilt
        :param key: integer
        :return: bool if key is in one of the sides in domino tilt, False if not
        """
        if self.__right == key or self.__left == key:
            return True
        else:
            return False

    def flip(self):
        """
        Function that take the current domino tilt and replace between the sides of domino tilt
        :return: object from Domino type with the opposite values for the domino tilt
        """
        flip_left = self.__right
        flip_right = self.__left
        return Domino(flip_left, flip_right)



