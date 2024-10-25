class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        return sum(producto.obtener_precio() for producto in self._productos)

    def mostrar_resumen(self):
        resumen = "Productos en el carrito:\n"
        for producto in self._productos:
            resumen += producto.mostrar_info() + "\n"
        resumen += f"Total a pagar: Gs{self.calcular_total():.2f}"
        return resumen
