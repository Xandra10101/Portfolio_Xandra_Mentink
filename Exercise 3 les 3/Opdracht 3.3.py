leeftijd = eval(input('Wat is uw leeftijd: '))
paspoort = input('Heeft u een Nederlands paspoort: ')
if paspoort == 'ja' and leeftijd >= 18:
    print('Gefeliciteerd, u mag stemmen!')
else:
    print('Helaas, u mag niet stemmen')

