import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Representation of student with a name, surname, active, login
    and id attributes."""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Runs after init"""
        self.id = generate_id()
        self.login = self.name[0] + self.surname
