def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b

def calcular(operacion, a, b):
    if operacion == "suma":
        return suma(a, b)
    elif operacion == "resta":
        return resta(a, b)
    elif operacion == "multiplicacion":
        return multiplicacion(a, b)
    elif operacion == "division":
        return division(a, b)
    else:
        return "Operación no válida"

def main():
    operaciones_validas = ["suma", "resta", "multiplicacion", "division"]
    
    # Solicitar operación al usuario
    operacion = input("Ingrese la operación (suma, resta, multiplicacion, division): ").lower()
    
    # Validar que la operación sea válida
    while operacion not in operaciones_validas:
        print("Operación no válida. Por favor, ingrese una operación válida.")
        operacion = input("Ingrese la operación (suma, resta, multiplicacion, division): ").lower()
    
    # Solicitar valores de entrada
    a = float(input("Ingrese el primer valor: "))
    b = float(input("Ingrese el segundo valor: "))
    
    # Calcular el resultado
    resultado = calcular(operacion, a, b)
    
    # Imprimir el resultado
    print(f"El resultado de la operación {operacion} con los valores {a} y {b} es: {resultado}")

if __name__ == "__main__":
    main()
