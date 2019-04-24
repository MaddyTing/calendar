
##################  LISTS

eventlist = []
monthlist = []
daylist = []
yearlist = []
monthname = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
##################  FUNCTIONS

def addtolist(eventname, month, day, year):
    # Adds event name, month, day, and year to the proper list
    eventlist.append(eventname)
    monthlist.append(month)
    daylist.append(day)
    yearlist.append(year)
 
def addnewevent(eventname, month, day, year):
    # Checking validity of month, day, year, then adds event
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

def monthconversion(monthnum):
    # Converts month number to month name
    return monthname[monthnum]
    
def printallevents():
    # Prints all events
    print("******************** List of Events ********************")
    
    for i in range(len(eventlist)):
        print(eventlist[i])
        print("Date: " + monthconversion(monthlist[i]) + " " + str(daylist[i]) + ", " + str(yearlist[i]))

def specmonth(specificmonth):
    # Prints all events in the specified month
    print("\n********** Events in " + monthconversion(specificmonth) + " **********")

    for x in range(len(eventlist)):
        if(str(monthlist[x]).find(str(specificmonth)) > -1):
            print(eventlist[x])
            print("Date: " + monthconversion(monthlist[x]) + " " + str(daylist[x]) + ", " + str(yearlist[x]))


##################  MAIN   ##################

##################  ASKING USER FOR EVENTS

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

##################  PRINTING OUT LISTS - ALL EVENTS AND SPECIFIC MONTH

printallevents()

specificmonth = int(input("What month would you like to see? (Enter the month number) "))
specmonth(specificmonth)
