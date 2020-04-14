
from src.bingo import sumar
from src.bingo import restar

def test_sumar():
    assert sumar(1,2) == 3
    assert sumar(1,10) == 11

def test_restar():
    assert restar(3,1) == 2