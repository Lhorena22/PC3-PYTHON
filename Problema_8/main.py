from funciones import generar_numeros, mostrar_lista, ordenar_valores

def main():
    lista_numeros = generar_numeros()
    mostrar_lista(lista_numeros)
    ordenar_valores(lista_numeros)

if __name__ == "__main__":
    main()