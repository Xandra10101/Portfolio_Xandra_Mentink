def toon_aantalkluizen_vrij():
    infile = open ('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    aantal_kluizen = len(kluizendata)
    aantal_vrij = 12 - aantal_kluizen
    print('het aantal kluizen vrij is {}'.format(aantal_vrij))

def nieuwe_kluis():
    kluisnummers = []
    for i in range(1,13):
        kluisnummers.append(i)
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    for kluis in kluizendata:
        gegevenskluis1 = kluis.split(':')
        stringnummer = gegevenskluis1[0]
        nummer = int(stringnummer)
        kluisnummers.remove(nummer)
    if len(kluisnummers) > 0:
        nieuwkluisnummer = kluisnummers[0]
        print('Uw kluisnummer is {}'.format(nieuwkluisnummer))
        code = input('Voer hier een code in: ')
        outfile = open('kluizen.txt', 'a')
        outfile.write('{}:{}\n'.format(nieuwkluisnummer, code))
        outfile.close()
    else:
        print('Er zijn geen kluizen meer beschikbaar')

def kluis_openen():
    infile = open ('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer = input('Wat is uw nummer: ')
    code = input('Wat is uw code ')
    gegevenscorrect = False
    for regel in kluizendata:
        gegevens_van_kluis = regel.split(';')
        stringkluisnummer = gegevens_van_kluis[0]
        kluiscode = gegevens_van_kluis[1].strip()
        if stringnummer == stringkluisnummer and kluiscode == code:
            gegevenscorrect = True
    if gegevenscorrect == True:
        print('correct')
    else:
        print('niet correct')

print('1: ik wil weten hoeveel kluizen er nog vrij zijn ')
print('2: ik wil een nieuwe kluis ')
print('3: ik wil iets uit mijn kluis halen')

keuze = eval(input('Geef hier uw keuze op: '))
if keuze == 1:
    toon_aantalkluizen_vrij()
elif keuze == 2:
    nieuwe_kluis()
else:
    kluis_openen()





