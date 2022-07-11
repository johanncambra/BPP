from funciones import *
import pytest


def test_control_non_number():
    with pytest.raises(TypeError):
        AreaReactangulo('f')


def test_AreaReactangulo():
    assert AreaReactangulo(2, 2) == 4


def test_car_inicial_values():
    carro = Car(model='Toyota', combustible=32, combustible_rendimiento=0.05)
    assert carro.combustible == 32
    assert carro.model == 'Toyota'
    assert carro.combustible_performance == 0.05


def test_car_automomia():
    carro = Car(model='Toyota', combustible=32, combustible_rendimiento=0.05)
    assert carro.Autonomia() == 32/0.05


def test_car_avanzar_kilometros():
    carro = Car(model='Toyota', combustible=32, combustible_rendimiento=0.05)
    assert carro.AvanzarKilometros(carro.Autonomia()+10) == False
