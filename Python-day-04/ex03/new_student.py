import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random string of 15 lowercase characters.

    Returns:
        str: A randomly generated 15-character string.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represents a student with automatically generated login and ID.

    Attributes:
        name (str): The student's first name.
        surname (str): The student's last name.
        login (str): Automatically generated login.
        id (str): Automatically generated 15-character ID.
        active (bool): Indicates if the student is active. Defaults to True.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname
        self.id = generate_id()
