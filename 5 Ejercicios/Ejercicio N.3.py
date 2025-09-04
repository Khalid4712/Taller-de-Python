class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad
    
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau Guau"

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        return "Miau"

mi_perro = Perro("Firulais", 3, "Marron")
mi_gato = Gato("ErMichi", 5, "Blanco")

print(f"{mi_perro.nombre} tiene {mi_perro.edad} anos y es de raza {mi_perro.raza}.")
print(f"Hace un sonido: {mi_perro.hacer_sonido()}")

print("-" * 30)

print(f"{mi_gato.nombre} tiene {mi_gato.edad} anos y es de color {mi_gato.color}.")
print(f"Hace un sonido: {mi_gato.hacer_sonido()}")
