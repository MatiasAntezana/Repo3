import random
from player import Player


class Human(Player):
    def __init__(self, name, xy, face = "@",hitpoints = 50):
        super().__init__(name, xy, face = face, hitpoints=hitpoints)
        self.weapon = None
        self.treasure = None
        self.tool = None
        self.alive = True
        self.face = '@'
        self.hitpoints = hitpoints

    def damage(self):
        if self.sword:
            return random.random() * 20 + 5
        return random.random() * 10 + 1

    def move_to(self, posi,posi2):
        movi = input ("Ingrese una tecla ")
        movi = movi.lower()
        letras = ["a","w","s","d"]
        while movi not in letras:
            movi = input ("Ingrese una tecla ")
            movi = movi.lower()
        if movi == "w":
            posi2 = posi2 - 1
            return posi,posi2
        elif movi == "a":
            posi = posi - 1
            return posi,posi2
        elif movi == "s":
            posi2 = posi2 + 1
            return posi,posi2
        elif movi == "d":
            posi = posi + 1
            return posi,posi2
        #return super().move_to(xy)

    def kill(self):
        self.hp = 0
        self.alive = False

    def has_sword(self):
        print ("jeje")
        #Completar
