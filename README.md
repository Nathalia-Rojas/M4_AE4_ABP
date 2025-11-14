# 🐾 Proyecto Tamagotchi en Python

## 🎯 Objetivo
Este proyecto tiene como propósito practicar **Programación Orientada a Objetos (POO)** en Python, utilizando **asociación entre clases**, **modularización** y **herencia**.  

Se simula la interacción entre una persona y su **Tamagotchi**, un personaje virtual que puede **jugar**, **comer** y **curarse** según las acciones del usuario.

---

## 🧩 Estructura del Proyecto

proyecto_tamagotchi/
│
├── persona.py # Clase Persona
├── tamagotchi.py # Clase base Tamagotchi
├── main.py # Archivo principal de ejecución
└── README.md # Descripción del proyecto


---

## 🧠 Clases Principales

### **Clase Tamagotchi**
Atributos:
- `nombre`
- `color`
- `salud`
- `felicidad`
- `energia`

Métodos:
- `jugar()`: aumenta la felicidad (+10) y reduce la salud (-5).  
- `comer()`: aumenta la felicidad (+5) y la salud (+10).  
- `curar()`: aumenta la salud (+20) y reduce la felicidad (-5).  

---

### **Clase Persona**
Atributos:
- `nombre`
- `apellido`
- `tamagotchi` (asociación con la clase Tamagotchi)

Métodos:
- `jugar_con_tamagotchi()`: llama al método `jugar()` del Tamagotchi.  
- `darle_comida()`: llama al método `comer()` del Tamagotchi.  
- `curarlo()`: llama al método `curar()` del Tamagotchi.  

---

## ⚙️ Ejemplo de uso

```python
from persona import Persona
from tamagotchi import Tamagotchi

# Crear un Tamagotchi
mi_tamagotchi = Tamagotchi("Luna", "Rosa")

# Crear una persona con su Tamagotchi
persona = Persona("Nathalia", "Rojas", mi_tamagotchi)

# Interacción
persona.darle_comida()
persona.jugar_con_tamagotchi()
persona.curarlo()

🖥️ Resultado esperado

Nathalia está dando de comer a Luna.
Luna comió y ahora tiene felicidad: 105, salud: 110
Nathalia está jugando con Luna.
Luna jugó y ahora tiene felicidad: 115, salud: 105
Nathalia está curando a Luna.
Luna fue curado. Salud: 125, Felicidad: 110
