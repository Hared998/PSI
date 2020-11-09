lista_a = [i for i in range(1,11,1)]
lista_b = [i for i in range(11,21,1)]
def function(a_list,b_list):
    b_list=[b for b in b_list if b%2==1]
    a_list=[a for a in a_list if a%2==0]
    c_list=a_list+b_list
    print(c_list)
function(lista_a,lista_b)
print("\n")


text1="PlacUSzki"
def function2(data_text):
    x=[a for a in data_text]
    slownik={"length": len(data_text),"letters":x,"big_letters":data_text.upper(),"small_letters":data_text.lower()}
    return slownik
print(function2(text1))
print("\n")



def function3(text, letter):
    for x in letter:
        text=text.replace(x,'')
    print(text)
function3(text1,"Uzi")
print("\n")


def function4(celcius,temperature_type):
    if temperature_type=="Kelvin":
        return celcius+273.15
    elif temperature_type=="Fahrenheit":
        return (celcius*1.8)+32
    elif temperature_type=="Rankine":
        return (celcius + 273.15)*1.8
    else :
        return "Podaj temperature!"
print(function4(15,"Kelvin"))
print(function4(15,"Fahrenheit"))
print(function4(15,"Rankine"))
print("\n")



class Calculator:
    def add(a,b):
        return a+b
    def difference(a,b):
        return a - b
    def multiply(a,b):
        return a * b
    def divide(a,b):
        return a / b

class ScienceCalculator(Calculator):
    def pow(a,b):
        return a**b

def function5(text):
    print(text[::-1])
function5("koteł")
print('\n')


