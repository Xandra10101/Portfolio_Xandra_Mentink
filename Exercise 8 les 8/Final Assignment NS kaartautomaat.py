def inlezen_beginstation(stations):
    beginstation = input('Geef hier uw beginstation op: ')
    while beginstation not in stations:
        beginstation = input('Ongeldige invoer. Geef een nieuw station op: ')
    return beginstation

def inlezen_eindstation(stations, beginsstation):
    eindstation = input('Geef hier uw eindstation op: ')
    while eindstation not in stations:
        eindstation = input('Ongeldige invoer. Geef een nieuw station op: ')
    while stations.index(eindstation)<= stations.index(beginstation):
        eindstation = input('Ongeldige invoer. Geef een nieuw station op: ')
    return eindstation

def omroepreis(stations, beginstation, eindstation):
    nummerBeginstation = stations.index(beginstation) + 1
    nummerEindstation = stations.index(eindstation) + 1
    afstand_reis = nummerEindstation - nummerBeginstation
    ritprijs = 5 * afstand_reis
    print('Het beginstation {} is het {}e station in het traject'.format(beginstation, nummerBeginstation))
    print('Het eindstation {} is het {}e station in het traject'.format(eindstation, nummerEindstation))
    print('De prijs van het kaartje bedraagt {} euro'.format(ritprijs))
    print('De afstand bedraagt {} stations'.format(afstand_reis))
    print(('U stapt in de trein in: {}'. format(beginstation)))
    for i in range(nummerBeginstation, nummerEindstation - 1):
        print(stations[i])
    print(('U stapt uit in: {}'.format(eindstation)))


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaamdam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepreis(stations, beginstation, eindstation)

