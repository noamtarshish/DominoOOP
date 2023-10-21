class Exceptions(Exception):
    pass

class EmptyBoardException(Exception):
    def __init__(self, message):
        """
        Function that define the init for the the exception
        :param message: optional message that describe the exception
        """
        self.message = "EmptyBoardException"

class FullBoardException(Exception):

    def __init__(self, message):
        """
        Function that define the init for the the exception
        :param message: optional message that describe the exception
        """
        self.message = "FullBoardException"

class NoSuchDominoException(Exception):

    def __init__(self, message):
        """
        Function that define the init for the the exception
        :param message: optional message that describe the exception
        """
        self.message = "NoSuchDominoException"

class InvalidNumberException(Exception):
    def __init__(self, message):
        """
        Function that define the init for the the exception
        :param message: optional message that describe the exception
        """
        self.message = message

    def __str__(self):
        """
        Function that return a string that describe the exception
        :return: the message
        """
        return "ERROR " + self.message
