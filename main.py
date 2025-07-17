def ej1():
    numeros = [10, 20, 30, 40, 50]
    suma_total = 0
    for numero in numeros:
        suma_total += numero
    print("la suma total", suma_total)

def ej2():
    cadena = "Programacion python"
    contador_vocales = 0
    vocales = "aeiouAEIOU"
    for caracter in cadena:
        if caracter in vocales:
            print("cantidad de vocales:", contador_vocales)
            

def ej3():
    numero = int(input("ingresa un numero entero:"))
    for i in range(1,11):
        producto = numero * i
        print(f"{numero} x {i} = {producto}")

def ej4():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
            print("Numeros pares:", pares)
            print("cantidad de pares:", len(pares))

def ej5():
    filas = 5
    for i in range(1, filas + 1):
        for j in range(i):
            print("*", end="")
        print()


