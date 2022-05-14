from typing import List, Tuple

import config
import human


def move(level: List[List[int]],
         character: dict,
         direction: str):
    """
    Mueve una entidad de una ubicación dada a la ubicación adecuada según el nivel del juego y el equipo para el
    personaje.

    :param level: Piso de juego en el que se mueve el personaje.
    :param character: Diccionario que representa el carácter.
    :param dirección: comando ARRIBA, ABAJO, IZQUIERDA o DERECHA (configurado en caracteres.py)

    :return: Tupla con coordenadas donde el personaje se movería en la dirección dada
    sin contar enemigos ni peligros.
    Aún así, moverse hacia las paredes hace que los personajes sin PICK se paren y no se muevan.
    """
    # completar
    raise NotImplementedError


def move_to(level: List[List[int]], entity: dict, location: Tuple[int, int]):
    # completar
    raise NotImplementedError


def move_up(level: List[List[int]], entity: dict):
    # completar
    raise NotImplementedError


def move_left(level: List[List[int]], entity: dict):
    # completar
    raise NotImplementedError


def move_down(level: List[List[int]], entity: dict):
    # completar
    raise NotImplementedError


def move_right(level: List[List[int]], entity: dict):
    # completar
    raise NotImplementedError
