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

Clase que representa cada uno de los jugadores. Esta clase tiene principalmente la finalidad dar la posibilidad de de gestionar los turnos, de asignarle a cada jugador un color y mantener el nombre ingresado por el usuario para una mejor experiencia. Dichos atributos pueden ser tanto asignados como modificados como obtenidos. En el juego hay 2 jugadores.

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

## Player:

### __name__

Atributo que contiene el nombre del jugador. Al inicio del juego, se les pregunta el nombre a cada uno de los jugadores para incluirlos en el juego.

### __colour__

Color de fichas que tiene asignado cada jugador. Ejemplo: Pepe juega con las fichas negras y Juan con las fichas blancas.

## Dice:

### __values__

Atributo que establece los posibles valores del dado. Para el juego siempre será un dado de 6 lados. Este atributo más que para el desarrollo del juego, en realidad sirve para los tests.

### __current_value__

Atributo que guarda en memoria el valor actual del dado. Si lo pasamos a una analogía física, luego de tirar el dado es el valor de la cara del dado que apunta hacia arriba.

## Checker:

### __checker_id__

Identificador único de cada ficha. Inicialmente pensaba asociarlo a la posición en memoria de la variable, pero luego pensé que el usuario tranquilamente podría suspender la computadora o cualquier cosa relacionada al programa, al sacarla de la suspensión y enviar el dato de vuelta a la memoria principal, el identificador de la posición de memoria podría cambiar.

### __colour__

Color asignado a cada ficha. Como dijimos antes, cada jugador tiene 15 fichas del color que le toca y únicamente puede manipular las fichas del color que tiene asignado.

## Board

### __board__

El único atributo que tiene la clase Board en realidad es un diccionario donde cada lugar posible donde se puedan poner fichas, tiene un nombre, que sería la key del diccionario. En el value de cada uno de estos campos, es una lista que dentro tiene elementos de la clase Checker.

## PointField, EatenField, HouseField

Las tres clases, las cuales son hijas de la clase Field, tienen los mismos atributos y son los siguientes:

### __name__

Nombre del campo. Desde el punto de vista del tablero se vería como las key del diccionario

### __checkers__

Lista de elementos de la clase Checker, que representará las fichas que están actualmente en el campo o punta.

### __colour__ (solo para campos especiales)

Dependiendo de si el color se asigna con B (de black) o con W (de white), se le asigna a cada jugador un campo del tipo. Además, dependiendo del color, se asigna el nombre al campo. En estos casos, __name__ depende de __colour__.

## BackgammonGame

### __turn__

Indica cuál es el jugador (asignado con el color) al cual le toca jugar. Si el turno es, por ejemplo, del blanco y se intenta mover una ficha negra, se le dice al usuario que el movimiento es inválido.

### __board__

Instancia de la clase Board. Es el tablero del juego.

### __dice1__ y __dice2__

Instancias de la clase Dice. Representan los dados principales del juego. Si los dados salen iguales durante el juego, en lugar de usar dos dados de más, simplemente se utiliza el valor del dado 1 y se "simula" como si se tuvieran en realidad 4 dados con el mismo valor.

### __player1__ y __player2__

Instancias de la clase Player. Representan a cada uno de los jugadores con su nombre y el color asignado. El primer jugador será el que juegue con las fichas negras y el segundo, el que juegue con las blancas.

### __black_checkers__ y __white_checkers__

Listas de fichas blancas y negras. Estas fichas son creadas con la clase CheckerFactory y luego los nombres de las variables para cada instancia de Checker (que esto ocurre porque ya había hecho prácticamente todo el código con los nombres de variables :/) son asignados con __setup_individual_references__.

### __move_validator__

Instancia de la clase CheckMoves. Es básicamente una sección del código que sirve como el "cerebro" o "director" que determina si los movimientos que se quieren hacer son válidos.

## CheckerFactory

No tiene atributos. Solamente se ha definido a esta clase para asignarle un método estático. Un método estático es un método que puede usarse sin necesariamente crear una instancia de una clase.

## CheckMoves

### __board__

La clase debe tener una instancia del tablero actual para coordinar lo que serían los movimientos válidos y los no válidos dependiendo del estado actual del mismo.

