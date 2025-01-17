num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
if (num1 == num2):
    print ("Los numeros son iguales")
else:
    if (num1 < num2):
        print (num2," es mayor que ",num1)
    else:
        print(num1," es mayor que ",num2)