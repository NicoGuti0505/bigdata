def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
<<<<<<< HEAD
    return True
=======
    return True                                        
>>>>>>> 41bcd8a569b1fcd71c52e2fac3e49f14c9292166
