from abc import ABC, abstractmethod

def requiere_mana(cantidad_mana):
    def decorador(metodo):
        def envoltura(self, objetivo):
            if self.mana >= cantidad_mana:
                self.mana -= cantidad_mana
                print(f"{self.nombre} gasta {cantidad_mana} de maná.")
                return metodo(self, objetivo)
            else:
                print(f"¡Maná insuficiente para lanzar el hechizo! Se requieren {cantidad_mana}.")
        return envoltura
    return decorador

class Personaje(ABC):
    def __init__(self, nombre, vida, mana):
        self._nombre = nombre
        self._vida = vida
        self._mana = mana

    @property
    def nombre(self):
        return self._nombre

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
        else:
            self._vida = valor

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, valor):
        if valor < 0:
            self._mana = 0
        else:
            self._mana = valor

    @abstractmethod
    def atacar(self, objetivo):
        pass

    def esta_vivo(self):
        return self.vida > 0

    def recibir_dano(self, dano):
        self.vida -= dano
        print(f"{self.nombre} recibe {dano} de daño. Vida restante: {self.vida}")

class Guerrero(Personaje):
    def __init__(self, nombre, vida, mana, dano_ataque_fisico):
        super().__init__(nombre, vida, mana)
        self._dano_ataque_fisico = dano_ataque_fisico

    def atacar(self, objetivo):
        print(f"{self.nombre} realiza un ataque físico a {objetivo.nombre}.")
        objetivo.recibir_dano(self._dano_ataque_fisico)

class Mago(Personaje):
    def __init__(self, nombre, vida, mana, dano_ataque_magico):
        super().__init__(nombre, vida, mana)
        self._dano_ataque_magico = dano_ataque_magico

    @requiere_mana(cantidad_mana=10)
    def atacar(self, objetivo):
        print(f"{self.nombre} lanza un hechizo a {objetivo.nombre}.")
        objetivo.recibir_dano(self._dano_ataque_magico)

print("¡Comienza la batalla!")
guerrero_1 = Guerrero(nombre="Khalid", vida=100, mana=0, dano_ataque_fisico=20)
mago_1 = Mago(nombre="Jay", vida=80, mana=30, dano_ataque_magico=25)

print("\nEstado inicial")
print(f"{guerrero_1.nombre}: {guerrero_1.vida} de vida")
print(f"{mago_1.nombre}: {mago_1.vida} de vida y {mago_1.mana} de maná")

print("\nTurno 1")
guerrero_1.atacar(mago_1)

print("\nTurno 2")
mago_1.atacar(guerrero_1)

print("\nTurno 3: Mago ataca de nuevo (maná restante: 20)")
mago_1.atacar(guerrero_1)

print("\nTurno 4: Mago ataca de nuevo (maná restante: 10)")
mago_1.atacar(guerrero_1)

print("\nTurno 5: Mago ataca de nuevo (maná restante: 0)")
mago_1.atacar(guerrero_1)

print("\nFin de la batalla")
print(f"Estado final de {guerrero_1.nombre}: {guerrero_1.vida} de vida")
print(f"Estado final de {mago_1.nombre}: {mago_1.vida} de vida y {mago_1.mana} de maná")
