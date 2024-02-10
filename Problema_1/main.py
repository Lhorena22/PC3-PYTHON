from funciones import porcentaje

def main():
    while True:
        fraccion = input("Introduce una fracción en formato X/Y: ")
        resultado = porcentaje(fraccion)
        if resultado:
            print("La cantidad de combustible en el tanque es:", resultado)
            break

if __name__ == "__main__":
    main()