class Producto:
    def __init__(self, nombre, precio, codigo_producto):
        self._nombre = nombre
        self._precio = precio
        self.__codigo_producto = codigo_producto

    @property
    def codigo_producto(self):
        return self.__codigo_producto

    def mostrar_informacion(self):
        return f"Producto: {self._nombre}, Precio: ${self._precio:.2f}, Codigo: {self.codigo_producto}"

class Electronico(Producto):
    def __init__(self, nombre, precio, codigo_producto, marca):
        super().__init__(nombre, precio, codigo_producto)
        self.marca = marca

    def mostrar_informacion(self):
        informacion_base = super().mostrar_informacion()
        return f"{informacion_base}, Marca: {self.marca}"

class Ropa(Producto):
    def __init__(self, nombre, precio, codigo_producto, talla):
        super().__init__(nombre, precio, codigo_producto)
        self.talla = talla

    def mostrar_informacion(self):
        informacion_base = super().mostrar_informacion()
        return f"{informacion_base}, Talla: {self.talla}"

xbox_series_s = Electronico("Xbox Series S", 299.99, "CON-001", "Microsoft")
playstation_5 = Electronico("Playstation 5", 499.99, "CON-002", "Sony")
camiseta_deportiva = Ropa("Camiseta Deportiva", 25.50, "ROP-001", "L")

print(xbox_series_s.mostrar_informacion())
print(playstation_5.mostrar_informacion())
print(camiseta_deportiva.mostrar_informacion())
