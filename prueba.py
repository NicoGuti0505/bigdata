def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True


def test_numeros_primos():
    assert es_primo(2)
    assert es_primo(3)
    assert es_primo(5)
    assert es_primo(7)
    assert es_primo(11)
    assert es_primo(13)
