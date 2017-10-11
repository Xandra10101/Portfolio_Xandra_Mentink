getallenlijst = []
getal = 1
while getal != 0:
    getal = eval(input('Geef een getal: '))
    if getal != 0:
        getallenlijst.append(getal)
som = sum(getallenlijst)
aantalgetallen = len(getallenlijst)
print('Er zijn {} getallen ingevoerd, de som is : {}'. format(aantalgetallen, som))


# while true:
#    getal = eval(input('Geef een getal: '))
#    if getal == 0:
#        break
#    else:
#       som = som + getal
# print(som)
