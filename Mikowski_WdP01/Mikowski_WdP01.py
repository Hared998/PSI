a = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie="Michał"
nazwisko="Mikowski"
litera_1=imie[1]
litera_2=nazwisko[2]
print("W tekście jest {} oraz {} liter".format(a.count(litera_1),a.count(litera_2)))



print("\n")


zmienna_typu_string="Hello There!"


print(dir(zmienna_typu_string))
help(zmienna_typu_string.capitalize())


print("\n")


print("Moje imie od tyłu to: %s, a nazwisko: %s" % (imie[::-1], nazwisko[::-1]))


print("\n")


lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = lista[5:10]
lista = lista[0:5]
print(lista2)
print(lista)
lista[5:]=lista2
print(lista)


print("\n")


student1= ("Michał", 412453)
student2= ("Jarek", 777777)
student3= ("Karol", 111111)
lista_studentów = [student1, student2,  student3]
slownik_studentów = {student1[0]:student1[1],student2[0]:student2[1],student3[0]:student3[1]}
print(slownik_studentów)