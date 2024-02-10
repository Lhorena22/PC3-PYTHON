from funciones import circulo

def main():
    radio = float(input("Introduce el radio del círculo: "))
    circulo_1 = circulo(radio)
    area = circulo_1.calculo_area()
    print("El área del círculo es:", area)

if __name__ == "__main__":
    main()