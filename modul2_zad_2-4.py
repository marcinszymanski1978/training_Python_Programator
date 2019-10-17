
def tablica_suma_liczb(lista):

    suma = 0
    for x in lista:
        #print(x)
        suma = suma + x
    return ("suma " + str(suma))

def min_max(lista):
    a = min(lista)
    b = max(lista)
    return "min = "+str(a)+" || max = "+str(b)

def suma_tablic(a,b):
    suma_a =0
    suma_b =0
    for x in a:
        suma_a=suma_a+x
    for y in b:
        suma_b=suma_b+y
    if suma_b==0:
        a_div_b = "Błąd: Dzielenie przez O"
    else:
        a_div_b = suma_a/suma_b
    return "Suma A = "+str(suma_a)+" || Suma B = "+str(suma_b)+" || A/B = "+str(a_div_b)


wart = [1,2,2,4,6]
wart_1 = [0,0,0]
print(min_max(wart))
print(tablica_suma_liczb(wart))
print(suma_tablic(wart,wart_1))