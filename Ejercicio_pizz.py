class Ingrediente:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pizza:
    def __init__(self, nombre, tamano, precio_base):
        self.nombre = nombre
        self.tamano = tamano
        self.precio_base = precio_base
        self.ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def calcular_precio_total(self):
        precio_ingredientes = sum(ingrediente.precio for ingrediente in self.ingredientes)
        return self.precio_base + precio_ingredientes

class Pedido:
    def __init__(self, numero_pedido):
        self.numero_pedido = numero_pedido
        self.pizzas = []

    def agregar_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calcular_total_pedido(self):
        return sum(pizza.calcular_precio_total() for pizza in self.pizzas)

    def mostrar_resumen_pedido(self):
        print(f"Resumen del Pedido{self.numero_pedido} ---")
        total_pedido = 0
        for i, pizza in enumerate(self.pizzas, 1):
            precio_pizza = pizza.calcular_precio_total()
            total_pedido += precio_pizza
            ingredientes = ", ".join(ingrediente.nombre for ingrediente in pizza.ingredientes)
            
            print(f"{i}. Pizza '{pizza.nombre}' ({pizza.tamano})")
            print(f"  Ingredientes: {ingredientes}")
            print(f"  Precio: ${precio_pizza:.2f}")
        
        print("-" * 30)
        print(f"Total del Pedido: ${total_pedido:.2f}")
        print("-" * 30)

queso = Ingrediente("queso", 1.50)
pepperoni = Ingrediente("pepperoni", 2.00)
tomate = Ingrediente("tomate", 0.75)
cebolla = Ingrediente("cebolla", 0.50)

mi_pizza = Pizza("Pizza de Pepperoni", "grande", 10.00)
mi_pizza.agregar_ingrediente(queso)
mi_pizza.agregar_ingrediente(pepperoni)
mi_pizza.agregar_ingrediente(tomate)

otra_pizza = Pizza("Pizza Vegetariana", "mediana", 8.00)
otra_pizza.agregar_ingrediente(queso)
otra_pizza.agregar_ingrediente(tomate)
otra_pizza.agregar_ingrediente(cebolla)

mi_pedido = Pedido(numero_pedido=1)
mi_pedido.agregar_pizza(mi_pizza)
mi_pedido.agregar_pizza(otra_pizza)

mi_pedido.mostrar_resumen_pedido()
