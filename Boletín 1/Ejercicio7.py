def suma (num1,num2):
    return num1+num2

def resultadosuma():
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    resultado = suma (num1,num2)
    print("La suma de",num1, "y" ,num2, "es" ,resultado)

resultadosuma()