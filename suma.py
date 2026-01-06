# Programa que suma dos o más números

numeros = input("Introduce los números separados por espacios: ")
lista = numeros.split()  # separa los números
suma = 0

for n in lista:
    suma += int(n)

print("La suma es:", suma)


