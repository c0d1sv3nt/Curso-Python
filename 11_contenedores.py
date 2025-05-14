"""
11 - Contenedores:
    Python proporciona varios tipos de datos para almacenar
    colecciones de elementos:
    - Listas: Mutables, ordenadas, permiten duplicados.
    - Tuplas: Inmutables, ordenadas, permiten duplicados.
    - Diccionarios: Mutables, no ordenados (a partir de Python 3.7),
      almacenan pares clave-valor.
"""
print("\n--- Contenedores ---")
# Ejercicio 11: Trabaja con listas, tuplas y diccionarios.
print("\nListas:")
frutas = ["manzana", "banana", "cereza"]
print(frutas)
frutas.append("naranja")
print(frutas)
print(frutas[1])

print("\nTuplas:")
colores = ("rojo", "verde", "azul")
print(colores)
print(colores[0])

print("\nDiccionarios:")
persona = {"nombre": "Ana", "edad": 25}
print(persona)
persona["profesion"] = "Ingeniera"
print(persona)
print(persona["nombre"])
