from funciones import *
import unittest


class TestCar(unittest.TestCase):

    def test_inicial_values(self):
        car = Car(model='Toyota', combustible=32, combustible_rendimiento=0.05)
        self.assertIs(car.combustible, 32)
        self.assertIs(car.model, 'Toyota')
        self.assertIs(car.combustible_performance, 0.05)

    def test_car_automomia(self):
        car = Car(model='Toyota', combustible=32, combustible_rendimiento=0.05)
        self.assertEqual(car.Autonomia(), 32/0.05)

    def test_car_avanzar_kilometros(self):
        car = Car(model='Toyota', combustible=0, combustible_rendimiento=0.05)
        self.assertFalse(car.AvanzarKilometros(car.Autonomia()+1))
        car.CargarCombustible(100)
        self.assertTrue(car.AvanzarKilometros(car.Autonomia()-1))

    def test_car_carga_combustible(self):
        car = Car(model='Toyota', combustible=0, combustible_rendimiento=0.05)
        car.CargarCombustible(100)
        self.assertEqual(car.combustible, 100)

    def test_car_lanza_error(self):
        self.assertRaises(TypeError, Car(model='Ford', combustible=0,
                          combustible_rendimiento=0.05))


if __name__ == '__main__':
    unittest.main()


# .assertEqual(a, b): Verifica la igualdad de ambos valores.
# .assertTrue(x): Verifica que el valor es True.
# .assertFalse(x): Verifica que el valor es False.
# .assertIs(a, b): Verifica que ambas variables son la misma (ver operador is).
# .assertIsNone(x): Verifica que el valor es None.
# .assertIn(a, b): Verifica que a pertenece al iterable b (ver operador in).
# .assertIsInstance(a, b): Verifica que a es una instancia de b
# .assertRaises(x): Verifica que se lanza una excepción.
