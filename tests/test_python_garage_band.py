
from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band,Musician,Guitarist,Drummer,Bassist
import pytest


def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture

def prep_data():

    shela =Guitarist("ahmad SH")
    emadooov = Bassist("emad Z3")
    jhon = Drummer("jhon")

    return {'shela':shela,'emadooov':emadooov,'jhon':jhon}

def test_repr(prep_data):
    expected = 'Bassist:emad Z3 '
    actual = prep_data['emadooov'].__repr__()
    assert actual == expected

def test_str(prep_data):
    expected="my name is 'ahmad SH', i'm a Musician"
    actual = prep_data['shela'].__str__()
    assert expected == actual

def test_get_instrument(prep_data):
    acutal = prep_data['jhon'].get_instrument()
    expected = 'Drums'
    assert expected==acutal

def test_play_solo(prep_data):
    actual = prep_data['shela'].play_solo()
    expected = 'some guitar sound'
    assert expected ==actual
