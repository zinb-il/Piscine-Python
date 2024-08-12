class calculator:
    """A calculator class for performing arithmetic operations \
of two vectors"""
    def __init__(self) -> None:
        """The default constructor of calculator class"""
        pass

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """This Function calculates the dotproduct of two vectors

        Args:
            V1 (list[float]): First vectors of float values
            V2 (list[float]): Second vectors of float values
        """
        dot_product = sum([i * j for i, j in zip(V1, V2)])
        return print(f"Dot product is: {dot_product}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """This Function calculates the dotproduct of two vectors

        Args:
            V1 (list[float]): First vectors of float values
            V2 (list[float]): Second vectors of float values
        """
        sum_vec = [float(i + j) for i, j in zip(V1, V2)]
        return print(f"Add Vector is : {sum_vec}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """This Function calculates the subtraction of two vectors

        Args:
            V1 (list[float]): First vectors of float values
            V2 (list[float]): Second vectors of float values
        """
        sub_vec = [float(i - j) for i, j in zip(V1, V2)]
        return print(f"Sous Vector is: {sub_vec}")
