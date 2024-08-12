from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The body of the King class that inherit from \
Character and Baratheonclass"""
    def __init__(self, first_name: str, is_alive: bool = True,
                 family_name: str = "Baratheon",
                 eyes: str = "brown", hairs: str = "dark") -> None:
        """The default constructor of Baratheon class

        Args:
            first_name (str): mandatory parameter
            is_alive (bool, optional): The health state of the character.
            family_name(str, optional): The family name.
            eyes (str, optional): Eye color.
            hairs (str, optional): Hair color.
        """
        super().__init__(first_name, is_alive, family_name, eyes, hairs)

    def set_eyes(self, eyes: str) -> None:
        """This function set the eye color of the current object

        Args:
            eyes (str): _description_
        """
        assert isinstance(eyes, str), "Eye color should be string"
        self.eyes = eyes

    def set_hairs(self, hairs: str) -> None:
        """This function set the hairs color of the current object

        Args:
            hairs (str): _description_
        """
        assert isinstance(hairs, str), "Hair color should be string"
        self.hairs = hairs

    def get_eyes(self) -> str:
        """This function return the eye color of the current object

        Returns:
            str: the eye color of the current object
        """
        return self.eyes

    def get_hairs(self) -> str:
        """This function return the hair color of the current object

        Returns:
            str: the hair color of the current object
        """
        return self.hairs
