def silnia(a):
    wynik=1
    for x in range(a):
        wynik *=(x+1)
    return wynik

liczba = int(input('podaj liczbe do silni'))
print(silnia(liczba))