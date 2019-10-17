

bazaKsiazek=[]

def wyszukajKsiazke():
    print('Podaj rok wydania  [RRRR]')
    a=-1
    while a==-1:
        rok=input()
        if rok.isdecimal:
            for iterator in bazaKsiazek:
                if int(iterator['Rok_Wydania'])>=int(rok):
                    print(iterator)
            break
        else:
            print('Podana warotść nie jest liczbą')


def wprowadzKsiazke():
    ksiazka ={
        'nr_IBAN':0,
        'Rok_Wydania':0,
        'Tytul':'',
        'Autorzy':'',
        'Wydawnictwo':'',
        'Status':'',
        'Wypozyczajacy':''
    }

    for b in ksiazka:
        print('***********')
        print('Wprowadź',b)
        x = input('')
        
        # obsługa błędu dla braku lub błędnie wprowadzonego roku wydania lub nr IBAN
        if b=='Rok_Wydania' and (x=='' or x.isdecimal()==False) :
            print('ERROR !! ')
            print('Należy podać poprawną wartość liczbową dla rekordu => ', b)
            ksiazka = []
            break
    
        elif b=='nr_IBAN' and (x=='' or x.isdecimal()==False) :
            print('ERROR !! ')
            print('Należy podać poprawną wartość liczbową dla rekordu => ', b)
            ksiazka = []
            break
    
        else:
            print(b,' = ',x)
            ksiazka[b]=x
                
    
    return ksiazka


def dodajKsiazkeDoBazy(baza,ksiazka): 

    if ksiazka in baza:
        print("Taki egzemplarz już istnieje !! Nie można dodać do bazy danych !!")
        
    elif ksiazka ==[]:
        print("Nie można dodać błędnego rekordu do bazy !")
    
    elif len(baza)==0:
        print('Wprowadzana pozycja to:')
        print(ksiazka)
        bazaKsiazek.append(ksiazka)
    
    else:  
        for x in range(len(baza)):
        
            if baza[x]['Tytul'] == ksiazka['Tytul']:
                return print("Taki egzemplarz już istnieje !! Nie można dodać do bazy danych !!")

            else:
                print('Wprowadzana pozycja to:')
                print(ksiazka)
                bazaKsiazek.append(ksiazka)
                print('Aktualna liczba książek w bazie to', len(bazaKsiazek))

    return ksiazka


def zamienKsiazke(baza, staraKsiazka, nowaKsiazka):
    
    if staraKsiazka not in bazaKsiazek:
        print("Nie ma takiego egzemplarza w bazie danych!! Nie można zmienić bazy danych !!")
        
    elif nowaKsiazka in bazaKsiazek:
        print("Taki egzemplarz już istnieje !! Nie można dodać do bazy danych !!")

    else:
        print('Zmieniono egzemplarz', staraKsiazka, 'na', nowaKsiazka)
        
        index = bazaKsiazek.index(staraKsiazka)
        baza[index] = nowaKsiazka


def usunKsiazke(baza, staraKiazka):
    
    if staraKiazka not in bazaKsiazek:
        print("Nie ma takiego egzemplarza w bazie danych!! Nie można zmienić bazy danych !!")

    else:
        print("Usunięto egzemplarz: ",staraKiazka)
        baza.remove(staraKiazka)
        print('Aktualna liczba książek w bazie to', len(baza))


#=============MAIN=================

a=-1
while a!='':
    print('====Lista dostepnych czynnosci=============')
    print('1 -> Wyświetl baze danych biblioteki')
    print('2 -> Dodaj pozycję do księgozbioru ')
    print('3 -> Sprawdz pozycję w księgozbiorze ')
    print('4 -> Zmień pozycję w księgozbiorze ')
    print('5 -> Usuń pozycję w księgozbiorze ')
    print('0 - Koniec programu')
    print('---------------------------------------')
    wybor = input('Podaj wybór czynności: ')
    if wybor.isdecimal()==True:
        if int(wybor) ==1:
            print('Aktualna ilość ksiązek w bazie to', len(bazaKsiazek))
            print(bazaKsiazek)
            a = -1
        elif int(wybor) ==2:
            dodajKsiazkeDoBazy(bazaKsiazek, wprowadzKsiazke())
            a= -1

        elif int(wybor) ==3:
            wyszukajKsiazke()
            a =-1

        elif int(wybor) ==4:
            zamienKsiazke(bazaKsiazek,wprowadzKsiazke(),wprowadzKsiazke())
        
        elif int(wybor) ==5:
            usunKsiazke(bazaKsiazek,wprowadzKsiazke())
        
        elif int(wybor) ==0:
            break
        else:
            print("Wprowadzony znak nie jest znakiem z zakresu 1 -> 3")    
    else:
        print("Wprowadzony znak nie jest znakiem z zakresu 1 -> 3")
        


    








