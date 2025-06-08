from working import convert
import pytest

def test_convert():
    assert convert("3 AM to 5 PM") == ("03:00 to 17:00")
    assert convert("9:00 AM to 4:00 PM") == ("09:00 to 16:00")
    assert convert("9:00 PM to 3 AM") == ("21:00 to 03:00")
    assert convert("10 AM to 4:00 PM") == ("10:00 to 16:00")


def test_value_error():
    with pytest.raises(ValueError):
        convert("13 PM to 3 AM")
    with pytest.raises(ValueError):
        convert("9 AM - 4 PM")
    with pytest.raises(ValueError):
        convert("Cat to Dog")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:66 PM")


