def sumaTablica(tablica):
    suma=0
    for licznik in tablica:
        suma=suma+licznik
    print('ilosc el.= ', len(tablica))
    return suma

def minLiczbaTablicy(tablica):
    minimum = tablica[0]
    for x in tablica:
        if x<minimum:
            minimum=x

    return minimum



lista =[]
liczba =''
while (liczba != ' '):
    liczba = input('podaj liczbe: ')
    
    if liczba ==" ":
        break
    else:
        liczba = float(liczba)
        lista.append(liczba)
        print(liczba)


print('Tablica = ', (lista))
print('Suma = ',sumaTablica(lista))
print('minimum = ',minLiczbaTablicy(lista))


