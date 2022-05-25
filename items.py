from typing import Union


numeric = Union[float, int]


class Item:
    def __init__(self, name, face, type):
        self.name = name
        self.face = face
        self.type = type

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Item('{self.name}', '{self.face}')"
"""Creo que esto será para cuando trabaje con el personaje, osea especifica el item que tendrá el personaje """

class Sword(Item):
    def __init__(self, name: str, face: str, min_dmg: numeric, max_dmg: numeric):
        super().__init__(name, face==face, 'weapon')
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg 
        self.face = face
        """min_dmg = Es el mínimo daño que puede hacer, creo
           max_dmg = Es el máximo daño que puede hacer, creo"""


class Amulet(Item):
    def __init__(self, name: str, face: str):
        super().__init__(name, face, 'treasure')


class PickAxe(Item):
    def __init__(self, name: str, face: str):
        super().__init__(name, face==face, 'tool')
