# Proyecto Integrador - PROTALENTO.
El proyecto de este curso estará basado en la creación y desarrollo de un videojuego de texto para recorrer laberintos.

Este consistirá en laberintos representados por caracteres ASCII dónde el símbolo "#" representará una pared, el símbolo "." un pasillo y la letra "P" el personaje que deberá completar todo el recorrido del laberinto hasta el final.

El código del programa deberá estructucturarse para que el jugador se pueda mover por el mapa usando las teclas ↑ ↓ ← → de tu teclado.

### Fases de las entregas del proyecto.
El desarrollo de este proyecto está planeado en 5 fases de entrega, teniendo en cuenta las indicaciones del mentor de Protalento.

------------

##### Proyecto Integrador - Entrega No. 1:
- Crear un archivo README.md con la descripción del proyecto escrita por ti, esta será tu documentación del proyecto.
- Crear el archivo main del proyecto, dentro del cual se debe pedir el nombre del jugador por teclado e imprimir un mensaje de bienvenida con el nombre.

###### Archivos de la Entrega No. 1:
1. PI_parte1_main.py
2. Readme.md
------------

##### Proyecto Integrador - Entrega No. 2:
- Instalar la librería: https://pypi.org/project/readchar/.
- Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ indicada como UP.

###### Archivos de la Entrega No. 2:
1. PI_parte2_bucleTeclas.py
------------

##### Proyecto Integrador - Entrega No. 3:
- Aprender a utilizar la instrucción "os.system('cls' if os.name=='nt' else 'clear')" con el fin de borrar la terminar e imprimir nuevo contenido.
- Escribir un programa que inicie con el número en 0, el usuario deberá pulsar la tecla `n` por consola y por cada 'n' presionada, el programa deberá borrar la terminal e imprimir el nuevo número hasta llegar al número 50.

###### Archivos de la Entrega No. 3:
1. PI_parte3_borrarTerminal.py
------------

##### Proyecto Integrador - Entrega No. 4:
- Implementar una función que reciba el mapa de un laberinto en forma de cadena, y lo convierta a matriz de caracteres. El mapa viene dado dentro de las especificaciones del proyecto como una cadena de string y se encuentra asignado a la variable "laberinto".
- Escribir una función que limpie la pantalla y muestre la matriz (recibe el mapa en forma de matriz).
- Implementar el main loop en una función (recibe el mapa en forma de matriz).

###### Archivos de la Entrega No. 4:
1. PI_parte4_mostrarMapa.py
------------

##### Proyecto Integrador - Entrega No. 5:
- Crear una nueva clase JuegoArchivo la cual hereda de Juego.
- Reescribir el constructor para leer un archivo al azar de una carpeta que contenga los mapas cada vez que se instancia el juego.
- Crear un método que lea los datos de estos archivos de mapa y devuelva una cadena que tenga concatenada todas las filas leídas del mapa y las coordenadas de inicio y fin. Al final de la lectura antes de retornar usar cadena.strip() para eliminar caracteres en blanco residuales.

###### Archivos de la Entrega No. 5:
1. PI_parte5_borradorJuego.py
------------
