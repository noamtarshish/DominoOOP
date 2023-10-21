from Collection import Collection
import Exceptions
from Domino import Domino


class Board(Collection):
    def __init__(self, max_capacity):
        """
        Function that define the init for the class Board
        :param max_capacity: the max range for the board
        """
        Collection.__init__(self, [])
        if max_capacity not in range(1, 29):
            raise Exceptions.InvalidNumberException("The number should be between 1 and 28")
        self.max_capacity = max_capacity

    def in_left(self):
        """
        Function that return the leftest value in board. if the board is empty would raise an exception
        :return: int represent the leftest value in board / exception if board is empty
        """
        if len(self.array) == 0:
            raise Exceptions.EmptyBoardException("The board should not be empty for the game")
        else:
            return self.array[0].get_left()

    def in_right(self):
        """
        Function that return the rightest value in board. if the board is empty would raise an exception
        :return: int represent the rightest value in board / exception if board is empty
        """
        if len(self.array) == 0:
            raise Exceptions.EmptyBoardException("The board should not be empty for the game")
        else:
            return self.array[-1].get_right()

    def add(self, domino, add_to_right=True):
        """
        Function that help to add domino tilts to the board if possible. if add_to_right is True the method try to
        add the domino tilt to the right side of the board in the original form. if its not possible the function
        do flip to the domino tilt and try to add in this form. If it is not possible the function try to do the same
        for the left side
        :param domino: domino tilt
        :param add_to_right: if its True the method try to add the domino tilt to the right side of the board.
        :return: bool, True if the domino tilt add to the board and False if not / exception if the board is full
        """
        if self.max_capacity == len(self.array):
            raise Exceptions.FullBoardException("The board is full")
        elif len(self.array) == 0:
            self.array.append(domino)
            return True

        if add_to_right is True:

            return self.add_right(domino)


        if add_to_right is False:

           return self.add_left(domino)

    def add_left(self, domino):
        """
        Function that help to add domino tilts to the board if possible. the method try to
        add the domino tilt to the left side of the board in the original form. if its not possible the function
        do flip to the domino tilt and try to add in this form.
        :param domino: domino tilt
        :return: bool, True if the domino tilt add to the board and False if not
        """

        if len(self.array) == 0:
            self.array.append(domino)
            return True

        left_domino = self.array[0]

        if Domino.get_left(left_domino) == Domino.get_right(domino):
            self.array.insert(0, domino)
            return True

        if Domino.get_left(left_domino) == Domino.get_left(domino):
            self.array.insert(0, domino.flip())
            return True

        else:
            return False


    def add_right(self, domino):
        """
        Function that help to add domino tilts to the board if possible. the method try to
        add the domino tilt to the right side of the board in the original form. if its not possible the function
        do flip to the domino tilt and try to add in this form.
        :param domino: domino tilt
        :return: bool, True if the domino tilt add to the board and False if not
        """

        if len(self.array) == 0:
            self.array.append(domino)
            return True

        if len(self.array) == self.max_capacity:
            return False

        right_domino = self.array[-1]

        if Domino.get_right(right_domino) == Domino.get_left(domino):
            self.array.append(domino)
            return True

        if Domino.get_right(right_domino) == Domino.get_right(domino):
            self.array.append(domino.flip())
            return True

        else:
            return False







