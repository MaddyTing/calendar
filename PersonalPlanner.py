'''
In this program you will create a personal organizer. 
Using parallel arrays you will store the following information on 
each event in your organizer:

Month (1 - 12)
Day (1 - 31)
Year
Event name

If the user enters an incorrect month the month should be set to January.
If the user enters an incorrect day then the day should be set to 1.


Write the following methods:

Add an event
Print all events
Print events in a specific month

'''


'''
eventname = input("Enter the event name: ")
month = int(input("Month: "))
day = int(input("Day: "))
year = int(input("Year: "))
enterevent = input("Do you want to enter another date? NO to stop. ")
'''

eventlist = []
monthlist = []
daylist = []
yearlist = []
monthname = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    

def addtolist(eventname, month, day, year):
    eventlist.append(eventname)
    monthlist.append(month)
    daylist.append(day)
    yearlist.append(year)
 
def monthconversion(monthnum):
    return monthname[monthnum - 1]
'''
for x in range(len(eventlist)):
        if(str(monthlist[x]).find(str(specificmonth)) > -1):
            print(eventlist[x])
'''
def specmonth(specificmonth):
    print("\n********** Events in " + monthconversion(specificmonth) + " **********")

    for x in range(len(eventlist)):
        if(str(monthlist[x]).find(str(specificmonth)) > -1):
            print(eventlist[x])
            print("Date: " + monthconversion(monthlist[x]) + " " + str(daylist[x]) + ", " + str(yearlist[x]))

def addnewevent(eventname, month, day, year):
    #Checking validity of month, day, year
    if(month > 12 or month < 1):
        month = 1
    if(year < 1):
        year = 1
    if(month == 4 or month == 6 or month == 9 or month == 11 and day > 30):
        day = 1
    if(month == 2 and day > 29):
        day = 1
    if(day < 1 or day > 31):
        day = 1
    addtolist(eventname, month, day, year)

def printallevents():
    print("******************** List of Events ********************")
    for i in range(len(eventlist)):
        print(eventlist[i])
        print("Date: " + monthconversion(monthlist[i]) + " " + str(daylist[i]) + ", " + str(yearlist[i]))

##################  MAIN

eventname = input("Enter the event name: ")
month = int(input("Month: "))
day = int(input("Day: "))
year = int(input("Year: "))

addnewevent(eventname, month, day, year)
enterevent = input("Do you want to enter another date? NO to stop. ")

while(enterevent != "NO"):
    eventname = input("Enter the event name: ")
    month = int(input("Month: "))
    day = int(input("Day: "))
    year = int(input("Year: "))
    
    addnewevent(eventname, month, day, year)
    enterevent = input("Do you want to enter another date? NO to stop. ")

#### ONCE FINISHED
printallevents()

specificmonth = int(input("What month would you like to see? (Enter the month number) "))
specmonth(specificmonth)
