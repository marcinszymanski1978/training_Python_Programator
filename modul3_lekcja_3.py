filmy =[]

nazwa = input("Podaj tytuł filmu: ")
rokProdukcji = input('Podaj rok produkcji: ')
gatunek = input('Podaj gatunek filmu /akcja/dramat/komedia/etc.: ')

film ={'tytul':nazwa, 'rokProdukcji':rokProdukcji, 'gatunek':gatunek}

filmy.append(film)

print(filmy)

