lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie = "Adrian"
nazwisko = "Merchel"
counti = 0
countn = 0
for i in lorem:
    if i == imie[2]:
        counti = counti + 1
    elif i == nazwisko[3]:
        countn = countn + 1
print("W tekście jest " + str(counti) + " liter: " + imie[2] + " oraz " + str(countn) + " liter: " + nazwisko[3])

zmienna_typu_string = "KrUlestwo wszelakie"
print(dir(zmienna_typu_string))
help(zmienna_typu_string.capitalize())
eime = imie[::-1]
oksiwzan = nazwisko[::-1]
print(eime + " " + oksiwzan)

tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tab2 = tab[5:10]
for i in tab:
    if i < 6:
        tab.pop()
tab.extend(tab2)
tab.insert(0,0)
print(tab)
indeksy = ("15553", "23345", "10045", "345013")
imina = ('Adrian Merchel', "Bartek Kowalski", "Rober Stefanczyk", "Maciej Markowski")
polaczone = indeksy, imina

print(polaczone)

indeks = dict({indeksy[0]:imina[0], indeksy[1]:imina[1], indeksy[2]:imina[2], indeksy[3]:imina[3]})
print(indeks)
telefony = ["660272666","660272666", "660272664", "664272666", "660272626", "660272626"]
print(telefony)
telefony = set(telefony)
print(telefony)

for i in range(1,11):
    print(i)
for j in reversed(range(20,101)):
    print(j)
