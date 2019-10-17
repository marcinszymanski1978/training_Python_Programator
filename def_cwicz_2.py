x = 'to jest z zewnatrz'
def nowa(a):
    print(x)
    print(a)
nowa('test')


y =2
def kwadrat():
    # global y -->> to jest przypisanie do zmiennej zewnetrznej 'y' nalezacej do programu
    y = 20 
    print(y, 'to jest wewnatrz funkcji')

kwadrat()

print(y, 'to jest z zewnatrz')