### __game__

La clase debe tener una instancia del juego en general, con la gestión de turnos, el tablero, las fichas y los dados principalmente.

# Decisiones de diseño relevantes

- En la interfaz gráfica, se usó puro renderizado, sin imágenes dado que no encontré ninguna forma de incluir imágenes de dados o de fichas y que me gustara cómo quedaba. Puede ser una iterfaz pesada para algunos dispositivos, pero por suerte tenemos la interfaz de líneas de comando :)
- Inicialmente, se iba a usar la posición en memoria de la instancia de la clase Checker como identificador. Eventualmente, recapacité y me di cuenta de que puede que el usuario deba suspender el programa o la propia computadora, y el swap entre memoria virtual y principal no garantiza que la ficha que necesitamos vuelva siempre (o incluso se mantenga) en la misma posición de memoria principal.
- Durante un tiempo consideré que cada campo del tablero en realidad fuera una lista del color de las fichas que tiene (si es que tiene fichas) y la cantidad de fichas que haya, pero si lo hubeiese hecho de esa forma, la clase Checker no habría tenido razón de ser.
- En lugar de hacer 30 instancias de la clase Checker (como hice en un momento), se creó la clase CkeckerFactory con el método create_checker_set que crea dichas instancias y las agrega a una lista para mayor organización y de paso, que a Pylint le guste más.
- Los múltiples métodos usados para validación de movimientos, no solamente se hicieron de la manera en la que se hicieron para que Pylint estuviera contento, sino que también garantiza un código muchísimo más organizado y mucho más acorde al diagrama de flujo.

# Excepciones y manejo de errores

En el manejo de la lógica del juego en BackgammonGame, se pueden lanzar dos excepciones posibles dentro del archivo exceptions.py. Estas excepciones pueden ser largadas cuando un color no es válido (InvalidColourError) y cuando un turno no es válido (InvalidTurnError).
Ambas excepciones toman el color o el turno respectivamente, y si no es "Black" o "White", toma cuál es el valor que fue capturado para poder detectar de mejor forma el error y facilitar cualquier debug.

# Estrategias de testing y cobertura

El objetivo de testear el código, es mantener una garantía de que el mismo funciona como se espera. Dichos tesets fueron hechos con Unittest para todos los métodos de todas las clases de core/ y la interfaz de líneas de comando.
A pesar de que si un método llama a otro y se testea únicamente el método "padre" (siempre y cuando se cause justamente ese llamado al hacer el test), ese método al que se llama queda cubierto, por cuestiones de debug, se ha intentado testear todos los métodos posibles.
Coverage es el encargado de evaluar qué porcentaje del código es testeado y cuál no.
Existen en total 56 tests del código en todo el proyecto y la cobertura es la siguiente:

```
Name                      Stmts   Miss  Cover
---------------------------------------------
cli\cli.py                  182      6    97%
core\backgammon_game.py     258      4    98%
core\board.py                56      5    91%
core\checker.py               8      0   100%
core\dice.py                 10      0   100%
core\player.py               12      0   100%
---------------------------------------------
TOTAL                       526     15    97%
```

El requisito era de una cobertira del 90% como mínimo. Como se puede ver, la cobertura total es de un 7% más que el requerido.

Para testear Dice, se usó Mock, dado que no podemos predecir el valor que saldrá en el dado al momento de tirarlo. Mock obliga a random a retornar un valor específico con la finalidad de que el test pueda quedar cubierto.

Por otro lado, para testear la interfaz de líneas de comando, se usó @patch. Esta utilidad le da un valor seleccionado por nosotros para asignarle un valor a un input para poder ejecutar el test.

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

## Player
Class that represents each of the players. The main purpose of this class is to give the game a way to manage turns, assign each player a color, and maintain the name entered by the user for a better experience. These attributes can be assigned, modified, and retrieved. There are 2 players in the game.

