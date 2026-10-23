# Animales Domésticos – Práctica de POO en Python

Pequeño proyecto de práctica para aprender **Programación Orientada a Objetos (POO)** en Python. Modela distintos animales domésticos (perro, gato y ave) con una clase padre y dos clases hijas que heredan de ella.

## ¿Qué se practica?

- **Clases e instancias**: la clase es el molde y cada animal creado es una instancia.
- **Atributos**: los datos de cada animal (nombre, edad, dueño, raza, peso...).
- **Métodos**: las acciones y cálculos que puede hacer cada animal.
- **Herencia**: `Felino` y `Ave` reutilizan todo lo de `Animales_Domesticos`.
- **`super()`**: llamar al constructor y a los métodos de la clase padre.
- **Sobrescritura de métodos**: `atributos()` se amplía en cada clase hija.
- **`return`**: `etapa_vida()` devuelve la etapa y `porcion_de_alimentos()` la reutiliza.

## Estructura de clases

```
Animales_Domesticos   (clase padre)
├── Felino            (añade: garras)
└── Ave               (añade: long_pico)
```

### `Animales_Domesticos`

| Elemento | Descripción |
|---|---|
| `nombre`, `edad`, `duenio`, `raza`, `peso` | Atributos comunes a todos los animales |
| `atributos()` | Muestra por consola los datos del animal |
| `cambiar_edad_mayor(edad)` | Suma años a la edad actual |
| `cambiar_edad_menor(edad)` | Resta años a la edad actual |
| `etapa_vida()` | Devuelve la etapa: `"cachorro"`, `"senior"`, `"anciano"` o `"MUY anciano"` |
| `porcion_de_alimentos()` | Calcula los gramos de comida según la etapa y el peso |

### `Felino` (hereda de `Animales_Domesticos`)

| Elemento | Descripción |
|---|---|
| `garras` | Atributo propio |
| `atributos()` | Muestra los datos del padre y además las garras |
| `estado_garras()` | Pregunta por el estado de las garras y indica si hay que cortarlas |

### `Ave` (hereda de `Animales_Domesticos`)

| Elemento | Descripción |
|---|---|
| `long_pico` | Atributo propio |
| `atributos()` | Muestra los datos del padre y además la longitud del pico |
| `longitud_pico()` | Pregunta por el estado del pico y da una recomendación |

## Ejemplo de uso

```python
perro = Animales_Domesticos("Pako2", 4, "Oscar", "pastor-aleman", 12)
gato = Felino("Miau", 3, "Paco", "Egipcio", 4, "cortas")
ave = Ave("lorito", 1, "Paquita", "monte", 1, "normal")

perro.atributos()
perro.porcion_de_alimentos()
gato.atributos()
ave.atributos()
```

Salida de `perro.atributos()`:

```
Pako2:
.edad: 4
.dueño: Oscar
.raza: pastor-aleman
.peso: 12
```

## Cómo ejecutarlo

1. Guarda el código en un archivo `.py` (por ejemplo `main.py`).
2. Desde la terminal, en la carpeta del proyecto:

```bash
python main.py
```

Necesitas tener Python 3 instalado.

## Mejoras futuras

Este proyecto es una práctica en construcción y **seguirá mejorando en todos los aspectos**: código, estructura, funcionalidades y documentación. Algunas ideas previstas:

- Corregir el caso de la edad 0 en `etapa_vida()`.
- Redondear el resultado de `porcion_de_alimentos()` para evitar decimales largos.
- Unir los bloques repetidos de `porcion_de_alimentos()`.
- Sobrescribir `etapa_vida()` en `Felino` y `Ave` con rangos de edad propios de cada especie.
- Validar los datos que introduce el usuario con `input()` para evitar errores.
- Usar los métodos `cambiar_edad_mayor()` y `cambiar_edad_menor()` en pruebas del programa.
- Seguir las convenciones de estilo de Python (PEP 8), por ejemplo en los nombres de las clases.
- Ampliar la documentación y añadir más tipos de animales.