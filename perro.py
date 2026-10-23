from animales_domesticos import Animales_Domesticos

class Canino(Animales_Domesticos):

    def __init__ (self, nombre, edad, duenio, raza, peso):
        super().__init__(nombre, edad, duenio, raza, peso)

    def atributos(self):
        super().atributos()


    def cambiar_edad_mayor(self, edad):
        self.edad = self.edad + edad

    def cambiar_edad_menor(self, edad):
        self.edad = self.edad - edad

    def etapa_vida(self):
        cachorro = self.edad >= 0 and self.edad < 3
        senior = self.edad >= 3 and self.edad < 11
        anciano = self.edad >= 11 and self.edad < 14

        if cachorro :
            print("Es cachorro")
            print()
            return "cachorro"
        elif senior:
            print("Es senior")
            return "senior"
        elif anciano:
            print("Es anciano")
            return "anciano"
        else:
            print("es MUY anciano")
            return "MUY anciano"


    def porcion_de_alimentos(self):
        etapa = self.etapa_vida()
        if etapa == "cachorro":
            porcion_comida = self.peso * 100
            print("porcion de comida que necesita tu cachorro es: ", porcion_comida, " gramos")

        elif etapa == "senior":
            porcion_comida = self.peso * 100
            print ("porcion de comida que necesita tu perro es: ", porcion_comida, " gramos")

        elif etapa == "anciano" or etapa == "MUY anciano":
            porcion_comida = self.peso * 30
            print("La porcion de comida que necesita tu perro anciano es: ", porcion_comida, " gramos")

