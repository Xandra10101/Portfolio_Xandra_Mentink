maand = eval(input('Vul hier een maandnummer in: '))

def seizoen(maandnummer):
    if 3 >=  maandnummer < 5:
        print('Het is nu lente')
    elif 6 >= maandnummer < 8:
        print('Het is nu zomer')
    elif 9 >= maandnummer < 11:
        print('Het is nu herfst')
    else:
        print('Het is nu winter')
seizoen(maand)



# nummers 3 t/m 5 = lente
# 9 t/m 11 = herfst
# 12,1,2 = winter
# 6 t/m 8 = zomer
