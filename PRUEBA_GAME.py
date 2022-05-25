from platform import platform
from re import X
import time
from player import Player
import mapping
import magic

import random
from human import Human
from items import Item, Sword
from gnome import Gnome
import actions


ROWS = 25
COLUMNS = 80

def bienvenida ():
    print ("Bienvenido jugador")
    print ("Para moverse en el mapa tiene que seguir las siguientes indicaciones")
    print ("Pulse w para ir hacia arriba, pulse a para ir a la izquierda, pulse s para ir hacia abajo y pulse d para ir hacia la derecha")

def nombre ():
    """Función que le pedidá que un nombre para el personaje"""
    nom = input ("Ingrese un nombre para su personaje ")
    while nom.isalpha() == False:
        nom = input ("Ingrese un nombre par su personaje ")
    return nom


if __name__ == "__main__":
    # initial parameters
    level = 0
    bienvenida()
    nam = nombre()
    player = Human(nam, (50,20), "@" , hitpoints = 50)
    hit_predeter = 50
    """(a,b), el a será la columna y el b la fila
    El nombre mepa que se guardó"""
    # initial locations may be random generated
    gnome = Gnome("gnome", (30,20), "G" , hitpoints = 50)

    item = Item("Espada","/","sword")

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).


    turns = 0
    while dungeon.level >= 0:
        turns += 1
        # render map
        while True:
            mapa = dungeon.render(player,gnome,item)
            print ("Player:",player.name, "Hp:",player.hitpoints,"/",hit_predeter)
            print ("Dlvl:",level)
            posicion = player.move_to(player.x,player.y)
            player = Human(nam, posicion, "@" ,)
        # read key
        hit = input()
        key = magic.read_single_keypress()
        # Hacer algo con keys:
        # move player and/or gnomes

    # Salió del loop principal, termina el juego