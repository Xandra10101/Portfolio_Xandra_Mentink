infile = open('Exercise5_2.txt', 'r')
regels2 = infile.readlines()
infile.close()
print('Deze file telt {} regels'.format(len(regels2)))
maximum = 0
regelnummer = 1
for regel in regels2:
    kaartinfo = regel.split(',')
    nummer = int(kaartinfo[0])
    if nummer > maximum:
        maximum = nummer
        maxregelnummer = regelnummer
    regelnummer += 1
print('Het grootste kaartnummer is {} en dat staat op regel {} '.format(maximum, maxregelnummer))

# for regel in regellijst():
#     grootste_nummer = max('Exercise5_2.txt')
#     locatie = find(0,len('Exercise5_2.txt'))


# print('Het grootste kaartnummer is {} en dat staat op regel {} ', format( ))

# print('Het grootste kaartnummer is {} en dat staat op regel {} ', format( ))
# lijstnummers = []


