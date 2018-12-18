#1 zmienne
#zmienna1 = 1
#zmienna2 = 1.5
#zmienna3 = "tekst"

#print("zmienna 1: ", zmienna1)
#print("zmienna 2: ", zmienna2)
#print("zmienna 3: ", zmienna3)
#"cos {}".format(...)

#2  input
#imie = input("Podaj imie ")
#print("Witaj ", imie)

#print("Witaj " + input("podaj imie")

#3
#cena, napiwek, podatek=input("Podaj cene, napiwek i podatek ").split(",")
#cena = int (cena)
#podatek = int (podatek)
#napiwek = int (napiwek)

#print ("Koszt końcowy: ", cena*(1+(napiwek/100)+(podatek/100) ))


#4 zabezpieczenia przed błędami
#wiek=input("Podaj swój wiek: ")
#try:
#  wiek=int (wiek)
#except ValueError:
 # print("Błąd")

#if wiek<0:
#  print("Błąd")
#elif(wiek>= 0) and (wiek <= 10):
#  print("Jesteś dzieckiem")
#elif (wiek>10) and (wiek <=20):
#  print("Jesteś nastolatkiem")
#else:
#  print("Jesteś już duży, zapierdalaj do roboty")

#5 random, sortowanie
#from random import randint

#lista_liczb=list()
##print (random.randint(0,10))
##print (randint(0,10))

#while True:
#  if (len(lista_liczb)>30):
#    break
#  liczba = randint(-100,100)
#
#  if liczba not in lista_liczb:
#    lista_liczb.append(liczba)

#sorted nie modyfikuje pierwotnej - zwraca nową
#sort modyfikuje istniejącą

#print(lista_liczb)
#print(sorted(lista_liczb))
#print(lista_liczb[::-1])
#print(sorted(lista_liczb)[::-1])

#6 słowniki
#imiona=['Karol', 'Krzysiek', 'Artur', 'Pati']
#numery=[123456, 123654, 321456, 321654]

#telefoniczna=dict(zip(imiona,numery))
#print(telefoniczna)
#for imie, numer in telefoniczna.items():
#  print(("Imię: {:10} Numer: {:10}").format(imie,numer))

#7 
def fibonacci_1(n):
  if n is 0:
    return 0
  if n is 1:
    return 1
  else:
    return fibonacci_1(n-1)+fibonacci_1(n-2)

print("wersja 1:")
for i in range(1, 10):
  wynik=fibonacci_1(i)
  print(wynik)

def fibonacci_2(n):
  fibonacci=list()
  fibonacci.append(0)
  fibonacci.append(1)
  for i in range(2, n+1):
    fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
  return fibonacci

print("wersja 2")
wynik2=fibonacci_2(10)
print(wynik2)





