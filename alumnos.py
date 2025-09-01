class alumno:

    def __init__(self, saludar, hacer_examen, salir_del_salon, preguntas_examen, entregar_tarea, recibir_notas):

        self.saludar = saludar
        self.hacer_examen = hacer_examen
        self.salir_del_salon = salir_del_salon
        self.__preguntas_examen = preguntas_examen
        self.__entregar_tarea = entregar_tarea
        self.__recibir_notas = recibir_notas


    def saludo (self):
        print(f"Hola que tal, vine a {self.saludar} al profesor Daniel Espitia")

    def examen (self):
        print(f"Vamos a {self.hacer_examen} que asigno el profesor...")


    def salir (self):
        print(f"Ya es hora de {self.salir_del_salon}")

    def preguntas (self):
        print(f"Llego la hora de {self.__preguntas_examen}")
    
    def tarea (self):
        print (f"Debo {self.__entregar_tarea} el dia de hoy")
    
    def notas (self):
        print (f"El dia de hoy los alumnos recibiran sus {self.__recibir_notas}")


Yo = alumno("saludar", "hacer el examen", "salir del salon", "responder las preguntas del examen", "entregar la tarea", "calificaciones")
Yo.saludo()
Yo.examen()
Yo.salir()
print ("\n")
Yo.preguntas()
Yo.tarea()
Yo.notas()