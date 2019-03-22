#Includes Option 3
#CodeSkulptor3 Link: https://py3.codeskulptor.org/#user303_b9J5sFwhPN_1.py

#DATE VALID/INVALID CHECK
def checkin(x, y, z):
#MONTH INVALID
    if(y > 12):
        return(False)
#DAY INVALID
    if(x < 1 or y < 1 or z < 1):
        return(False)
    if(y == 4 or y == 6 or y == 9 or y == 11 and x > 30):
        return(False)
    elif(x > 29 and y == 2 and leapyear == 1):
        return(False)
    elif(x > 28 and y == 2 and leapyear == 0):
        return(False)
    elif(x > 31):
        return(False)
            
#LEAP YEAR CHECK   
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
    for i in range(y - 1):
        if(i == 2 and leapyear == 1):
            x = x + 29
        elif(i == 2 and leapyear == 0):
            x = x + 28
        elif(i == 4 or i == 6 or i == 9 or i == 11):
            x = x + 30
        else:
            x = x + 31 
    if(leapyear == 1):
        return(366 - x)
    elif(leapyear == 0):
        return(365 - x)
    
#3 (extra)
def month_days_left(x, y, z):
    leapyear = leap_year(z)
    if(y == 2 and leapyear == 1):
        return(29 - x)
    elif(y == 2 and leapyear == 0):
        return(28 - x)
    elif(y == 4 or y == 6 or y == 9 or y == 11): 
        return(30 - x)
    else:
        return(31 - x)

#MAIN
print("Please enter a date.")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))  

#DATE VALID/INVALID CHECK
checkin(day, month, year)
while (checkin(day, month, year) == False):
    print("\nYour date was invalid. Please try again.\n")
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))  
    checkin(day, month, year)

#PRINT DATE
print("\nDate: " + str(month) + "/" + str(day) + "/" + str(year))

#MENU
print("\nMenu: ")
print("1)	Calculate the number of days in the given month.")
print("2)	Calculate the number of days left in the given year.")
print("3)	Calulate the number of days left in the given month.\n")

menu = int(input("Would you like 1, 2, or 3?"))

#MENU ACTION
print("You chose Option " + str(menu) + "\n")
if(menu == 1):
    print("Number of days in month " + str(month) + " in year " + str(year) + ":")
    print(number_of_days(month, year))
if(menu == 2):
    print("Number of days left in year " + str(year) + ":")
    print(days_left(day, month, year))
if(menu == 3):
    print("Number of days left in month " + str(month) + " in year " + str(year) + ":")
    print(month_days_left(day, month, year))

