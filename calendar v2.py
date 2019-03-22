'''
If year can be evenly divided by 4 it is a leap year. (Test this condition first.)
If the year can be evenly divided by 100 and 400 it is a leap year. (If condition 1 isn't met then test for this condition.)
Hints about the functions you will create for this exercise.

The leap year function will have one parameter (year).
The number of days in month function will have two parameters (month, year).
The number of days left in the year will have three parameters (day, month, year).
 
Menu:
1)  	Calculate the number of days in the given month.
2)  	Calculate the number of days left in the given year.

You'll need to include these functions:

leap_year: Takes the year as a parameter and returns a 1 if a year is a leap year and 0 if it is not. This information will only be used by other functions.
 
number_of_days: This subprogram will accept the date as parameters and return how many days are in the given month.


days_left: This will accept the date as parameters and then calculate the number of days left in the year. This should not include the date the user entered in the count.

'''

import math

#DATE VALID/INVALID??
def checkin(x, y):
#MONTH INVALID
    if(y > 12):
        return(False)
#DAY INVALID
    if(y == 4 or y == 6 or y == 9 or y == 11 and x > 30):
        return(False)
    elif(x > 29 and y == 2 and leapyear == 1):
        return(False)
    elif(x > 28 and y == 2 and leapyear == 0):
        return(False)
    elif(x > 31):
        return(False)
            
#LEAP YEAR???    
def leap_year(x):
    if(x % 4 == 0 and x % 100 != 0):
        return (1)
    elif(x % 400 == 0):
        return (1)
    else:
        return (0)

#1
def number_of_days(y, z):
    leapyear = leap_year(z)
    if(y == 2 and leapyear == 1):
        return(29)
    elif(y == 2 and leapyear == 0):
        return(28)
    elif(y == 4 or y == 6 or y == 9 or y == 11):
        return(30)
    else:
        return(31)
    
#2
def days_left(x, y, z):
    leapyear = leap_year(z)
    print("Start")
    print(x)
    for i in range(y - 1):
        if(i == 2 and leapyear == 1):
            x = x + 29
            print("+29")
        elif(i == 2 and leapyear == 0):
            x = x + 28
            print("+28")
        elif(i == 4 or i == 6 or i == 9 or i == 11):  #Backwards calendar
            x = x + 30
            print("+30")
        else:
            x = x + 31 
            print("+31")
    print("New X")
    print(x)
    if(leapyear == 1):
        return(366 - x)
    elif(leapyear == 0):
        return(365 - x)

#MAIN
print("Please enter a date.")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))  

#DATE VALID/INVALID CHECK
checkin(day, month)
while (checkin(day, month) == False):
    print("\nYour date was invalid. Please try again.\n")
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))  
    checkin(day, month)

#PRINT DATE
print("\nDate: " + str(month) + "/" + str(day) + "/" + str(year))

#MENU
menu = int(input("\nMenu: " + "\n1)\tCalculate the number of days in the given month." + "\n2)\tCalculate the number of days left in the given year.\n\n"))

#MENU ACTION
if(menu == 1):
    print(number_of_days(month, year))
if(menu == 2):
    print(days_left(day, month, year))
