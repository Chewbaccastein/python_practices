from plates import is_valid


def test_is_valid():
    assert is_valid("123456") == False
    assert is_valid("CS50") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGHI") == False
    assert is_valid("50ABCD") == False
    assert is_valid("AB_50") == False
    assert is_valid("AB22AS") == False
    assert is_valid("AB0044") == False
