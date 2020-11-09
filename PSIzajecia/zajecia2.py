from file_manager import FileManager
#-------------------CW 1---------
def parniepar(a_list, b_list):
    c_list = []
    for i in a_list:
        if i%2 == 0:
            c_list.append(i)
    for i in b_list:
        if i%2 == 1:
            c_list.append(i)

    return c_list
a_list = [1,2,3,4,5,6,7,8,9,10]
b_list = [11,12,13,14,15,16,17,18,19,20]
print(parniepar(a_list,b_list))


#-------------------CW 2---------
def splitlist(tekst):
    newlist = []
    newlist[:0] = tekst
    return newlist

def ztextem(data_text):
    meta_text = {
          "Lenght": len(data_text),
          "Letters": splitlist(data_text),
          "BIG_LETTERS": data_text.upper(),
          "small_letters": data_text.lower()
        }
    return meta_text

print(ztextem("SieManko"))
#-------------------CW 3---------
def usunlitere(text, letter):
    bezlitery= ""
    for i in text:
        if i != letter:
            bezlitery = bezlitery+i;
    return bezlitery

print(usunlitere("Ta bateria posiada całkowity brak energii", "a"))
#-------------------CW 4---------
def zamiencelcjusz(temp, temperature_type):

    if temperature_type == "kelvin":
        nowatemp = (temp + 273.15)

    elif temperature_type == "rankine":
        nowatemp = (temp + 273.15) * 1.8

    elif temperature_type == "fahrenheit":
        nowatemp = (temp * 1.8) + 32
    else:
        return "podaj poprawną wartość na jakim typ konwersji a nie na jakieś " + temperature_type + "y"
    return nowatemp

print(zamiencelcjusz(32, "kelvin"))
print(zamiencelcjusz(32, "rankine"))
print(zamiencelcjusz(32, "fahrenheit"))
print(zamiencelcjusz(32, "centymetr"))
#-------------------CW 5---------
class calculator:
    def add(a,b):
        return a+b
    def difference(a,b):
        return a - b
    def multiply(a,b):
        return a * b
    def divide(a,b):
        return a / b
class ScienceCalculator:
    def exponentiation(a, x):
        value = 1
        while x >= 0:
            x = x-1
            value = a * a
        return value
def odwroc(text):
    return text[::-1]
print(odwroc("SIemanko to ja Adrian"))

plik = FileManager("Siemanko.txt")
plik.update_file("Witam bardzo serdecznie nazywam sie Adrian")
plik.update_file("A to przykładowy plik")
print(plik.read_file())

