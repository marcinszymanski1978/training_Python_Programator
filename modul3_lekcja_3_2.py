czynnosci =['Powrót do menu głównego', 'Dodaj', 'Usuń', 'Wyświetl bazę danych' ]
moduly = ['Koniec', 'Sprzedarz','Magazyn','Kontrahenci', 'Wyświetl bazę danych']
nrTransakcji=0
lista_Transakcji = {}
towary =[]
kontrahenci =[]





def dodajItem(a1,b1):
    global nrTransakcji
    nrTransakcji+=1
    transakcja = moduly[a1]+':'+czynnosci[b1]
    print(transakcja)
    lista_Transakcji[nrTransakcji] = transakcja




def usunItem(a1,b1):
    global nrTransakcji
    nrTransakcji+=1
    transakcja = moduly[a1]+':'+czynnosci[b1]
    lista_Transakcji[nrTransakcji] = transakcja

def wyswietlBazeDanych():
    global nrTransakcji
    print(lista_Transakcji)

    


#print('Lista dostepnych modułów')
#print('1 -> Sprzedarz')
#print('2 -> Magazyn')
#print('3 -> Kontrahenci')
#a=int(input('Podaj wybor modułu: '))
a=-1
b=-1

while a !=0:
    while a != 1 and a!=2 and a!=3 and a!=0:
        print('========================')
        print('Lista dostepnych modułów')
        print('1 -> Sprzedarz')
        print('2 -> Magazyn')
        print('3 -> Kontrahenci')
        print('0 -> Koniec')
        a=int(input('Podaj wybor modułu: '))
        print('Wybrany moduł to ==> ', moduly[a])
        if a==1:
            b=-1
        
        elif a==2:
            b=-1
        
        elif a==3:
            b=-1


    while b != 1 and b!=2 and b!=3 and b!=0 and a!=0:
        print('--------------------------')
        print('Lista dostepnych czynności')
        print('1 -> Dodaj')
        print('2 -> Usuń')
        print('3 -> Wyświetl bazę danych')
        print('0 -> Powrót do menu głównego')
        
        b=int(input('Podaj wybor czynności: '))
        
        print('Wybrana czynność to ==> ', czynnosci[b])
        if b==1:
            dodajItem(a,b)
            a=-1
        
        elif b==2:
            usunItem(a,b)
            a=-1
        
        elif b==3:
            wyswietlBazeDanych()
            a=-1
        
        elif b==0:
            a=-1
            

print(a,b)




