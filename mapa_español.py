import random
from typing import Optional, Tuple

import player
import items


Location = Tuple[int, int]


class Tile:
    """
    Tile(char: str, transitable: bool=True)

    Un mosaico es el objeto que se utiliza para representar el tipo de suelo de la mazmorra.

    Argumentos

    char (str): cadena de longitud 1 que se representa al representar un mapa.
    transitable (bool): indica si el mosaico es transitable o no.
    """
    def __init__(self, char: str, walkable: bool = True):
        self.walkable = walkable
        self.face = char

    def is_walkable(self) -> bool:
        """
        Devuelve Verdadero si el mosaico es transitable, Falso de lo contrario.
        """
        return self.walkable


AIR = Tile(' ')
WALL = Tile('▓', False)
STAIR_UP = Tile('<')
STAIR_DOWN = Tile('>')


class Level:
    """
    Nivel (filas: int, columnas: int) -> Nivel

    Argumentos

    filas (int) -- es el número de filas para el nivel.
    columnas (int) -- es el número de columnas para el nivel.

    Devuelve una instancia de un nivel.
    """
    def __init__(self, rows: int, columns: int):
        """Inicializa una clase de nivel de mazmorra. Consulte la documentación de la clase"""
        tiles = [[1] * 12 + [0] * (columns - 24) + [1] * 12]  # 0=air 1=rocks
        for row in range(1, rows):
            local = tiles[row - 1][:]
            for i in range(2, columns - 2):
                vecindad = local[i - 1] + local[i] + local[i + 1]
                local[i] = random.choice([0]*100+[1]*(vecindad**3*40+1))
            tiles.append(local)

        for row in range(0, rows):
            for col in range(0, columns):
                tiles[row][col] = AIR if tiles[row][col] == 0 else WALL

        self.tiles = tiles
        self.rows, self.columns = rows, columns
        self.items = {}

    def find_free_tile(self) -> Location:
        """Busca aleatoriamente una ubicación libre dentro del mapa del nivel.
        Este método nunca podría terminar."""
        i, j = random.randint(0, self.rows - 1), random.randint(0, self.columns - 1)
        while self.tiles[i][j] != AIR:
            i, j = random.randint(0, self.rows - 1), random.randint(0, self.columns - 1)
        return (j, i)

    def get_random_location(self) -> Location:
        """Calcule y devuelva una ubicación aleatoria en el mapa."""
        return random.randint(0, self.columns - 1), random.randint(0, self.rows - 1)

    def add_stair_up(self, location: Optional[Location] = None):
        """Agregue un mosaico de escalera ascendente a una ubicación determinada o aleatoria en el mapa."""
        if location is not None:
            j, i = location
        else:
            i = random.randint(0, self.rows - 1)
            j = random.randint(0, self.columns - 1)
        self.tiles[i][j] = STAIR_UP

    def add_stair_down(self, location: Optional[Location] = None):
        """Agregue un mosaico de escalera descendente a una ubicación aleatoria o dada en el mapa."""
        if location is not None:
            j, i = location
        else:
            i = random.randint(0, self.rows - 1)
            j = random.randint(0, self.columns - 1)
        self.tiles[i][j] = STAIR_DOWN

    def add_item(self, item: items.Item, location: Optional[Location] = None):
        """Agregue un elemento a una ubicación determinada en el mapa. Si no se proporciona ninguna ubicación, se busca aleatoriamente un espacio libre.
        """
        if location is None:
            j, i = self.find_free_tile()
        else:
            j, i = location
        items = self.items.get((i, j), [])
        items.append(item)
        self.items[(i, j)] = items

    def render(self, player: player.Player):
        """Dibuja el mapa en la terminal, incluidos el jugador y los elementos. El jugador debe tener un método loc(), devolviendo su ubicación y un atributo facial. Todos los elementos en el mapa deben tener un atributo de cara que se va a mostrar. Si hay varios elementos en una ubicación, solo se representará uno.
        """
        # completar (cuando se agregue el gnomo)
        print("-" + "-" * len(self.tiles[0]) + "-")
        for i, row in enumerate(self.tiles):
            print("|", end="")
            for j, cell in enumerate(row):
                if (j, i) == player.loc():
                    print(player.face, end='')
                elif (i, j) in self.items:
                    print(self.items[(i, j)][0].face, end='')
                else:
                    print(cell.face, end='')
            print("|")
        print("-" + "-" * len(self.tiles[0]) + "-")

    def is_walkable(self, location: Location):
        """Comprueba si un jugador puede caminar por un lugar determinado."""
        j, i = location
        return self.tiles[i % self.rows][j % self.columns].walkable

    def index(self, tile: Tile) -> Location:
        """Obtenga la ubicación de un mosaico determinado en el mapa. Si hay varios mosaicos de ese tipo, entonces solo uno es
        devuelto

        Argumentos

        mosaico (Mosaico) -- uno de los tipos de mosaicos conocidos (AIRE, PARED, ESCALERA_ABAJO, ESCALERA_ARRIBA)

        Devuelve la ubicación de ese tipo de tesela o plantea ValueError
        """
        for i in range(self.rows):
            try:
                j = self.tiles[i].index(tile)
                return j, i
            except ValueError:
                pass
        raise ValueError

    def loc(self, xy: Location) -> Tile:
        """Obtenga el tipo de mosaico en una ubicación dada."""
        j, i = xy
        return self.tiles[i][j]

    def get_items(self, xy: Location) -> list[items.Item]:
        """Obtenga una lista de todos los elementos en una ubicación determinada. Elimina los elementos de esa ubicación."""
        j, i = xy
        if (i, j) in self.items:
            items = self.items[(i, j)]
            del(self.items[(i, j)])
        else:
            items = []
        return items

    def dig(self, xy: Location) -> None:
        """Reemplace una PARED en la ubicación dada, por AIRE."""
        j, i = xy
        if self.tiles[i][j] is WALL:
            self.tiles[i][j] = AIR

    def is_free(self, xy: Location) -> bool:
        """Compruebe si una ubicación determinada está libre de otras entidades."""
        # completar
        raise NotImplementedError

    def are_connected(self, initial: Location, end: Location) -> bool:
        """Compruebe si hay un camino transitable entre la ubicación inicial y la ubicación final."""
        # completar
        raise NotImplementedError

    def get_path(self, initial: Location, end: Location) -> bool:
        """Devuelve una secuencia de ubicaciones entre la ubicación inicial y la ubicación final, si existe."""
        # completar
        raise NotImplementedError


