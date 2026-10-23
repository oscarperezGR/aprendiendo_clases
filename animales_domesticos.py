class Animales_Domesticos:

    def __init__(self, nombre, edad, duenio, raza, peso):
        self.nombre = nombre
        self.edad = edad
        self.duenio = duenio
        self.raza = raza
        self.peso = peso

    def atributos(self):
        print(self.nombre, ":", sep="")
        print(".edad:", self.edad)
        print(".dueño:", self.duenio)
        print(".raza:", self.raza)
        print(".peso:", self.peso)


