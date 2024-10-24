#Ejercicio 2.1.5
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales
#o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus 
#ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def debe_tributar(edad, ingresos):
    return edad >= 16 and ingresos >= 1000

if __name__ == "__main__":
    edad = int(input("Ingrese la edad: "))
    ingresos = float(input("Ingrese los ingresos: "))
    if debe_tributar(edad, ingresos):
        print("Debe tributar")
    else:
        print("No debe tributar")
