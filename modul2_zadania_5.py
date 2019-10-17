def rokPrzestepny(rok):
    print(('Czy rok jest przestepny ? Odpowiedź: ', rok%4==0 and rok%100!=0) or rok%400==0)



rok=int(input('Podaj rok YYYY '))
rokPrzestepny(rok)

