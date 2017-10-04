def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def table():
    print('  F', 'C', sep = '       ')
    for graden in gradenlijst:
        fahrenheit = convert(graden)
        print('{:5}{:8}'.format(fahrenheit, graden))

gradenlijst = [-30.0, -20.0, -10.0, 0.0, 10.0, 20.0, 30.0, 40.0]
table()
