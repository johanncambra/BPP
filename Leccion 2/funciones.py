import numbers


def AreaReactangulo(lado_a, lado_b):
    if not isinstance(lado_a, numbers.Number):
        raise TypeError("La variable lado_a no es un número.")
    if not isinstance(lado_b, numbers.Number):
        raise TypeError("La variable lado_b no es un número.")
    return lado_b*lado_a


class Car():
    def __init__(self, model: str, combustible: float, combustible_rendimiento: float):
        self.model = model
        self.combustible = combustible
        self.combustible_performance = combustible_rendimiento

        if not isinstance(self.model, str):
            raise TypeError("La variable model ingresada no es un string.")
        if not isinstance(self.combustible, numbers.Number):
            raise TypeError(
                "La variable combustible ingresada no es un número.")
        if not isinstance(self.combustible_performance, numbers.Number):
            raise TypeError("La variable combustible_rendimiento ingresada \
                            no es un número.")
        if self.combustible_performance < 0:
            raise TypeError("La variable combustible_rendimiento ingresada tiene que \
                            ser mayor que cero.")

    def Autonomia(self):
        return self.combustible/self.combustible_performance

    def AvanzarKilometros(self, kilometros):
        if not isinstance(kilometros, numbers.Number):
            raise TypeError("La variable kilometros ingresada no es \
             un número.")
        if kilometros < 0:
            raise TypeError("La variable kilometros ingresada tiene que \
                            ser mayor que cero.")
        if kilometros <= self.Autonomia():
            self.combustible -= self.Autonomia()
            return True
        else:
            return False

    def CargarCombustible(self, litros):
        if not isinstance(litros, numbers.Number):
            raise TypeError("La variable litros ingresada no es un número.")
        if litros < 0:
            raise TypeError("La variable litros ingresada tiene que \
                            ser mayor que cero.")
        self.combustible += litros
