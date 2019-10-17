x = input("podaj rok w formacie ####")
if ((int(x)%4==0 and int(x)%100!=0) or int(x)%400==0 ):
    print('rok jest przestepny')
else:
    print('rok nie jest przestepny')