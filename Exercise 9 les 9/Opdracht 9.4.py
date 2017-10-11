import csv
with open('artikelen.csv', 'w', newline = '') as CSVbestand:
    schrijver = csv.writer(CSVbestand, delimiter = ';')
    schrijver.writerow(('artikelnummer', 'artikelcode', 'naam', 'voorraad', 'prijs'))

    while True:
        artikelnummer = input('Geef hier een artikelnummer op: ')
        if artikelnummer == '':
            break
        artikelcode = input('Geef hier een artikelcode op: ')
        naam = input('Geef hier een naam op: ')
        voorraad = input('Geef hier een voorraad op: ')
        prijs = input('Geef hier een prijs op: ')
        schrijver.writerow((artikelnummer, artikelcode, naam, voorraad, prijs))

