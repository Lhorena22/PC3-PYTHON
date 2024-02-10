from funciones import rectangulo

def main():
    largo = float(input("Introduce el largo del rectángulo: "))
    ancho = float(input("Introduce el ancho del rectángulo: "))
    rectangulo_1 = rectangulo(largo, ancho)
    area = rectangulo_1.calculo_area()
    print("El área del rectángulo es:", area)

if __name__ == "__main__":
    main()