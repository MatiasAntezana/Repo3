import random
from typing import List, Tuple


import config


def render(tiles: List[List[int]], player: dict, gnome: dict):
    """
    Dibuja el mapa en la terminal, incluidos el jugador, los elementos y el gnomo.

    :param tiles: nivel de mazmorra, creado con level(). Es una lista de listas de enteros.
    :param player: ubicación del jugador en el mapa (dict).
    :param gnome: ubicación del gnomo en el mapa (dict).

    :return: Ninguno, el mapa se representa en la pantalla.
    """
    print("-" + "-" * len(tiles[0]) + "-")
    for i, row in enumerate(tiles):
        print("|", end="")
        for j, cell in enumerate(row):
            if (i, j) == player["location"]:
                print(player["face"], end='')
            elif gnome and (i, j) == gnome["location"]:
                print(gnome["face"], end='')
            elif cell == 0:
                print(config.SPACE, end='')
            elif cell == 1:
                print(config.WALL_ROCK, end='')
            else:
                print(cell, end='')
        print("|")
    print("-" + "-" * len(tiles[0]) + "-")


def level(rows: int, columns: int) -> List[List[int]]:
    """
    Crea un nivel de mazmorra

    :param rows: es el número de filas para el nivel (int).
    :param column: es el número de columnas para el nivel (int).

    :regresar: mapa de nivel
    """
    tiles = [[1] * 12 + [0] * (columns - 24) + [1] * 12]  # 0=air 1=rocks
    for row in range(1, rows):
        local = tiles[row - 1][:]
        for i in range(2, columns - 2):
            vecindad = local[i - 1] + local[i] + local[i + 1]
            local[i] = random.choice([0]*100+[1]*(vecindad**3*40+1))
        tiles.append(local)

    return tiles


def dungeon(rows: int, columns: int, levels: int = 3) -> List[List[List[int]]]:
    """
    Crea una mazmorra

    :param filas: es el número de filas para cada nivel (int).
    :param columnas: es el número de columnas para cada nivel (int).
    :param level: el número de niveles que debe tener la mazmorra (int).

    :regreso: mazmorra
    """
    dungeon_levels = [level(rows, columns) for _ in range(levels)]

    up = []
    down = []
    for i in range(levels - 1):
        # Up stairs
        x = random.randint(0, rows - 1)
        y = random.randint(0, columns - 1)
        up.append((x, y))
        dungeon_levels[i][x][y] = config.LADDER_UP

        # Down stairs
        x = random.randint(0, rows - 1)
        y = random.randint(0, columns - 1)
        down.append((x, y))
        dungeon_levels[i][x][y] = config.LADDER_DOWN

    # Last Up stair
    x = random.randint(0, rows - 1)
    y = random.randint(0, columns - 1)
    up.append((x, y))
    dungeon_levels[-1][x][y] = config.LADDER_UP

    return dungeon_levels


def add_item(dungeon: List[List[List[int]]], item: dict, level: int):
    """
    Coloca elementos en un mapa recién generado. La función no comprueba la inalcanzabilidad de las posiciones.

    :param dungeon: mazmorra a modificar.
    :param elemento: elemento para agregar
    :param nivel: número de piso

    :return: Sin valor de retorno, el mapa se modifica en el lugar.
    """
    x, y = item["location"]
    dungeon[level][x][y] = item["face"]


def is_tile(level: List[List[int]], location: Tuple[int, int], tile: str) -> bool:
    """
    Comprueba si una ubicación dada del mapa de nivel es de un tipo de mosaico dado, por ejemplo, una escalera arriba '<'.

    :param level: mapa de nivel de mazmorra (lista de listas de ints)
    :param location: coordenadas del mosaico a verificar (tupla de enteros)
    :param mosaico: tipo de mosaico para ver (todos los mosaicos tienen 1 carácter --- cadenas de longitud 1)

    :return: Verdadero si lo es, falso en caso contrario.
    """
    x, y = location
    return level[x][y] == tile


def set_tile(level: List[List[int]], location: Tuple[int, int], tile: str):
    """
    Establezca una ubicación dada de un mapa de nivel con el mosaico especificado.

    :param level: mapa de nivel de mazmorra (lista de listas de ints)
    :param location: coordenadas del mosaico a verificar (tupla de enteros)
    :param mosaico: tipo de mosaico para ver (todos los mosaicos tienen 1 carácter --- cadenas de longitud 1)

    :return: Sin valor de retorno, el mapa se modifica en el lugar.
    """
    x, y = location
    level[x][y] = tile


def is_free(level: List[List[int]], xy: Tuple[int, int]) -> bool:
    """Compruebe si una ubicación determinada está libre de otras entidades."""
    # completar
    raise NotImplementedError


def are_connected(level: List[List[int]], initial: Tuple[int, int], end: Tuple[int, int]) -> bool:
    """Compruebe si hay un camino transitable entre la ubicación inicial y la ubicación final."""
    # completar
    raise NotImplementedError


def get_path(level: List[List[int]], initial: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Devuelve una secuencia de ubicaciones entre la ubicación inicial y la ubicación final, si existe."""
    # completar
    raise NotImplementedError
