import math
from test import *
print("Hello world")
liczba=42
print(liczba)
liczba="superkurs"
print(liczba)
print("tekst",end="\n") #domyœlnie
print("tekst2", end="*\n")

#bool (True/False)
#int, zespolone
#tuple -krotki zadeklarowane i bez zmian
#lista
liczby =list()
liczby.append(1)
print(liczby) #drukuje w nawiasie kwadratowym
liczby=[1,5, 10, 3.2, "mas³o"]
print(liczby) #drukuje ca³¹ tablicê
print(liczby[2])

lista2=[1, 2, 3, "xddd"]

liczby.append(lista2) #lista w liœcie
print(liczby)

liczby.extend(lista2) #dodaje listy do siebie <3
print(liczby)

#s³owniki klucz:wartosc
s³ownik={"Ko³o":"Robocik","iloœæ":68}
print(s³ownik["Ko³o"]) #drukuje "Robocik"
s³ownik["Kolejny"]="Dzia³a"
print(s³ownik["Kolejny"])
print(s³ownik)

#operacje arytmetyczne
#a/b float a//b int
a=5
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b) #float
print(a//b) #int
print(a%b)
print(a**b)
print(a**(1/b)) #pierwiastek a stopnia b

#print(input("Jesteœ spoko :D")) #pobiera dane z konsoli

#print(input("podaj trzy liczby ").split(",")) # w split #domyœlnie spacja, mo¿na daæ inny znak np ","

#pêtle
# while True:
i=95
while i<100:
  print(i)
  i=i+1
for i in range(0,5):
  print(i)

#print(range(5))
#print(range(3,6))# 3,4,5
#print(range(0, 10,2))# 0,2,4,6,8

for i in range(3,6):
  print(i)

for i in range (0,10,3):#co 3
  print (i)

# pass nic nie rób
b=10
if b>10:
  print("B > 10")
elif b==10:
  print("B = 10\n")
else:
  print("B < 10") 

a=2
b=3
if a>10 and b>2:
  print("OK 1") 

c=10
d=15  
if c>16 or d>10:
  print("OK 2\n")   


#def nazwa_funkcji(argumenty):
 # czynnoœci
  #return mo¿e nie musi

def luz():
  print("chillout")
luz()
#rekurencja
def silnia(n):
  if(n>0):
    return silnia(n-1)*n
  if (n==0):
    return 1

print(silnia(5))

print (math.pi)

print(a)
print(funkcja())

class Dog: #przy dziedziczeniu DOg(zwierzê)
  species='mammal'
  def __init__(self, name, age):#konstruktor
    self.name=name
    self.age=age
  def szczekaj(self, tekst):
    print("Hau {}".format(tekst))
  zmienna=12

pies=Dog("Burek", 2)
print (pies.age)
pies.szczekaj("robocik")
#innit del konstruktor/destruktor
#enter exit
print(pies.zmienna)

def tabliczka_mnozenia():
  for i in range(1,11):
    print(" ")
    for j in range(1,11):
      print("{:3}".format (i*j), end= " ")
  

tabliczka_mnozenia()


lista =[1, 2, 3, 4, 5, 6, 7, 8]

for liczba in lista:
  print liczba