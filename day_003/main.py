import sys

# Izquierda o Derecha?
print(f"Llegamos a la isla del tesoro, tenemos poco tiempo para encontrar el tesoro, que camino elegimos? izquierda o derecha?")
resp= str(input())
if resp == "izquierda":
    print("Exploto una mina!! Game Over")
    sys.exit()

# Abrir la puerta o nadar?
print(f"Bien!, encontramos un lago y una puerta, que deberíamos elegir, nadar o entrar?")
resp= str(input())
if resp == "nadar":
    print("Estaba lleno de pirañas!! Game Over")
    sys.exit()

# Tomar la esfera Azul, Rojo, Amarillo
print(f"Genial!, detrás de la puerta hay 3 llaves para abrir el cofre del tesoro, qué color tomamos, rojo, azul o verde?")
resp= str(input())
if resp == "rojo":
    print("GANAMOS!!!")
else:
    print("Nos equivocamos, nos atraparon, Gamer Over")