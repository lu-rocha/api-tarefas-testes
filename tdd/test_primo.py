# test_primo.py

from primo import eh_primo


def test_eh_primo():
    assert eh_primo(2) == True
    assert eh_primo(7) == True
    assert eh_primo(4) == False
    assert eh_primo(11) == True
    assert eh_primo(1) == False
