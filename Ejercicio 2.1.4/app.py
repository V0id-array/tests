#Ejercicio 2.1.4
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
def es_par(numero):
    return numero % 2 == 0

def main():
    try:
        numero = int(input("Introduce un número entero: "))
        if es_par(numero):
            print(f"{numero} es par.")
        else:
            print(f"{numero} es impar.")
    except ValueError:
        print("Error: Debes introducir un número entero válido.")

if __name__ == "__main__":
    main()
