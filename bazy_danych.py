bazaosob = []

osoba1 = {
    'imie' : 'Marcin',
    'nazwisko' : 'Szymanski'
    }

osoba2 = {
    'imie' : 'Magda',
    'nazwisko' : 'Szymanska'
}

bazaosob = [osoba1,osoba2]

def dodajOsobe(baza,osoba):
    if osoba in baza :
        print('Błąd -> taka osoba już istnieje w bazie')
    else:
        baza.append(osoba)
    

def usunOsobe(baza,osoba):
    if osoba in baza :
        baza.remove(osoba)
    else:
        print('Błąd -> nie ma takiej osoby w bazie')

def zamienOsobe(baza, osoba):
    if osoba in baza :
       zmianaImie = input('Podaj nowe imie: ')
       zmianaNazwisko = input('Podaj nowe nazwisko: ')
       index = baza.index(osoba)
       baza[index] = {
           'imie' : zmianaImie,
           'nazwisko' : zmianaNazwisko
       }

    else:
        print('Błąd -> nie ma takiej osoby w bazie')

#def inputData():
imie =""
nazwisko =""
wybor=""

while wybor != '4' :
    imie = input('Podaj Imie: ')
    nazwisko = input('Podaj nazwisko: ')
    wybor = input('Podaj wybor 1-3: ')
    osoba = {
        'imie' : imie,
        'nazwisko' : nazwisko
}

    if wybor == '1' :
        dodajOsobe(bazaosob,osoba)
    elif wybor =="2":
        usunOsobe(bazaosob,osoba)
    elif wybor =='3':
        zamienOsobe(bazaosob,osoba)
    
    print(bazaosob)
    print('Ilosć osób w bazie', len(bazaosob))





