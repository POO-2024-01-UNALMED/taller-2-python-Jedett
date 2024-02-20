class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        listaColores = ["rojo", "verde", "amarillo", "negro","blanco"]
        if color in listaColores:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        listaTipos = ["gasolina", "electrico"]
        if tipo in listaTipos:
            self.tipo = tipo
    
class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor:Motor, registro):
        Auto.cantidadCreados += 1
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        cont = 0
        for asiento in self.asientos:
            if asiento is not None:
                cont = cont + 1
        return cont
    
    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        for asiento in self.asientos:
            if asiento is not None:
                if asiento.registro != self.registro:
                    return "Las piezas no son originales"
        return "Auto original"


        