from pythonic_garage_band.garage_band import Band, Musician, Guitarist, Bassist, Drummer


def test_one():
    jwan = Guitarist('Jwan', 'Guitarist')
    actual = "I'm Jwan, and I play Guitar"
    expected = jwan.__str__()
    assert expected == actual

def test_two():
    jwan = Guitarist('Jwan', 'Guitarist')
    actual = "guitar"
    expected = jwan.get_instrument()
    assert expected == actual

def test_three():
    jwan = Guitarist('Jwan', 'Guitarist')
    actual = "tun tun ttattatun"
    expected = jwan.play_solo()
    assert expected == actual