def sumaTablica(tablica):
    suma=0
    for licznik in tablica:
        suma=suma+licznik
    return suma

matryca = []
sumaMatryc = 0
for x in range(2):
    print('Lista nr: ', x+1)
    lista =[]
    liczba =''
    while (liczba != ' '):
        liczba = input('podaj liczbe: ')
        
        if liczba ==" ":
            break
        else:
            liczba = float(liczba)
            lista.append(liczba)
        print('Tablica = ', (lista))
        print('ilosc el.= ', len(lista))
        print('Suma = ',sumaTablica(lista))
        #print('minimum = ',minLiczbaTablicy(lista))
    sumaMatryc+=sumaTablica(lista)
    matryca.append(lista)

print('Matryca = ', matryca)
print('Suma = ',sumaMatryc)