class Dungeon:
    """Mazmorra(filas: int, columnas: int, niveles: int = 3) -> Mazmorra

    Argumentos

    filas (int) -- es el número de filas para la mazmorra.
    columnas (int) -- es el número de columnas para la mazmorra.
    niveles (int) -- es el número de niveles para la mazmorra (predeterminado: 3).

    Devuelve una instancia de una mazmorra.
    """
    def __init__(self, rows: int, columns: int, levels: int = 3):
        """Inicializa una clase de mazmorra. Ver documentación de la clase."""
        self.dungeon = [Level(rows, columns) for _ in range(levels)]
        self.rows = rows
        self.columns = columns
        self.level = 0

        self.stairs_up = [level.get_random_location() for level in self.dungeon]
        self.stairs_down = [level.get_random_location() for level in self.dungeon[:-1]]

        for level, loc_up, loc_down in zip(self.dungeon[:-1], self.stairs_up[:-1], self.stairs_down):
            # Ubicar escalera que sube
            level.add_stair_up(loc_up)

            # Ubicar escalera que baja
            level.add_stair_down(loc_down)

        # Ubicar escalera del nivel inferior
        self.dungeon[-1].add_stair_up(self.stairs_up[-1])

    def render(self, player: player.Player):
        """Dibuja el nivel actual en la terminal, incluidos el jugador y los elementos. El jugador debe tener un método loc(), regresando
        su ubicación y un atributo facial. Todos los elementos en el mapa deben tener un atributo de cara que se va a mostrar.
        Si hay varios elementos en una ubicación, solo se representará uno.
        """
        self.dungeon[self.level].render(player)

    def find_free_tile(self) -> Location:
        """Busca aleatoriamente una ubicación libre dentro del mapa del nivel.
        Este método nunca podría terminar.
        """
        return self.dungeon[self.level].find_free_tile()

    def is_walkable(self, tile: Tile):
        """Comprueba si un jugador puede caminar por un lugar determinado. Ver Level.is_walkable()."""
        return self.dungeon[self.level].is_walkable(tile)

    def add_item(self, item: items.Item, level: Optional[int] = None, xy: Optional[Location] = None):
        """Agregue un elemento a una ubicación determinada en el mapa de un nivel dado o actual. Si no se da una ubicación, una gratis
        el espacio se busca aleatoriamente. Es posible que este método no funcione nunca si la probabilidad de encontrar un espacio libre es baja.
        """
        if level is None:
            level = self.level + 1
        if 0 < level <= len(self.dungeon):
            self.dungeon[level - 1].add_item(item, xy)

    def loc(self, xy: Location) -> Tile:
        """Obtenga el tipo de mosaico en una ubicación dada."""
        return self.dungeon[self.level].loc(xy)

    def index(self, tile: Tile) -> Location:
        """Obtenga la ubicación de un mosaico determinado en el mapa. Si hay varios mosaicos de ese tipo, entonces solo uno es
        devuelto Ver Nivel.index().
        """
        return self.dungeon[self.level].index(tile)

    def get_items(self, xy: Location) -> list[items.Item]:
        """Obtenga una lista de todos los elementos en una ubicación determinada. Elimina los elementos de esa ubicación. Consulte Level.get_items()."""
        return self.dungeon[self.level].get_items(xy)

    def dig(self, xy: Location) -> None:
        """Reemplace una PARED en la ubicación dada, por AIRE. Consulte Nivel.dig()."""
        return self.dungeon[self.level].dig(xy)

    def is_free(self, xy: Location) -> bool:
        """Te dice si el casillero del mapa está vacio o no"""
        """
        NO SE HA IMPLEMENTADO. Compruebe si una ubicación determinada está libre de otras entidades. Ver Level.is_free()."""
        return self.dungeon[self.level].is_free(xy)
