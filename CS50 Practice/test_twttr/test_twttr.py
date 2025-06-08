import twttr

def test_shorten():
    assert twttr.shorten("Hello") == ("Hll")
    assert twttr.shorten("What's up?") == ("Wht's p?")
    assert twttr.shorten("Goodbye World") == ("Gdby Wrld")
    assert twttr.shorten("CS50") == ("CS50")
    assert twttr.shorten("Oh My Good!") == ("h My Gd!")
