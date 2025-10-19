# PROMPTS FOR DOCUMENTATION

## 1. GPT-5
## Prompt:
Respecto a venv, coverage y unittest, ¿cuáles de estas cosas habría que poner en el archivo requirements para subirlo a gh y que el usuario tenga todo lo necesario para usarlo?

## Answer:
Muy buena pregunta, ahí hay que separar 👇

🔹 1. venv

NO se pone en requirements.txt.

venv viene incluido con Python, no es un paquete externo.

Cada usuario crea su entorno local con python -m venv venv.

🔹 2. unittest

NO se pone en requirements.txt.

unittest también viene en la biblioteca estándar de Python.

Todos los que tengan Python ya lo tienen disponible.

🔹 3. coverage

SÍ lo ponés en requirements.txt si querés que todos puedan correr medición de cobertura.

Ejemplo:

coverage

🔹 (Opcional) pytest

Si preferís correr tests con pytest (en vez de usar python -m unittest), también lo ponés:

pytest


✅ Conclusión:
En tu requirements.txt deberían estar solo las dependencias externas.
En tu caso mínimo:

coverage


y opcionalmente

pytest


👉 Eso garantiza que cuando alguien clone el repo y haga:

pip install -r requirements.txt


ya tenga todas las librerías externas necesarias para correr tests y coverage.

¿Querés que te arme un requirements.txt y un .gitignore “listos para entregar” para tu repo de GH Classroom?

### Used with no changes
### No files were affected by this prompt. It was just to make sure the requirements.txt file was correct.