from perro import Canino


def pedir_datos_perro():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    duenio = input("Dueño: ")
    raza = input("Raza: ")
    peso = float(input("Peso: "))
    return Canino(nombre, edad, duenio, raza, peso)


animales = {}

perro1 = pedir_datos_perro()
animales[perro1.nombre] = perro1

perro2 = pedir_datos_perro()
animales[perro2.nombre] = perro2

for nombre, animal in animales.items():
    print(nombre)
    animal.atributos()