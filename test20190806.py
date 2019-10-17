miasto0 ={
    'Nazwa':'Lubin',
    'Panstwo':'Polska',
    'Liczba_Mieszkancow':2000
    }

miasto1 ={
    'Nazwa':'Legnica',
    'Panstwo':'Polska',
    'Liczba_Mieszkancow':3500
    }


miasto2 ={
    'Nazwa':'Breslau',
    'Panstwo':'Niemcy',
    'Liczba_Mieszkancow':4500
    }


bazaMiast=[miasto0,miasto1,miasto2]



def dodajMiasto(baza, noweMiasto):
    if noweMiasto in baza:
        print("Takie miasto już istnieje !! Nie można dodać do bazy danych !!")
        
    elif noweMiasto ==[]:
        print("Nie można dodać błędnego rekordu do bazy !")
    
    elif len(baza)==0:
        print('Wprowadzana pozycja to:')
        print(noweMiasto)
        bazaMiast.append(noweMiasto)
    
    else:  
        print('Wprowadzana pozycja to:')
        print(noweMiasto)
        bazaMiast.append(noweMiasto)
        print('Aktualna liczba miast w bazie to', len(bazaMiast))

    return noweMiasto


def usunMiasto(baza, usuwaneMiasto):
    if usuwaneMiasto not in baza:
        print("Nie ma takiego miasta w bazie danych!! Nie można zmienić bazy danych !!")

    else:
        print("Usunięto miasto: ", usuwaneMiasto)
        baza.remove(usuwaneMiasto)
        print('Aktualna liczba miast w bazie to', len(baza))

def zamienMiasto(baza, stareMiasto, noweMiasto):
    if stareMiasto not in baza:
        print("Nie ma takiego miasta w bazie danych!! Nie można zmienić bazy danych !!")
        
    elif noweMiasto in baza:
        print("Takie miasto już istnieje !! Nie można dodać duplikatu miasta do bazy danych !!")

    else:
        print('Zmieniono miasto', stareMiasto, 'na', noweMiasto)
        
        index = baza.index(stareMiasto)
        baza[index] = noweMiasto

def wyswietlmiasto(baza):
    print('Podaj Państwo w którym chcesz wyświetlić miasta')
    panstwo=input()
    lista = []
    if panstwo!='':
        for iterator in baza:
            if iterator['Panstwo']==panstwo:
                lista.append(iterator['Nazwa'])
                
    else:
        print('Nie wprowadzono żadnej wartości')

    return lista


def sredniaLiczbaMieszkancow(baza, szukaneMiasto):
    suma = 0
    liczbaMiast = 0
    wynik =''
    if szukaneMiasto==[]:
        wynik = "Wprowadzono niepoprawne dane"
        return wynik

    for licznik in baza:
        if licznik['Panstwo'] == str(szukaneMiasto['Panstwo']):
            suma+=int(licznik['Liczba_Mieszkancow'])
            liczbaMiast+=1
            wynik = str(suma/liczbaMiast)

    return wynik

def sredniaLiczbaMieszkancowBazyMiast(baza):
    suma = 0
    
    for licznik in baza:
        suma+=int(licznik['Liczba_Mieszkancow'])
        

    return suma/len(baza)

def najwiekszeMiasto(baza):
    maxLudnosc=-1
    maxMiasto=''
 
    for licznik in bazaMiast:
        if int(licznik['Liczba_Mieszkancow'])>maxLudnosc:
            maxMiasto=licznik["Nazwa"]
            maxLudnosc=int(licznik['Liczba_Mieszkancow'])

    wynik = str(maxMiasto)+' : '+ str(maxLudnosc)

    return wynik
   

def najmniejszeMiasto(baza):

    minLudnosc=99999999999999
    minMiasto=''
 
    for licznik in bazaMiast:
        if int(licznik['Liczba_Mieszkancow'])<minLudnosc:
            minMiasto=licznik["Nazwa"]
            minLudnosc=licznik['Liczba_Mieszkancow']

    wynik = str(minMiasto)+' : '+ str(minLudnosc)

    return wynik


def wprowadzMiasto():
    miasto ={
        'Nazwa':'',
        'Panstwo':'',
        'Liczba_Mieszkancow':0
    }

    for licznik in miasto:
        print('***********')
        print('Wprowadź',licznik)
        dane = input('')
        
        # obsługa błędu dla braku lub błędnie wprowadzonych danych
        if licznik=='Liczba_Mieszkancow' and (dane=='' or dane.isdecimal()==False) :
            print('ERROR !! ')
            print('Należy podać poprawną wartość liczbową dla rekordu => ', licznik)
            miasto = []
            
    
        elif dane==''  :
            print('ERROR !! ')
            print('Należy podać wartość tekstową dla rekordu => ', licznik)
            miasto = []
            
    
        else:
            print(licznik,' = ',dane)
            miasto[licznik]=dane
                
    
    return miasto    

#=============MAIN=================

a=-1
while a!='':
    print('====Lista dostepnych czynnosci=============')
    print('1 -> Wyświetl baze danych miast')
    print('2 -> Dodaj pozycję do bazy danych ')
    print('3 -> Sprawdz pozycję w bazie danych')
    print('4 -> Zmień pozycję w bazie danych ')
    print('5 -> Usuń pozycję z bazy danych ')
    print('6 -> Wyświetl średnią liczbę mieszkańców danego kraju ')
    print('7 -> Wyświetl średnią liczbę mieszkańców miast znajdujących się w bazie danych')
    print('8 -> Wyświetl najmniej liczne miasto')
    print('9 -> Wyświetl najbardziej liczne miasto')
    print('0 - Koniec programu')
    print('---------------------------------------')
    wybor = input('Podaj wybór czynności: ')
    if wybor.isdecimal()==True:
        if int(wybor) ==1:
            print('Aktualna ilość miast w bazie to', len(bazaMiast))
            print(bazaMiast)
            a = -1
        elif int(wybor) ==2:
            dodajMiasto(bazaMiast, wprowadzMiasto())
            a= -1

        elif int(wybor) ==3:
            print(wyswietlmiasto(bazaMiast))
            a =-1

        elif int(wybor) ==4:
            zamienMiasto(bazaMiast,wprowadzMiasto(),wprowadzMiasto())
        
        elif int(wybor) ==5:
            usunMiasto(bazaMiast,wprowadzMiasto())
        
        elif int(wybor) ==6:
            print(sredniaLiczbaMieszkancow(bazaMiast,wprowadzMiasto()))

        elif int(wybor) ==7:
            print(sredniaLiczbaMieszkancowBazyMiast(bazaMiast))
            
        elif int(wybor) ==8:
            print(najmniejszeMiasto(bazaMiast))

        elif int(wybor) ==9:
            print(najwiekszeMiasto(bazaMiast))
        
        elif int(wybor) ==0:
            break
        else:
            print("Wprowadzony znak nie jest znakiem z zakresu 1 -> 3")    
    else:
        print("Wprowadzony znak nie jest znakiem z zakresu 1 -> 3")