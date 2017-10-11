import csv
with open('Inloggers.csv', 'w', newline = '') as CSVfile:
    schrijver = csv.writer(CSVfile, delimiter = ';')
    schrijver.writerow(('naam', 'voorl', 'gbdatum', 'email'))

    while True:
        naam = input('Wat is uw achternaam: ')
        if naam == 'einde':
            break
        voorl = input('Wat zijn uw voorletters: ')
        gbdatum = input('Wat is uw geboortedatum: ')
        email = input('Wat is uw emailadres: ')

        schrijver.writerow((naam, voorl, gbdatum, email))
