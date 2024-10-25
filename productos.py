class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def mostrar_info(self):
        return f"Producto: {self._nombre}, Precio: Gs{self._precio:.2f}"

    def obtener_precio(self):
        return self._precio


class Ropa(Producto):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio)
        self._talla = talla
        self._tipo_tela = tipo_tela

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Talla: {self._talla}, Tipo de Tela: {self._tipo_tela}"


class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_cuello):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_cuello = tipo_cuello

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo de Cuello: {self._tipo_cuello}"


class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_pantalon):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_pantalon = tipo_pantalon

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo de Pantalón: {self._tipo_pantalon}"


class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_zapato):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_zapato = tipo_zapato

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo de Zapato: {self._tipo_zapato}"
