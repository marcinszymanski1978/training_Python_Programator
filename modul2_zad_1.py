liczba =""
def czyulamek(x):
    a = float(x)
    b = int(a)
    if a==b:
        return "liczba nie jest ułamkiem"
    else:
        return 'liczba jest ułamkiem'

# ===========MAIN======================

while (liczba =="" ):
    liczba = input("podaj liczbe w formacie ##.## : ")

print(czyulamek(liczba))