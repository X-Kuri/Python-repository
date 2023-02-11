#Programming rock paper scissors lizard spock game  in python

def random():
    import random
    return random.randint(0,4)
    
print("Este es el juego piedra papel tijeras lagarto spock")
print("Elige una opcion")
print("0 = piedra")
print("1 = papel")
print("2 = tijeras")
print("3 = lagarto")
print("4 = spock")
print("5 = salir")


def game():
    nombres = ["Piedra", "Papel", "Tijeras", "Lagarto", "Spock"]
    player = int(input("elige una opcion: "))
    if player == 5:
        print("Cerrando juego. Hasta lueguito.")
        return
    computer = random()
    #print("la computadora eligio: ",nombres[computer])
    if player == computer:
        print("Elegiste:",nombres[player],"Computadora eligio:",nombres[computer])
        print("empate")
    elif player == 0 and computer == 2:
        print("Elegiste piedra y la computadora eligio tijeras")
        print("Piedra aplasta tijeras")
        print("Ganaste!!!!!!")
    elif player == 0 and computer == 3:
        print("Elegiste piedra y la computadora eligio lagarto")
        print("Piedra aplasta lagarto")
        print("Ganaste!!!!!!")
    elif player == 1 and computer == 0:
        print("Elegiste papel y la computadora eligio piedra")
        print("Papel envuelve piedra")
        print("Ganaste!!!")
    elif player == 1 and computer == 4:
        print("Elegiste papel y la computadora eligio spock")
        print("Papel desaprueba a spock")
        print("Ganaste!!!")
    elif player == 2 and computer == 1:
        print("Elegiste tijeras y la computadora eligio papel")
        print("Tijeras corta papel")
        print("Ganaste!!!")
    elif player == 2 and computer == 3:
        print("Elegiste tijeras y la computadora eligio lagarto")
        print("Tijeras decapita lagarto")
        print("Ganaste!!!")
    elif player == 3 and computer == 1:
        print("Elegiste lagarto y la computadora eligio papel")
        print("Lagarto come papel")
        print("Ganaste!!!")
    elif player == 3 and computer == 4:
        print("Elegiste lagarto y la computadora eligio spock")
        print("lagarto envenena spock")
        print("Ganaste!!!")
    elif player == 4 and computer == 0:
        print("Elegiste spock y la computadora eligio piedra")
        print("Spock vaporiza la piedra")
        print("Ganaste!!!")
    elif player == 4 and computer == 2:
        print("Elegiste spock y la computadora eligio tijeras")
        print("Spock rompe tijeras") 
        print("Ganaste!!!")
    elif player == 0 and computer == 1:
        print("Elegiste piedra y la computadora eligio papel")
        print("Papel envuelve piedra")
        print("Perdiste D:")
    elif player == 0 and computer == 4:
        print("Elegiste piedra y la computadora eligio spock")
        print("Spock vaporiza la piedra")
        print("Perdiste D:")
    elif player == 1 and computer == 2:
        print("Elegiste papel y la computadora eligio tijeras")
        print("Tijeras corta papel")
        print("Perdiste D:")
    elif player == 1 and computer == 3:
        print("Elegiste papel y la computadora eligio lagarto")
        print("Lagarto come papel")
        print("Perdiste D:")
    elif player == 2 and computer == 0:
        print("Elegiste tijeras y la computadora eligio piedra")
        print("Piedra aplasta tijeras")
        print("Perdiste D:")
    elif player == 2 and computer == 4:
        print("Elegiste tijeras y la computadora eligio spock")
        print("Spock rompe tijeras")
        print("Perdiste D:")
    elif player == 3 and computer == 0:
        print("Elegiste lagarto y la computadora eligio piedra")
        print("Piedra aplasta lagarto")
        print("Perdiste D:")
    elif player == 3 and computer == 2:
        print("Elegiste lagarto y la computadora eligio tijeras")
        print("Tijeras decapita lagarto")
        print("Perdiste D:")
    elif player == 4 and computer == 1:
        print("Elegiste spock y la computadora eligio papel")
        print("Papel desaprueba a spock")
        print("Perdiste D:")
    elif player == 4 and computer == 3:
        print("Elegiste spock y la computadora eligio lagarto")
        print("Lagarto envenena spock")
        print("Perdiste D:")
    game()

game()