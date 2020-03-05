#Cecilia zacarias
#3/5/2020

#problem 3 this function take s list and checks if the value 5 is in the list

#generating random list of numbers
import random

res = [random.randrange(1, 15, 1) for i in range(7)]

print("Random number list is:" + str(res))

#checking is if the value 5 is in list

if 5 in res:
    print("5 exist in list")
else:
    print("ther is no 5 in this list")
    
