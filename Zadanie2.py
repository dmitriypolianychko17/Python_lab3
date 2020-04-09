from array import *
numbers = array('u')
a = input("Podaj ilość liczb, które chcesz wpisać: ")
for i in range(int(a)):
 a = input(f"Podaj liczbę {i+1}: ")
 numbers.append(a)
numbers.reverse()
print(f"Odwrócona tablica: {numbers}")
