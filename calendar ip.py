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

def leap_year(x):
    if(x % 4 == 0 and x % 100 != 0):
        return (1)
    if(x % 100 == 0 and x % 400 == 0):
        return (1)
    else:
        return (0)

def number_of_days(x, y):
    leap_year(year)
    if(y % 2 == 1):
        return(31)
    elif(y == 2 and leap_year == 1):
        return(29)
    elif(y == 2 and leap_year == 0):
        return(28)
    elif(y % 2 == 0):
        return(30)

def days_left(x, y, z):
    leap_year(year)
    x = 0
    for i in range(y):
        if(i % 2 == 1):
            x = x + 31
        elif(i % 2 == 0):
            x = x + 30 ##FIXIXIXIXIXIIX  
        elif(i == 2 and leap_year == 1):
            x = x + 29
        elif(i == 2 and leap_year == 0):
            x = x + 28          
    if(leap_year == 1):
        return(366 - x)
    elif(leap_year == 0):
        return(365 - x)
    
def number_of_days_left_month(x, y):
    leap_year(year)
    if(y % 2 == 1):
        return(31 - x)
    elif(y == 2 and leap_year == 1):
        return(29 - x)
    elif(y == 2 and leap_year == 0):
        return(28 - x)
    elif(y % 2 == 0):
        return(30 - x)
        
print("Please enter a date.")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))  
print("\nDate: " + str(month) + "/" + str(day) + "/" + str(year))

print("\nMenu: ")
print("1)	Calculate the number of days in the given month.")
print("2)	Calculate the number of days left in the given year.")
print("3)	Calulate the number of days left in the given month.\n")

menu = int(input("Would you like 1, 2, or 3?"))

if(menu == 1):
    number_of_days(day, month)
    print(number_of_days(day, month))
if(menu == 2):
    days_left(day, month, year)
    print(days_left(day, month, year))
if(menu == 3):
    number_of_days_left_month(day, month)
    print(number_of_days_left_month(day, month))
    
