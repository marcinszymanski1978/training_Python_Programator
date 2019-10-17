def kwadrat(y):
    wynik = int(y)*int(y)
    return wynik

def nowyPrint(a):
    print('funkcja kwadrat z liczby', a, "wynosi", kwadrat(a))
    print(a)

# y = input ("podaj liczbe 0-9 :")

nowyPrint(input ("podaj liczbe 0-9 :"))

