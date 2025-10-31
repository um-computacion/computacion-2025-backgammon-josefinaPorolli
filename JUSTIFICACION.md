# BACKGAMMON - 2025

Este proyecto final de la materia Computación I se basa en la creación de un software que simule el juego de mesa Backgammon.

# Datos del Alumno
**Nombre y apellido**: Josefina Porolli Serpa
**Carrera**: Ingeniería en Informática
**Año**: 2025

# Resumen del diseño general

El proyecto consiste en un juego Backgammon desarrollado en Python.
Algunas partes importantes a tener en cuenta respecto a este proyecto son:
- El proyecto está estrucutado estrictamente con clases cumpliendo (o mejor dicho, intentando cumplir, perdón :/) con los principios SOLID.
- Unittest para testeo de funcionamiento de los métodos de las clases usadas y la interfaz CLI.
- Coverage para reportes sobre dichos tests hechos con Unittest.
- Pylint para testeo de calidad del código
- Github action

Para resumirlo muy brevemente, existen 4 clases que serían como "las partes de una mesa" para el armado del juego: board (tablero), checkers (fichas), dice (dado) y player (jugador). Luego, está la clase BackgammonGame que unifica dichas clases para gestionar la lógica del juego: inicialización, manejo de turnos, validación de movimientos y movimientos en sí, entre otros aspectos. Esta última es la única clase que se comunica de forma directa con las interfaces, de las cuales existen una de consola (CLI) y una gráfica con Pygame (GUI).

## Estructura básica del proyecto

/backgammon/
├── core/           → clases para la lógica del juego
├── cli/            → interfaz de consola
├── pygame_ui/      → interfaz gráfica
├── tests/          → tests
└── requirements.txt

Es necesario tener en cuenta el archivo requirements.txt es sumamente importante al momento de usar el juego la primera vez, ya que el mismo tiene todo lo que debe ser obligatoriamente instalado para poder ejecutar el código.

# Justificación de las clases elegidas

## Player (Jugador)

Clase que representa cada uno de los jugadores. Esta clase tiene principalmente la finalidad de gestionar los turnos, de asignarle a cada jugador un color y mantener el nombre ingresado por el usuario para una mejor experiencia. Dichos atributos pueden ser tanto asignados como modificados como obtenidos. En el juego hay 2 jugadores.

## Dice (dado)

Clase que representa cada uno de los dados. El mismo contiene los valores que pueden salir (como es un D6, solamente pueden salir valores enteros del 1 al 6) y el valor actual, considerando que representa lo que en la vida real sería el lado que apunta hacia arriba luego de ser tirado. En el juego hay 2 dados principalmente. Por cuestiones de optimización, a pesar de que si se obtienen 2 dados con valores iguales, se considera como si hubiese 4 dados del mismo valor, simplemente tomamos 2. El valor actual del dado puede ser modificado por un número aleatorio entre los válidos con el método roll(), el cual simula una tirada de dados, y también peude ser obtenido.

## Checker (ficha)

Clase que representa cada ficha del juego. Cada jugador tendrá 15 fichas asignadas blancas o negras para jugar. Cada ficha tiene un identificador y un color asignado. El identificador y el color de cada ficha únicamente pueden ser obtenidos con los getters. No pueden ser modificados ni eliminados, dado que a lo largo del juego siempre tendrán los mismos valores.

## Board (tablero)

Clase que representa el tablero físico con sus puntas y sus campos especiales, como los campos para las casas y las fichas comidas de cada jugador. Esta clase puede agregar fichas a un campo, eliminarlas de un campo, retornar las fichas en un campo específico y retornar el tablero completo.

### Field (campo)

Esta clase representa cada campo posible dentro del tablero. Los campos del tablero pueden ser de distintos tipos (Eaten, House, point), por lo que se aplicó el principio de abierto para extensión y cerrado para modificación. De esta forma, a pesar de que las reglas del juego ya están escritas, es una forma cómoda de permitir que se agreguen más tipos de campos. Esta es la clase padre de las siguientes 3 clases que siguen:

