from S1E9 import Character


class Baratheon(Character):
    """Class inherits from Character class and represents a \
Baratheon character"""
    def __init__(self, first_name: str, is_alive: bool = True,
                 family_name: str = "Baratheon", eyes: str = "brown",
                 hairs: str = "dark") -> None:
        """The default constructor of Baratheon class

        Args:
            first_name (str): mandatory parameter
            is_alive (bool, optional): The health state of the character.
            family_name(str, optional): The family name.
            eyes (str, optional): Eye color.
            hairs (str, optional): Hair color.
        """
        assert isinstance(first_name, str), "First Name should be string"
        assert isinstance(is_alive, bool), "The attribut is_alive should be a \
boolean"
        assert isinstance(family_name, str), "Family Name should be string"
        assert isinstance(eyes, str), "Eye color should be string"
        assert isinstance(hairs, str), "Hair color should be string"
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __repr__(self) -> str:
        """Returns a string representation of the Baratheon object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self) -> str:
        """Returns a human-readable string representation \
of the Baratheon object."""
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self) -> None:
        """Method to change the health state of the character to False."""
        self.is_alive = False


class Lannister(Character):
    """Class inherits from Character class and represents \
a Lannister character"""
    def __init__(self, first_name: str, is_alive: bool = True,
                 family_name: str = "Lannister", eyes: str = "blue",
                 hairs: str = "light") -> None:
        """The default constructor of Lannister class

        Args:
            first_name (str): mandatory parameter
            is_alive (bool, optional): The health state of the character.
            family_name(str, optional): The family name.
            eyes (str, optional): Eye color.
            hairs (str, optional): Hair color.
        """
        assert isinstance(first_name, str), "First Name should be string"
        assert isinstance(is_alive, bool), "The attribut is_alive should be a \
boolean"
        assert isinstance(family_name, str), "Family Name should be string"
        assert isinstance(eyes, str), "Eye color should be string"
        assert isinstance(hairs, str), "Hair color should be string"
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __repr__(self) -> str:
        """Returns a string representation of the Lannister object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self) -> str:
        """Returns a human-readable string representation \
of the Lannister object."""
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self) -> None:
        """Method to change the health state of the character to False."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True,
                         family_name: str = "Lannister", eyes: str = "blue",
                         hairs: str = "light") -> 'Lannister':
        """Creates a new Lannister character.

        Args:
            first_name (str): First Name
            is_alive (bool, optional): The health state of the character.

        Returns:
            Lannister: A new instance of the Lannister class.
        """
        assert isinstance(first_name, str), "First Name should be string"
        assert isinstance(is_alive, bool), "The attribut is_alive should be a \
boolean"
        return cls(first_name, is_alive)
