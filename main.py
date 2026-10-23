
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


    def cambiar_edad_mayor(self, edad):
        self.edad = self.edad + edad

    def cambiar_edad_menor(self, edad):
        self.edad = self.edad - edad

    def etapa_vida(self):
        cachorro = self.edad > 0 and self.edad < 3
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
            porcion_comida = self.peso * 0.1
            porcion_comida = porcion_comida * 1000
            print("porcion de comida que necesita tu cachorro es: ", porcion_comida, " gramos")

        elif etapa == "senior":
            porcion_comida = self.peso * 0.1
            porcion_comida = porcion_comida * 1000
            print ("porcion de comida que necesita tu perro es: ", porcion_comida, " gramos")

        elif etapa == "anciano" or etapa == "MUY anciano":
            porcion_comida = self.peso * 0.03
            porcion_comida = porcion_comida * 1000
            print("La porcion de comida que necesita tu perro anciano es: ", porcion_comida, " gramos")



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


perro=Animales_Domesticos("Pako2",4,"Oscar","pastor-aleman", 12)
gato=Felino ("Miau", 3, "Paco", "Egipcio", 4, "cortas")
ave=Ave("lorito", 1, "Paquita", "monte", 1, "normal")

perro.atributos()
perro.porcion_de_alimentos()
print()
gato.atributos()
print()
ave.atributos()
print()

