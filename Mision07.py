#Maria Angelica Hernandez Parada
#Funciones con ciclos while

#Esta es una función para poder dividir, pero sin los signos de division, y regresa el cociente y el residuo
def dividir(dividendo,divisor):
    cociente = 0
    nB = dividendo

    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente += 1

    print(nB, "/", divisor, "=", cociente, ", sobra", dividendo)

#Esta funcion llama numeros y de esos imprime el mayor.
def encontrarMayor():
    print("Teclea una serie de números para encontrar el mayor.")
    n = 0
    numeroMayor = 0

    while n != -1:
        n = int(input("Teclea el número [-1 para salir]:"))
        if n >= numeroMayor:
            numeroMayor= n

    print("El mayor es: ", numeroMayor)
    if n == -1:
        print("No hay valor mayor")


def main():

    opcion =9
    while opcion !=3:

        print("""
    Misión 07. Ciclos While
    Autor: María Angélica Hernández Parada
    Matrícula: A01169796
    1. Calcular divisiones
    2. Calcular el Mayor
    3. Salir
    """)
        opcion =int(input("Teclea tu opción: "))
        if opcion==1:
            print("Calculando divisiones")
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            dividir(dividendo, divisor)


        elif opcion==2:
            encontrarMayor()
        elif opcion<0 or opcion>3:
            print("""ERROR, teclea 1, 2 0 3 """)

    print("Gracias por usar este programa, regresa pronto.")

main()