def namen():
    aantalkeernaam = {}
    for aantal in naam:
        if aantal in aantalkeernaam:
            aantalkeernaam[aantal] += 1
        else:
            aantalkeernaam[aantal] = 1
    return aantalkeernaam



naam = input('Wat is je voornaam: ')
print(namen())
