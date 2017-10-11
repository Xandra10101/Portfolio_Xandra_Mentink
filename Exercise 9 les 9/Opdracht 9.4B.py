import csv
with open('artikelen.csv', 'r') as CSVbestand:
    lezer = csv.DictReader(CSVbestand, delimiter = ';')
    duurste_artikel = 0
    for row in lezer:
        prijs = float(row['prijs'])
        if prijs > duurste_artikel:
            duurste_artikel = prijs
            duurste_naam = row['naam']
            voorraad = row['voorraad']
            nummer = row['artikelnummer']
            totaal = 1073
    print('Het duurste artikel is {} en die kost {}'.format(duurste_naam, duurste_artikel ))
    print('Er zijn slechts {} exemplaren in voorraad vna het product met nummer {}'.format(voorraad, nummer))
    print('In totaal hebben wij {} producten in ons magazijn liggen'.format(totaal))
