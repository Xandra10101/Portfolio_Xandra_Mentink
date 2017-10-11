
def ticker():
    infile = open('tickernames.txt', 'r')
    regels = infile.readlines()
    infile.close()
    tickerdict = {}
    for regel in regels:
        tickerregel = regel.split(':')
        sleutel = tickerregel[0]
        waarde = tickerregel[1].strip()
        tickerdict[sleutel] = waarde
    return tickerdict


# input('Voer hier een bedrijfsnaam in: ')
# input('Voer hier een Ticker Symbol in:  ')
# print('Het bij behorende Ticker Symbol is {}'. format() )
# print('Het bij behorende bedrijfsnaam is {}'. format() )

print(ticker())
