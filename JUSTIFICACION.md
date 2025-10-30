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
- Unittest para testeo de funcionamiento de los métodos de las clases usadas.
- Coverage para reportes sobre dichos tests hechos con Unittest.
- Pylint para testeo de calidad del código
- Github action

Para resumirlo muy brevemente, existen 4 clases que serían como "las partes de una mesa" para el armado del juego: board (tablero), checkers (fichas), dice (dado) y player (jugador). Luego, está la clase BackgammonGame que unifica dichas clases para gestionar la lógica del juego: inicialización, manejo de turnos, validación de moviientos y movimientos en sí, entre otros aspectos. Esta última es la única clase que se comunica de forma directa con las interfaces, de las cuales existen una de consola (CLI) y una gráfica con Pygame (GUI).

## Estructura básica del proyecto

/backgammon/
├── core/           → clases para la lógica del juego
├── cli/            → interfaz de consola
├── pygame_ui/      → interfaz gráfica
├── tests/          → tests
└── requirements.txt

Es necesario tener en cuenta el archivo requirements.txt es sumamente importante al momento de usar el juego las primeras veces, ya que el mismo tiene todo lo que debe ser obligatoriamente instalado para poder ejecutar el código.

# Justificación de las clases elegidas
# Justificación de atributos
# Decisiones de diseño relevantes
# Excepciones y manejo de errores
# Estrategias de testing y cobertura
# Referencias a requisitos SOLID y cómo se cumplen
# Anexos: diagramas UML

---

# Summary of the general design
# Justification of the chosen classes
# Justification of attributes
# Relevant design decisions
# Exceptions and error handling
# Testing and coverage strategies
# References to SOLID requirements and how they are met
# Annexes: UML diagrams
