import random

def generar_numeros():
    return [random.randint(0, 100) for _ in range(20)]

def mostrar_lista(lista):
    print("Lista obtenida:")
    print(lista)

def ordenar_valores(lista):
    lista_ordenada = sorted(lista)
    print("Valores de la lista ordenados:")
    print(lista_ordenada)