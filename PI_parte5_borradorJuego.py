import random
from readchar import readkey, key
import os

class Juego:

    def __init__(self):
        self.ficha_jugador = None
        self.nombre_jugador = None
        
        self.laberinto_list = None
        self.coordenada_inicial_x = None
        self.coordenada_inicial_y = None
        
        self.coordenada_x_final_juego = None
        self.coordenada_y_final_juego = None

        self.coordenada_final_x = None
        self.coordenada_final_y = None
        self.px = None
        self.py = None
        
    def limpiarTerminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def printTablero(self):
        self.limpiarTerminal()
        for fila in self.laberinto_list:
            string = ''.join(fila)
            print(string)

    def ponerFichaJugadorTablero(self):
        self.laberinto_list[self.px][self.py] = self.ficha_jugador

    def asignarCoordenadasIniciales(self):
        # Se asignan las coordenadas finales del tablero
        self.coordenada_final_x = len(self.laberinto_list) - 1
        self.coordenada_final_y = len(self.laberinto_list[0]) - 1
        # Se asignan las coordenadas finales del tablero
        self.px = self.coordenada_inicial_x
        self.py = self.coordenada_inicial_y
        
    def limitePared(self, x, y):
        return self.laberinto_list[x][y] != '#'

    def limitesCoordenadas(self, x: int, y: int):
        if x < 0 or y < 0:
            return False
        elif x == self.coordenada_final_x and y == self.coordenada_final_y:
            return self.limitePared(x, y)
        elif x > self.coordenada_final_x or y > self.coordenada_final_y:
            return False
        else:
            return self.limitePared(x, y)

    def changeTablero(self, tecla_presionada: str):
        if (tecla_presionada == key.DOWN):
            if self.limitesCoordenadas(self.px + 1, self.py):
                self.laberinto_list[self.px][self.py] = '.'
                self.laberinto_list[self.px + 1][self.py] = self.ficha_jugador
                self.px += 1
        elif (tecla_presionada == key.UP):
            if self.limitesCoordenadas(self.px - 1, self.py):
                self.laberinto_list[self.px][self.py] = '.'
                self.laberinto_list[self.px - 1][self.py] = self.ficha_jugador
                self.px -= 1
        elif (tecla_presionada == key.LEFT):
            if self.limitesCoordenadas(self.px, self.py - 1):
                self.laberinto_list[self.px][self.py] = '.'
                self.laberinto_list[self.px][self.py - 1] = self.ficha_jugador
                self.py -= 1
        elif (tecla_presionada == key.RIGHT):
            if self.limitesCoordenadas(self.px, self.py + 1):
                self.laberinto_list[self.px][self.py] = '.'
                self.laberinto_list[self.px][self.py + 1] = self.ficha_jugador
                self.py += 1
        
    def saludarJugador(self):
        print("Bienvenido al juego!!!... Tu Misión: atravesar el siguiente campo de batalla!!")
        print("Debes llegar hasta el final del Laberinto!!")
        print("La Salida esta ubicada en la última fila!!")
        nombre_jugador_juego = input("Ingresa tu nombre: ")
        ficha = input(f"Ingresa la ficha con la que deseas jugar {nombre_jugador_juego}: ")
        self.ficha_jugador = ficha
        self.nombre_jugador = nombre_jugador_juego

    def startGame(self):
        self.saludarJugador()
        self.ponerFichaJugadorTablero()
        self.printTablero()
        while (self.px, self.py) != (self.coordenada_x_final_juego, self.coordenada_y_final_juego):
            tecla_presionada = readkey()
            self.changeTablero(tecla_presionada)
            self.printTablero()
        print(f"Felicidades {self.nombre_jugador}, ERES UN GANADOR!!!")

class JuegoArchivo(Juego):

    def __init__(self):
        self.leerMapa()
        self.asignarCoordenadasIniciales()

    def leerMapa(self):
        listas_mapas = random.choice(os.listdir("tableros/"))
        ruta = "tableros/" + listas_mapas

        with open(ruta, "r", encoding="utf-8") as archivo:
            primeraLinea = next(archivo)
            posicion_x, posicion_y, final_x, final_y = (int(x) for x in primeraLinea.split())
            mapa = [list(linea.rstrip()) for linea in archivo]

            self.coordenada_inicial_x = posicion_y
            self.coordenada_inicial_y = posicion_x
            self.coordenada_x_final_juego = final_y
            self.coordenada_y_final_juego = final_x
            self.laberinto_list = mapa

game1 = JuegoArchivo()
game1.startGame()
