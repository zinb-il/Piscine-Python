from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for characters."""
    
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """The default constructor of character class.

        Args:
            first_name (str): mandatory parameter
            is_alive (bool, optional): The health state of the character
        """
        assert isinstance(first_name, str), "First Name should be string"
        assert isinstance(is_alive, bool), "The attribut is_alive should be a \
boolean"
        self.first_name = first_name
        self.is_alive = is_alive
        
    @abstractmethod
    def die(self)-> None:
        """Method to change the health state of the character to False."""
        pass

class Stark(Character):
    """this the body of the Stark class that inherit from Character class
    """
    def die(self):
        """Method to change the health state of the character to False."""
        self.is_alive = False