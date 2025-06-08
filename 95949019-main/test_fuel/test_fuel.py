import fuel
import pytest

def test_convert():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("5/5") == 100
    assert fuel.convert("1/5") == 20
    assert fuel.convert("1/100") == 1

def test_convert_value_error():
    with pytest.raises(ValueError):
        fuel.convert("Cat")
    with pytest.raises(ValueError):
        fuel.convert("5/4")

def test_convert_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("3/0")


def test_gauge():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(50) == "50%"

