from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo, costo_base):
        self.marca = marca
        self.modelo = modelo
        self._costo_base = costo_base

    @abstractmethod
    def calcular_costo_mantenimiento(self):
        pass

    def mostrar_info(self):
        costo_mantenimiento = self.calcular_costo_mantenimiento()
        print(f"Informacion del Vehiculo:")
        print(f"  Marca: {self.marca}")
        print(f"  Modelo: {self.modelo}")
        print(f"  Costo de Mantenimiento: ${costo_mantenimiento:.2f}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, costo_base, numero_puertas):
        super().__init__(marca, modelo, costo_base)
        self.numero_puertas = numero_puertas

    def calcular_costo_mantenimiento(self):
        return self._costo_base * self.numero_puertas

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, costo_base, cilindrada_cc):
        super().__init__(marca, modelo, costo_base)
        self.cilindrada_cc = cilindrada_cc

    def calcular_costo_mantenimiento(self):
        return self._costo_base + (self.cilindrada_cc * 0.5)

automovil = Automovil("Honda", "Civic", 150.00, 4)
motocicleta = Motocicleta("Yamaha", "MT-07", 80.00, 689)

print("Calculo de Mantenimiento de Vehiculos")
print("\nAutomovil:")
automovil.mostrar_info()
print("\nMotocicleta:")
motocicleta.mostrar_info()