## Dice
Class that represents each of the dice. It contains the possible outcomes (since it's a D6, only integer values from 1 to 6 can appear) and the current value, considering it represents what in real life would be the face pointing upwards after being rolled. There are primarily 2 dice in the game. For optimization reasons, even though getting two dice with equal values is considered as if there were four dice of the same value, we simply use two. The current value of the die can be modified by a random number among the valid ones using the roll() method, which simulates a dice throw, and it can also be retrieved.

## Checker
Class that represents each game piece/token. Each player will have 15 assigned white or black checkers to play with. Each checker has an identifier and an assigned color. The identifier and color of each checker can only be retrieved using the getters. They cannot be modified or deleted, as they will always have the same values throughout the game.

## Board
Class that represents the physical board with its points and its special fields, such as the fields for the homes and the eaten pieces of each player. This class can add checkers to a field, remove them from a field, return the checkers in a specific field, and return the entire board.

### Field
This class represents each possible field on the board. The board fields can be of different types (Eaten, House, point), so the open/closed principle was applied (open for extension, closed for modification). This way, even though the game rules are already written, it's a convenient way to allow more field types to be added. This is the parent class of the following 3 classes:

### PointField (Point)
This class is a type of field that can be on the board. The points are the triangles within the main area of the board where the players' checkers interact. Each point, in the traditional game, is represented as a triangle. In total, there are 24 points on the board.

### HouseField (Home)
This class is the type of field that stores each player's checkers and determines whether they win the game or not. Once a player has all their checkers in their home quadrant, they can start bearing off their checkers under certain conditions, and the first player to successfully bear off all 15 of their checkers is the winner.

### EatenField (Eaten checkers or on the Bar)
This class is the type of field where pieces that are "eaten" by the opponent are placed. Yes, I used 'eaten' to add personality because I love Latin American idioms. In summary, when there is only one of my pieces on a point and the opponent places their piece on top of mine, they "eat" my piece and I must re-enter it. In the traditional game, they are usually placed on the central bar of the board, but both to simplify and for the "personality" of this field, I decided to place it on the side of the board, like the pieces in the homes.

### BackgammonGame (Backgammon Game Logic)
Class that manages the general game logic. It groups turn management, dice values, moves, the initial placement of checkers on the points, and their movements. To comply with the SRP principle, two classes were created for the initial setup of the checkers and move validation.

### CheckerFactory
With the purpose of not creating 30 instances of the Checker class in BackgammonGame, this task is delegated to CheckerFactory. Initially, these instances were created one by one as an attribute of the BackgammonGame class, until I realized that neither Pylint nor I liked it, and besides, it was horribly implemented. This is why this task is delegated to this class.

### CheckMoves
The task of checking if moves are valid before making them is actually quite a heavy task and should not be the responsibility of BackgammonGame. This class implements several methods based on the game rules to validate whether the move being attempted is valid and according to the rules or not.

# Justification of attributes

## Player:
### __name__
Attribute that contains the player's name. At the start of the game, each player is asked for their name to include them in the game.

### __colour__
The color of the checkers assigned to each player. Example: Pepe plays with the black checkers and Juan with the white checkers.

## Dice:
### __values__
Attribute that defines the possible values of the die. For the game, it will always be a 6-sided die. This attribute is more useful for testing than for the actual game development.

### __current_value__
Attribute that stores the current value of the die in memory. Using a physical analogy, after rolling the die, this is the value on the face pointing upwards.

## Checker:
### __checker_id__
Unique identifier for each checker. Initially, I considered associating it with the memory address of the variable, but then I thought that the user could easily put the computer to sleep or anything related to the program; when resuming from sleep and sending the data back to main memory, the memory address identifier could change.

### __colour__
Color assigned to each checker. As mentioned before, each player has 15 checkers of their assigned color and can only manipulate the checkers of the color assigned to them.

## Board
### __board__
The only attribute the Board class actually has is a dictionary where each possible location where checkers can be placed has a name, which would be the key of the dictionary. The value for each of these fields is a list containing elements of the Checker class.

## PointField, EatenField, HouseField
These three classes, which are children of the Field class, have the same attributes, which are as follows:

### __name__
Name of the field. From the board's perspective, it would be seen as the dictionary keys.

### __checkers__
List of elements of the Checker class, representing the checkers currently in the field or point.

### __colour__ (only for special fields)
Depending on whether the color is assigned as 'B' (for black) or 'W' (for white), each player is assigned a field of that type. Furthermore, depending on the color, the name is assigned to the field. In these cases, __name__ depends on __colour__.

## BackgammonGame
### __turn__
Indicates which player (assigned by color) has the current turn. If it's the white player's turn, for example, and an attempt is made to move a black checker, the user is told that the move is invalid.

### __board__
Instance of the Board class. It is the game board.

### __dice1__ and __dice2__
Instances of the Dice class. They represent the main dice of the game. If the dice show the same value during the game, instead of using two extra dice, the value of dice1 is simply used and it's "simulated" as if there were actually 4 dice with the same value.

### __player1__ and __player2__
Instances of the Player class. They represent each of the players with their name and assigned color. The first player will be the one playing with the black checkers and the second, the one playing with the white checkers.

### __black_checkers__ and __white_checkers__
Lists of black and white checkers. These checkers are created using the CheckerFactory class, and then the variable names for each Checker instance (this happens because I had already written almost all the code with the variable names :/) are assigned using __setup_individual_references__.

### __move_validator__
Instance of the CheckMoves class. It is basically a section of code that serves as the "brain" or "director" that determines whether the moves you want to make are valid.

## CheckerFactory
Has no attributes. This class was defined solely to assign a static method to it. A static method is a method that can be used without necessarily creating an instance of a class.

## CheckMoves
### __board__
The class must have an instance of the current board to coordinate what would be valid and invalid moves depending on its current state.

### __game__
The class must have an instance of the game in general, with the management of turns, the board, the checkers, and the dice primarily.

# Relevant design decisions

- In the graphical interface, pure rendering was used, without images, since I couldn't find a way to include images of dice or checkers that I liked how it looked. It might be a heavy interface for some devices, but luckily we have the command-line interface :)
- Initially, the memory address of the Checker class instance was going to be used as an identifier. Eventually, I reconsidered and realized that the user might need to suspend the program or the computer itself, and the swap between virtual and main memory does not guarantee that the checker we need will always return to (or even remain in) the same main memory location.
- For a while, I considered making each board field simply a list containing the color of the checkers it holds (if it has any) and the number of checkers present. However, if I had done it that way, the Checker class would have had no reason to exist.
- Instead of creating 30 instances of the Checker class directly (as I did at one point), the CheckerFactory class was created with the create_checker_set method. This method creates those instances and adds them to a list for better organization, and also to make Pylint happier.
- The multiple methods used for move validation were implemented not only to keep Pylint satisfied but also to ensure much more organized code that better follows the flow diagram.

# Exceptions and error handling

In the management of the game logic in BackgammonGame, two possible exceptions can be raised within the exceptions.py file. These exceptions can be thrown when a color is not valid (InvalidColourError) and when a turn is not valid (InvalidTurnError).
Both exceptions take the color or the turn respectively, and if it is not "Black" or "White", they capture the value that was received to better detect the error and facilitate debugging.

# Testing and coverage strategies

The goal of testing the code is to maintain a guarantee that it functions as expected. These tests were written using Unittest for all methods of all classes in core/ and the command-line interface.

Although if one method calls another and only the "parent" method is tested (provided that call is specifically triggered during the test), the called method becomes covered. However, for debugging purposes, we have attempted to test all possible methods.

Coverage is responsible for evaluating what percentage of the code is tested and what is not.
There are a total of 56 tests for the code throughout the project, and the coverage is as follows:

```
Name                      Stmts   Miss  Cover
---------------------------------------------
cli\cli.py                  182      6    97%
core\backgammon_game.py     258      4    98%
core\board.py                56      5    91%
core\checker.py               8      0   100%
core\dice.py                 10      0   100%
core\player.py               12      0   100%
---------------------------------------------
TOTAL                       526     15    97%
```

The requirement was a minimum coverage of 90%. As can be seen, the total coverage is 7% higher than required.

To test Dice, Mock was used, since we cannot predict the value that will appear on the die when rolled. Mock forces random to return a specific value so that the test can be covered.

On the other hand, to test the command-line interface, @patch was used. This utility allows us to assign a value of our choice to an input in order to execute the test.

# References to SOLID requirements and how they are met
# Annexes: UML diagrams
