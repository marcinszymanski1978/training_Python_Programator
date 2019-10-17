tablica = [[' ',' ',' '],
           [' ',' ',' '],
           [' ',' ',' ']]
runda = 1
print(tablica[0],tablica [1], tablica[2], sep='\n', end='\n')

def dodajKolko(a,b):
    if tablica[a][b] !=' ' :
        print("Pole nie jest puste, powtórz ruch")
    else:
        tablica[a][b]="O"
        global runda
        runda = runda +1
        

def dodajKrzyzyk(a,b):
    if tablica[a][b] !=' ' :
        print("Pole nie jest puste, powtórz ruch")
    else:
        tablica[a][b]="X"
        global runda
        runda = runda +1


while runda <= 9 :
    print('Runda nr: ', runda)
    if runda%2==0 :
        print('Tura gracza nr 2')
        x = int(input('X [0-1-2] = '))
        y = int(input('Y [0-1-2] = '))
        dodajKolko(y,x)
    else:
        print('Tura gracza nr 1')
        x = int(input('X [0-1-2] = '))
        y = int(input('Y [0-1-2] = '))
        dodajKrzyzyk(y,x)
    
    print(tablica[0],tablica [1], tablica[2], sep='\n', end='\n')

print('cala tablica zapelniona ==> powtórz gre !')