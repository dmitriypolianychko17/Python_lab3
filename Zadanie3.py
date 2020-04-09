from array import *
import random
numbers = array('f')
początek = int(-5)
koniec = int(5)
for i in range(5):
    numbers.append(random.uniform(początek, koniec))
file = open("Zadanie3.txt", "w")
file.write(str(numbers))
file.close()