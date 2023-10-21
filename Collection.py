class Collection:
    def __init__(self, array):
        """
        Function that define the array for the class
        :param array: list
        """
        self.array = array

    def get_collection(self):
        """
        Function that return the array
        :return: array
        """
        return self.array

    def add(self, item, option):
        """
        Function that add arguments to array by some rules. In this function the method will not implemented.
        :param item: object
        :param option: object
        :return: Exception because the method will not implemented in this function
        """
        raise NotImplementedError("This method would not implemented in this class")

    def __getitem__(self, i):
        """
        Function that return the argument in index i in array
        :param i: index
        :return: object in place i
        """
        if i >= len(self.array):
            return None
        else:
            return self.array[i]

    def __eq__(self, other):
        """
        Function that check if self object equal to other object
        :param other: object to check equal
        :return: Bool, True if equal and False if not
        """
        for i in range(len(self.array)):
            temp = False
            for j in range(len(other.array)):
                if self.array[i] == other.array[j]:
                    temp = True

            if temp is False:
                return False
        return True

    def __ne__(self, other):
        """
        Function that check if self object not equal to other object
        :param other: object to check equal
        :return: Bool, True if not equal and False if equal
        """
        return not self.__eq__(other)

    def __len__(self):
        """
        Function that return the numbers of objects in array.
        :return: the numbers of object in array
        """
        return len(self.array)

    def __contains__(self, item):
        """
        Function that check if item is in array by method __eq__
        :param item: object
        :return: bool, True if item is in array and False if not
        """
        for i in self.array:
            if i.__eq__(item) is True:
                return True
        return False

    def __str__(self):
        """
        Function that return string representing the current Collection
        :return: string
        """
        string = ''
        for i in self.array:
            string = string + str(i)
        return string

    def __repr__(self):
        """
        Function that return string representing the current Collection
        :return: string
        """
        string = ''
        for i in self.array:
            string = string + str(i)
        return string

