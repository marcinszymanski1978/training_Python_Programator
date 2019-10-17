def potegowanie(a,b):
    
    if int(b)==0 :
        wynik = 1
    else:
        wynik = int(a)**int(b)
    return wynik


def silnia(a):
    wynik = 1
    for x in range(int(a)):
        wynik = wynik*(x+1)
    return wynik





x = input("podaj liczbe: ")
y = input('podaj wykladnik ')
print('Potegowanie: ',x, 'do potegi', y, 'wynosi', str(potegowanie(x,y)))
print('Silnia z ', x, "wynosi ", str(silnia(x)))