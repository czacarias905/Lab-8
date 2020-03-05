#Cecilia Zacarias
#3/5/2020

#Problem 4 this is a function that takes a year as a parameter and returns true if the year is a leap year, false if it is not.

year = int(input("Please Enter the Year you wish to check if it is a leap year: "))

if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d is a Leap Year" %year)
else:
    print("%d is Not a Leap Year" %year)

