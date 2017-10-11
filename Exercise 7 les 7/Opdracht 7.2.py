
while True:
    woord = input('Geef hier een woord op: ')
    if len(woord) == 4:
        print('Inlezen van een correcte string: {} is geslaagd'. format(woord))
        break
    else:
        print('{} heeft {} letters'.format(woord, len(woord)))





