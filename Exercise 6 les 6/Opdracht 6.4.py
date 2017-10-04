studentencijfers = [[95,92,86], [66,75,54], [89,72,100], [34,0,0]]
def gemiddelde_per_student(studentencijfers):
    antw = []
    for student in studentencijfers:
        gem = sum(student)/len(student)
        antw.append(gem)
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    som = sum(gemiddelde_per_student(studentencijfers))
    aantalstudenten = len(studentencijfers)
    antw = som/aantalstudenten
    return antw
print(gemiddelde_van_alle_studenten(studentencijfers))
print(gemiddelde_per_student(studentencijfers))
