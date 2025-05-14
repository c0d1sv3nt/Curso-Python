"""
09 - Bucles:
    Los bucles se utilizan para ejecutar un bloque de código
    repetidamente.  Python proporciona dos tipos principales
    de bucles:
    - for: Itera sobre una secuencia (lista, tupla, rango, etc.)
    - while: Ejecuta un bloque de código mientras una condición
      sea verdadera.
"""
print("\n--- Bucles ---")
# Ejercicio 9: Usa bucles for y while.
print("Bucle for:")
for i in range(5):
    print(i)
print("\nBucle while:")
contador = 0
while contador < 5:
    print(contador)
    contador += 1