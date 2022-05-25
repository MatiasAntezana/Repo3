from msilib.schema import Class
from player import Player

class Gnome (Player):
    def __init__(self, name, xy, face, hitpoints = 50):
        super().__init__(name,xy,face = face, hitpoints = hitpoints)

    def loc(self):
        return self.x, self.y