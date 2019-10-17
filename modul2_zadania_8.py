def nowaPlansza(x,y):
    matryca =[]
    for a in range(y):
        lista =[]
        for b in range(x):
            lista.append(' ')
        
        matryca.append(lista)

    return matryca

def drukujPlansze(plansza):
    x= int(len(plansza))
    for a in range(x):
        print(plansza[a])


def wstaw(x,y):
    global runda
    global stanPola
    if stanPola(x,y)==True:
        if runda%2==0:
            plansza[x][y]='O'
            
        else:
            plansza[x][y]='X'
        runda +=1
            
    else:
        print('Pole x=',x,'y=',y, 'jest już zajete ! Jego wartość to: ', plansza[x][y])

        



def stanPola(x,y):
    return plansza[x][y]==' '




#===========MAIN===========
runda = 1
iloscRund = int(input('Podaj ilosc rund: '))
x = int(input('Podaj ilosc kolumn: '))
y = int(input('Podaj ilosc wierszy: '))
plansza = nowaPlansza(x,y)

drukujPlansze(plansza)
while runda<=iloscRund:
    
    print('Runda nr: ', runda)
    x=int(input('Podaj nr wiersza: '))
    if x>int(len(plansza)):
        print('Wprowadzona warość x jest poza zakresem planszy !' )
    else: 
        y=int(input('Podaj nr kolumny: '))
        if y>int(len(plansza[x-1])):
            print('Wprowadzona warość y jest poza zakresem planszy !' )
        else:
            wstaw((x-1),(y-1))
    drukujPlansze(plansza)

    print('==================')












