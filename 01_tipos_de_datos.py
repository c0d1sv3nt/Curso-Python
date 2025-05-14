"""
01 - Tipos de datos:
    Python admite varios tipos de datos integrados, incluyendo:
    - Números enteros (int): 1, 10, -5
    - Números de punto flotante (float): 3.14, 2.0, -0.5
    - Cadenas (str): "Hola", 'Mundo', "Python"
    - Booleanos (bool): True, False
    - Listas (list): [1, 2, 3], ['a', 'b', 'c']
    - Tuplas (tuple): (1, 2, 3), ('x', 'y', 'z')
    - Diccionarios (dict): {'a': 1, 'b': 2}, {'nombre': 'Juan', 'edad': 30}
    - Conjuntos (set): {1, 2, 3}, {'rojo', 'verde', 'azul'}
    - NoneType (None): Representa la ausencia de un valor
"""
print("\n--- Tipos de datos ---")
# Ejercicio 1: Crea variables de cada tipo de dato y muestra su tipo.
entero = 10
flotante = 3.14
cadena = "Hola"
booleano = True
lista = [1, 2, 3]
tupla = (4, 5, 6)
diccionario = {"a": 1, "b": 2}
conjunto = {7, 8, 9}
nada = None

print(f"Variable 'entero': Valor = {entero}, Tipo = {type(entero)}")
print(f"Variable 'flotante': Valor = {flotante}, Tipo = {type(flotante)}")
print(f"Variable 'cadena': Valor = {cadena}, Tipo = {type(cadena)}")
print(f"Variable 'booleano': Valor = {booleano}, Tipo = {type(booleano)}")
print(f"Variable 'lista': Valor = {lista}, Tipo = {type(lista)}")
print(f"Variable 'tupla': Valor = {tupla}, Tipo = {type(tupla)}")
print(f"Variable 'diccionario': Valor = {diccionario}, Tipo = {type(diccionario)}")
print(f"Variable 'conjunto': Valor = {conjunto}, Tipo = {type(conjunto)}")
print(f"Variable 'nada': Valor = {nada}, Tipo = {type(nada)}")