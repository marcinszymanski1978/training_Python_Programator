liczba=100
while(liczba>=1):
    print(liczba)
    
    if (liczba%3==0 and liczba%5==0):
        print(liczba,"FizzBuzz")
    elif (liczba%3==0):
        print(liczba,"Fizz")
    elif (liczba%5==0):
        print(liczba,"Buzz")
    liczba=liczba-1
    