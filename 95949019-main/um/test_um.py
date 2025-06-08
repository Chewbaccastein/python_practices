from um import count

def test_count():
    assert count("Hi there") == 0
    assert count("um Hi") == 1
    assert count("Yummy!") == 0
    assert count("Heloow woumld um my goodness, um Hi") == 2
    assert count("UM, um, uM, Um, hi") == 4
