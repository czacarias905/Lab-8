#Cecilia Zacarias
#3/5/2020

#problem 2 this function takes two inputs from a user and prints weather the sums is greater than 10,less than 10, or equal to 10
#import math

x = input("Choose a number:")

y = input("Choose your second number:")

sum = int(x) + int(y)
    

if int(x + y) >10:
    print(sum,"is greater then 10")

elif int(x + y) <10:
    print(sum,"is less then 10")

elif int(x + y) == 10:
    print(sum,"is equal to 10")