### PointField (punta)

Esta clase es un tipo de campo que se puede tener en el tablero. Las puntas son los triángulos dentro de la zona principal del tablero donde hay cruce entre las fichas de los jugadores. Cada punta, en el juego tradicional, es representada como un triángulo. En total, hay 24 puntas en el tablero.

### HouseField (casa)

Esta clase es el tipo de campo que guarda las fichas de cada jugador y que determina si gana el juego o no. Una vez que el jugador tiene todas las fichas en su cuadrante, puede comenzar a meter las fichas a su casa con ciertas condiciones, y el primer jugador que logre meter sus 15 fichas a la casa, es el ganador.

### EatenField (fichas comidas o sobre la barra central del tablero)

Esta clase es el tipo de campo donde se ponen las fichas que son "comidas" por el oponente. Sí, le puse eaten para meterle personalidad porque me encantan los modismos latinoamericanos. En resumen, cuando hay una sola ficha mía en una punta y el oponente pone su ficha sobre la mía, me "come" la ficha y yo debo reingresarla. En el juego tradicional, suelen ponerse sobre la línea central del tablero, pero tanto para simplificar como por el tema de "personalidad" de dicho campo, decidí ponerlo al costado del tablero, como las fichas en las casas.

## BackgammonGame (Juego backgammon para lógica)

Clase que gestiona la lógica general del juego. Agrupa la gestión de turnos, los valores de los dados, los movimientos, el seteo inicial de fichas en las puntas y los movimientos de las mismas. Para cumplir con el principio SRP, se crearon dos clases para el seteo inicial de las fichas y el chequeo de movimientos.

### CheckerFactory (fábrica de fichas)

Con la finalidad de no crear 30 instancias de la clase Checker en BackgammonGame, esta tarea se la delega a CheckerFactory. En un principio, estas instancias se creaban una por una como atributo de la clase BackgammonGame, hasta que me di cuenta de que ni a Pylint ni a mí nos gustaba, y además estaba horriblemente implementado. Por esto es que se le delega dicha tarea a esta clase.

### CheckMoves

La tarea de chequear si los movimientos son válidos antes de hacerlos, en realidad es una tarea bastante pesada y no debería ser responsabilidad de BackgammonGame. Esta clase implementa varios métodos basados en el reglamento del juego para validar si el movimiento que se está intentando hacer es válido y acorde a las reglas o no.

# Justificación de atributos
# Decisiones de diseño relevantes
# Excepciones y manejo de errores
# Estrategias de testing y cobertura
# Referencias a requisitos SOLID y cómo se cumplen
# Anexos: diagramas UML

---

# Summary of the general design

The project consists in a Backgammon computer game.
Some parts we need to take into account regarding this project are_
- It is structured strictly with classes fulfilling (or at least trying to fulfill, sorry :/) SOLID principles.
- Unittest was used for testing the functionalities in classes and CLI.
- Coverage for reporting about tests.
- Pylint for code quality tracking.
- Github action

To summarize it briefly, there are 4 classes that are "the parts of a table" for the structure of the game: board, checkers, dice and player. Then, there is a class called BackgammonGame that unifies the other 4 classes in order to manage the logic of the game: initialization, turn handling, move validations, moves themselves, and other aspects. This class is the only class that communicates directly with the interfaces, of which there is a command line interface (CLI) and a graphic interface with pygame (GUI).

## Basic structure of the project:

/backgammon/
├── core/           → classes for game logic
├── cli/            → command line interface
├── pygame_ui/      → graphic interface
├── tests/          → tests
└── requirements.txt

Take into consideration that requirements.txt file is truly important when using the game the first time, since it has everything that must be installed in order to be able to execute the code.

# Justification of the chosen classes
# Justification of attributes
# Relevant design decisions
# Exceptions and error handling
# Testing and coverage strategies
# References to SOLID requirements and how they are met
# Annexes: UML diagrams
