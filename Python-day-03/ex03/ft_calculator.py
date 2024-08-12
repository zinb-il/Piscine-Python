class calculator:
    """A calculator class for performing arithmetic operations"""
    def __init__(self, vector: list[float]) -> None:
        """The default constructor of calculator class

        Args:
            object (list[float]): list of float number
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """Overloads the '+' operator to add a scalar to each \
element of the vector.

        Args:
            object (float): number to add to the instance
        """
        self.vector = [i + object for i in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Overloads the '*' operator to multiply each element of \
the vector by a scalar.

        Args:
            object (float): number to multiple to the instance
        """
        self.vector = [i * object for i in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Overloads the '-' operator to subtract a scalar \
from each element of the vector.

        Args:
            object (float): number to substruct to the instance
        """
        self.vector = [i - object for i in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Overloads the '/' operator to divide each element \
of the vector by a scalar.

        Args:
            object (float): number to divide to the instance
        """
        assert object != 0, "Division by zero is not allowed"
        self.vector = [i / object for i in self.vector]
        print(self.vector)
