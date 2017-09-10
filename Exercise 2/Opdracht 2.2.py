cijferICOR = 6
cijferPROG = 7
cijferCSN = 8
gemiddelde = ((cijferCSN + cijferICOR + cijferPROG)/3)
beloning = ((cijferCSN *30) + (cijferICOR *30)+ (cijferPROG * 30))
overzicht = 'mijn cijfers (gemiddeld een ' + str(gemiddelde)+ ' ) leveren een beloning van € '+str(beloning)+'op!'
print(overzicht)
