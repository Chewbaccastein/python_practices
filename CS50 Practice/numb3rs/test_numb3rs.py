from numb3rs import validate


def test_validate():
    assert validate(r"127.0.0.1") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.5125.521.521") == False
    assert validate(r"cat") == False
    assert validate(r"1.2.3.1000") == False
    assert validate(r"1") == False
    assert validate(r"1.1") == False
    assert validate(r"1.1.1") == False
    assert validate(r"125.999.0.1") == False
    assert validate(r"0.0.999.1") == False
    assert validate(r"1.1.1.999") == False
