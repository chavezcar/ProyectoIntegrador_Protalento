import os

def borrarTerminal():
    num = 0
    print(num)
    while num <= 50:
        letra = input('Presione la tecla "n" :')
        if letra == "n":
            os.system('cls' if os.name == 'nt' else 'clear')
        print(num)
        num += 1

borrarTerminal()
