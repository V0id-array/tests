
def debe_tributar(edad, ingresos):
    return edad >= 16 and ingresos >= 1000

if __name__ == "__main__":
    edad = int(input("Ingrese la edad: "))
    ingresos = float(input("Ingrese los ingresos: "))
    if debe_tributar(edad, ingresos):
        print("Debe tributar")
    else:
        print("No debe tributar")
