import random
#PIEDRA, PAPEL O TIJERA
print("----------BIENVENIDO A PIEDRA, PAPEL O TIJERA----------")
com_opc = ("piedra","papel","tijera")
acum_j = 0
acum_pc = 0
y = 0
z = 0
def pi(tu_opc, x):
    com_opc = ("piedra","papel","tijera")
    if x == com_opc[0]:
        print(f"{tu_opc} vs {com_opc[0]}: EMPATE")
        return 0,0
    elif x == com_opc[1]:
        print(f"{tu_opc} vs {com_opc[1]}: PERDISTE")
        return 0,1
    elif x == com_opc[2]:
        print(f"{tu_opc} vs {com_opc[2]}: GANASTE")
        return 1,0
def pa(tu_opc, x):
    com_opc = ("piedra","papel","tijera")
    if x == com_opc[0]:
        print(f"{tu_opc} vs {com_opc[0]}: GANASTE")
        return 1,0
    elif x == com_opc[1]:
        print(f"{tu_opc} vs {com_opc[1]}: EMPATE")
        return 0,0
    elif x == com_opc[2]:
        print(f"{tu_opc} vs {com_opc[2]}: PERDISTE")
        return 0,1
def tij(tu_opc, x):
    com_opc = ("piedra","papel","tijera")
    if x == com_opc[0]:
        print(f"{tu_opc} vs {com_opc[0]}: PERDISTE")
        return 0,1
    elif x == com_opc[1]:
        print(f"{tu_opc} vs {com_opc[1]}: GANASTE")
        return 1,0
    elif x == com_opc[2]:
        print(f"{tu_opc} vs {com_opc[2]}: EMPATE")
        return 0,0
def reini():
    rei_siono = input("Quieres reiniciar el juego? (si/no) :")
    rei_siono = rei_siono.lower()
    if rei_siono == "si":
        print("Reiniciando...")
        return 0,0
    elif rei_siono == "no":
        print("Apagando...")
        return 1,1
    else:
        print("Supongo que es un 'no'...")
        return 1,1
while True:
    a = random.randint(0,2)
    x = com_opc[a]
    tu_opc = input("Ingresa tu opcion: ")
    tu_opc = tu_opc.lower()
    if tu_opc == "piedra":
        y,z = pi(tu_opc, x)
        acum_j += y
        acum_pc += z
    elif tu_opc == "papel":
        y,z = pa(tu_opc, x)
        acum_j += y
        acum_pc += z
    elif tu_opc == "tijera":
        y,z = tij(tu_opc, x)
        acum_j += y
        acum_pc += z
    else:
        print("Por favor escriba: piedra, papel o tijera...")
        
    if acum_j == 3:
        print("FELICIDADES, HAS GANADO EL JUEGO")
    elif acum_pc == 3:
        print("QUE TRISTE, PERDISTE EL JUEGO...")

    if acum_j == 3 or acum_pc == 3:
        y,z = reini()
        acum_j *= y
        acum_pc *= z
        if acum_j == 3 or acum_pc == 3:
            break
       