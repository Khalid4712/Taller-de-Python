class Plato:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def mostrar_descripcion(self):
        return f"{self._nombre} - ${self._precio:.2f}"

class Pizza(Plato):
    def __init__(self, nombre, precio, ingredientes, tamano):
        super().__init__(nombre, precio)
        self._ingredientes = ingredientes
        self._tamano = tamano

    def mostrar_descripcion(self):
        descripcion_plato = super().mostrar_descripcion()
        return f"{descripcion_plato}, Ingredientes: {', '.join(self._ingredientes)}, Tamano: {self._tamano}"

plato_hamburguesa = Plato("Hamburguesa Junior", 8.99)
pizza_pepperoni = Pizza("Pizza de Pepperoni", 15.00, ["queso", "pepperoni", "tomate"], "familiar")

print("Menu del Restaurante:")
print(plato_hamburguesa.mostrar_descripcion())
print(pizza_pepperoni.mostrar_descripcion())
