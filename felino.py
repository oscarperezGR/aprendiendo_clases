from animales_domesticos import Animales_Domesticos

class Felino(Animales_Domesticos):


    def __init__ (self, nombre, edad, duenio, raza, peso, garras):
        super().__init__(nombre, edad, duenio, raza, peso)
        self.garras = garras

    def estado_garras(self):
        opcion= int(input("Si alguna de estas opciones es afirmativa seleccione 1 : Puntas en forma de aguja, Visibles en reposo, sonido al caminar... De lo contrario pulse 2"))
        if opcion == 1:
            print("Debe cortar las garras")
        elif opcion == 2:
            print("Las garras se cortan de 2 a 4 semanas")
        else:
            print("Ingrese solo opcion 1 o 2")

    def atributos(self):
        super().atributos()
        print(".Garras: ",self.garras)