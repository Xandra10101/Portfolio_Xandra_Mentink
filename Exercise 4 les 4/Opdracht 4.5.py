grondgetallen = [4, 5, 3, -81]
def kwadraten_som(grondgetallen):
    som = 0
    for nummer in grondgetallen:
        if nummer == abs(nummer):
            som += nummer**2
    return som
print(kwadraten_som(grondgetallen))
