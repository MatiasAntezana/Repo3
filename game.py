#!/usr/bin/env python3
import time
import mapping
import magic

import random
from human import Human
from items import Item
from gnome import Gnome
import actions


ROWS = 25
COLUMNS = 80



if __name__ == "__main__":
    # initial parameters
    level = 0
    player = Human("player", (50,20), "@" , hitpoints = 150)
    """(a,b), el a será la columna y el b la fila"""

    # initial locations may be random generated
    gnome = Gnome("gnome", (30,20), "G" , hitpoints = 150)

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).

    turns = 0
    while dungeon.level >= 0:
        turns += 1
        # render map
        dungeon.render(player, gnome)
        hit = input ()
        # read key
        key = magic.read_single_keypress()

        # Hacer algo con keys:
        # move player and/or gnomes

    # Salió del loop principal, termina el juego
        