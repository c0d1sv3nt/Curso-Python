"""
10 - Funciones:
    Las funciones son bloques de código reutilizables.  Pueden
    tomar argumentos y devolver valores.
"""
print("\n--- Funciones ---")
# Ejercicio 10: Define y llama una función.
def saludar(nombre="Amigo"):
    """
    Esta función saluda a la persona proporcionada.

    Parámetros:
        nombre (str, opcional): El nombre de la persona a saludar.
            Por defecto es "Amigo".
    """
    print(f"Hola, {nombre}!")
saludar("Juan")
saludar()