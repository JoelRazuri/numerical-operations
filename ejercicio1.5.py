""" 
Implementar algoritmos que resuelvan los siguientes problemas:
a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.
b) Dado un número entero 𝑛, imprimir su tabla de multiplicar.
"""

# a)
n1=int(input("Ingrese un numero:"))
n2=int(input("Ingrese otro numero:"))

suma= n1 + n2
resta= n1 - n2
division= n1 / n2
multiplicación= n1 * n2

print(f"Numero 1: {n1}, Numero 2: {n2}")
print(f"Suma: {suma}\nResta: {resta}\nDivision: {division}\nMultiplicacion: {multiplicación}")
print("")


# b)
n3=int(input("Ingrese un numero n :"))

for i in range(1,11):
    print(f"{n3} * {i} = {n3*i}")