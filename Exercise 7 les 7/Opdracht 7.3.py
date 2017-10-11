def goedecijfers():
    for naam  in cijfers:
        if cijfers[naam] > 9.0:
            print(naam, cijfers(naam))
        else:
            print(cijfers)
    return cijfers

# print(list(cijfers.keys()))
print(goedecijfers())
cijfers = {'Jan van der Hof':'6.5', 'Zander de Jong':'9.2', 'Herman Veringa':'4.5', 'Erik ter Horst':'8.7', 'Lieke de Graaf':'6.7', 'Merinda den Broek':'7.4', 'Bart Lindhorst':'9.7', 'Cait McCormick':'8.4', 'Elise Pen':'5.4', 'Dirk Geesthuizen':'3.5'}
