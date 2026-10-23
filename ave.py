
from animales_domesticos import Animales_Domesticos

class Ave(Animales_Domesticos):
    def __init__(self, nombre, edad, duenio, raza, peso, long_pico):
        super().__init__(nombre, edad, duenio, raza, peso)
        self.long_pico = long_pico

    def atributos(self):
        super().atributos()
        print(".Longitud del pico: ",self.long_pico)

    def longitud_pico(self):
        opcion= int(input("Seleccione 1 si la afirmacion es correcta, de lo contrario cualquier otro numero: * La mandibua (pico) superior sobrepasa el limite inferior?"))
        if opcion == 1:
            print("Debe cortar el pico con dremel o lima")
        else:
            print("Un pico mas grande de lo normal es malo para el ave")

