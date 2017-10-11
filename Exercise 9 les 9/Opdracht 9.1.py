try:
    aantal_personen = int(input('Hoeveel personen gaan mee: '))
    if aantal_personen <0:
        raise IndexError
    kosten = 4356/aantal_personen
    print(kosten)
except ZeroDivisionError:
    print('U kan niet delen door 0')
except ValueError:
    print('U moet een getal invoeren')
except IndexError:
    print('Negatieve getallen zijn niet toegestaan!')
except TypeError:
    print('Ongeldige invoer')
except OverflowError:
    print('Ongeldige invoer')
except RuntimeError:
    print('Ongeldige invoer')
