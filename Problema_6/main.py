from funciones import producto, catalogo

def main():
    catalogo1 = catalogo()
    catalogo1.agregar_producto(producto("Aro", "A0012", 200, 2020))
    catalogo1.agregar_producto(producto("Muelle", "A0013", 100, 2024))
    catalogo1.agregar_producto(producto("Luces led", "A0014", 150, 2021))
    catalogo1.mostrar_productos()
    catalogo1.filtrar_año(2024)

if __name__ == "__main__":
    main()