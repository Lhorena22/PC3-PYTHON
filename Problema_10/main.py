from funciones import circulo, rectangulo
import math

def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    circulo_1 = circulo(radio)  
    area = circulo_1.calculo_area()
    print("El área del círculo es:", area)

def calcular_area_rectangulo():
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    rectangulo_1 = rectangulo(largo, ancho) 
    area = rectangulo_1.calculo_area()
    print("El área del rectángulo es:", area)

def calcular_area_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = pow(lado,2)
    print("El área del cuadrado es:", area)

def mostrar_menu():
    print("")
    print("Menú:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            calcular_area_circulo()
        elif opcion == "2":
            calcular_area_rectangulo()
        elif opcion == "3":
            calcular_area_cuadrado()
        elif opcion == "4":
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()