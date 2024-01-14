import readchar

def main():
    print("Presiona la tecla ↑ para salir.")
    
    while True:
        # Lee la tecla presionada
        key = readchar.readkey()
        # Imprime la tecla
        print(f"Tecla presionada: {key}")
        # Verifica si la tecla de flecha arriba fue presionada para salir del bucle
        if key == readchar.key.UP:
            print("Tecla ↑ presionada. Saliendo del programa.")
            break

if __name__ == "__main__":
    main()
