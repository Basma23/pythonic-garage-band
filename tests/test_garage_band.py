from pythonic_garage_band.garage_band import Band, Musician, Guitarist, Bassist, Drummer

def test_jimmy_is_instance_of_correct_class(jimmy):
    assert isinstance(jimmy, Guitarist)


def test_jimmy_is_instance_of_parent_class(jimmy):
    assert isinstance(jimmy, Musician)


def test_jimmy_name(jimmy):
    assert jimmy.name == 'Jimmy'


def test_jimmy_instrument(jimmy):
    assert jimmy.instrument == 'guitar'


# def test_to_list(test_data):
#     Band.create_from_data(test_data)
#     expected = 3
#     actual = Band.to_list()
#     assert len(actual) == expected



