import os
from typing import List, Tuple
import readchar
from readchar import readkey, key

laberinto = """..###################
    ....#...............#
    #.#.#####.#########.#
    #.#...........#.#.#.#
    #.#####.#.###.#.#.#.#
    #...#.#.#.#.....#...#
    #.#.#.#######.#.#####
    #.#...#.....#.#...#.#
    #####.#####.#.#.###.#
    #.#.#.#.......#...#.#
    #.#.#.#######.#####.#
    #...#...#...#.#.#...#
    ###.#.#####.#.#.###.#
    #.#...#.......#.....#
    #.#.#.###.#.#.###.#.#
    #...#.#...#.#.....#.#
    ###.#######.###.###.#
    #.#.#.#.#.#...#.#...#
    #.#.#.#.#.#.#.#.#.#.#
    #.....#.....#.#.#.#.#
    ###################.."""

def saludar():
    nombreJugador = str(input("Cual es tu nombre? "))
    print(f"!Hola¡ {nombreJugador}... Bienvenido al Juego del Laberinto!!!")

saludar()

def convertir_matriz(laberinto):
    filas = laberinto.split('\n    ')
    matriz = [list(fila) for fila in filas]
    return matriz

mapa = convertir_matriz(laberinto)

punto_inicial = (0, 0)
punto_final = (len(mapa)-1, len(mapa[0])-1)

def mapa_visual(mapa):
    clear_terminal()
    for fila in mapa:
        print(''.join(fila))

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_loop(mapa: List[List[str]], punto_inicial: Tuple[int, int], punto_final: Tuple[int, int]):
    eje_x, eje_y = punto_inicial

    def mostrar_mapa():
        mapa[eje_x][eje_y] = 'P'
        mapa_visual(mapa)

    mostrar_mapa()

    while (eje_x, eje_y) != punto_final:
        pressed_key = readchar.readkey()
        nuevo_eje_x, nuevo_eje_y = eje_x, eje_y
        if pressed_key == key.UP and eje_x > 0 and mapa[eje_x - 1][eje_y] != '#':
            nuevo_eje_x -= 1
        elif pressed_key == key.DOWN and eje_x < len(mapa) -1 and mapa[eje_x + 1][eje_y] != '#':
            nuevo_eje_x += 1
        elif pressed_key == key.LEFT and eje_y > 0 and mapa[eje_x][eje_y - 1] != '#':
            nuevo_eje_y -= 1
        elif pressed_key == key.RIGHT and eje_y < len(mapa[0]) -1 and mapa[eje_x][eje_y + 1] != '#':
            nuevo_eje_y += 1
        
        mapa[eje_x][eje_y] = '.'
        eje_x, eje_y = nuevo_eje_x, nuevo_eje_y

        mostrar_mapa()

main_loop(mapa, punto_inicial, punto_final)

print("Fin del Juego!!")
print(f"Lo lograste!! Amigo, \nFelicidades eres el Ganador")