from distutils.fancy_getopt import fancy_getopt

from atomicwrites import move_atomic


class Player:
    def __init__(self, name, xy, face, hitpoints=50):
        self.name = name
        self.x, self.y = xy
        self.hp = hitpoints
        self.max_hp = hitpoints
        self.face = face

    def loc(self):
        return self.x, self.y

    def move_to(self,xy):
        print (xy)
        #self.x, self.y = xy

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Player('{self.name}', '{self.loc}', '{self.hp}')"
