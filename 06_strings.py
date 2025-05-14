"""
06 - Strings:
    Las cadenas son secuencias de caracteres.  Python proporciona
    muchos métodos para manipular cadenas.
"""
print("\n--- Strings ---")
# Ejercicio 6: Manipula cadenas de texto.
texto = "Python es un lenguaje poderoso"
longitud = len(texto)
mayusculas = texto.upper()
minusculas = texto.lower()
reemplazo = texto.replace("poderoso", "increíble")
subcadena = texto[0:6]
print(f"Texto: {texto}")
print(f"Longitud: {longitud}")
print(f"Mayúsculas: {mayusculas}")
print(f"Minúsculas: {minusculas}")
print(f"Reemplazo: {reemplazo}")
print(f"Subcadena: {subcadena}")