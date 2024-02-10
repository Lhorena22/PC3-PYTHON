class producto:
    def __init__(self, nombre, codigo, precio, año):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"Nombre: {self.nombre}, Código: {self.codigo}, Precio: {self.precio}, Año: {self.año}"

class catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Lista de productos:")
        for producto in self.productos:
            print(producto)

    def filtrar_año(self, año):
        print(f"Productos del año {año}:")
        for producto in self.productos:
            if producto.año == año:
                print(producto)