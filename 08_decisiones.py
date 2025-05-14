"""
08 - Decisiones:
    Las estructuras condicionales (if, elif, else) se utilizan para
    ejecutar diferentes bloques de código basados en condiciones.
"""
print("\n--- Decisiones ---")
# Ejercicio 8: Usa estructuras condicionales.
nota = int(input("Ingrese su nota (0-100): "))
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bien")
elif nota >= 70:
    print("Bien")
elif nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")