from perro import Canino
from felino import Felino
from ave import Ave

perro=Canino("Pako2",4,"Oscar","pastor-aleman", 12)
gato=Felino ("Miau", 3, "Paco", "Egipcio", 4, "cortas")
ave=Ave("lorito", 1, "Paquita", "monte", 1, "normal")

perro.atributos()
perro.porcion_de_alimentos()
print()
gato.atributos()
print()
ave.atributos()
print()

