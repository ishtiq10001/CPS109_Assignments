from math import *
from random import *

"""
This is a simple program that gives the user some options to choose from
and solves that problem for them. The problems are:
1) Bus Schedule List
- User inputs a time and the program shows the bus schedule for that time
OR - user inputs a specific bus and the program gives the times for that bus 
2) To do list
- User inputs tasks then the program creates a list for them
3) Random Name Selector
- Selects a random name from a given list
4) Weather status at a given time
- User a time and the program gives the user the weather status at that time
5) Average Calculator
- Calculates the average for the user
"""

def bus_schedule():
    #bus list where index is the time/hour
    bus_list = ["70C,20B","19A,70C,15D","19B,19C,21D","17C,19A,21D",
                "16C,19A,21D","19A,21D","77A,21D,24A","9B,7B,12B",
                "67C,293,256C","7C,6D,5B","16C,9A,19C","19A,15D",
                "67C,181","9C,17C,15D","","17C,19A,21D",
                "6C,17B,12A","12B,17C","17C,15B","9C,7C,15D",
                "19B,19C,12D","19C,18D,17D","70C,20A,19B","19C,256"]
                #so the index 6 would refer to time 0600 (24 hour clock) or 6 am(12 hour clock)

    #letting the user decide whether they want the bus schedule at a time or
    #they want to enter the bus number and see at what times there is that bus.        
    inp_user = input("enter 1 for enter the time and 2 for the bus you're looking for: ")

    
    if (inp_user == str(1)):#if user input is 1, promt them to input the hour of the bus schedule
        inp_time = int(input("""enter the hour of the day to see the bus schedule at
that hour(enter 6 for 6 am or 23 for 11 pm): \n"""))
        if (inp_time < 12 and inp_time > 0):#time formatting, am if time is before noon and after midnight
            print("All the buses for " + str(inp_time) + " am\n" + bus_list[int(inp_time)])
        elif (inp_time > 12 and inp_time < 24):#time formatting, pm if time is after noon and before midnight
            print("All the buses for " + str(inp_time) + " pm\n" + bus_list[int(inp_time)])
        elif (inp_time == 0 or inp_time == 24):#time formatting, if time is midnight
            print("All the buses for mid night" + bus_list[0])
        elif (inp_time == 12):#time formatting, if time is noon
            print("All the buses for noon\n" + bus_list[0])
        else:#if time is invalid
            print("Invalid Time")
            
                    
        
    elif (inp_user == str(2)):
        inp_bus = input("""enter the bus number to see when the bus scheduled \n""")
        counter = 0
        for char in bus_list:
            if inp_bus in char:
                print(inp_bus + " in " +  str(counter))
            counter += 1
                
                


        
    else:
        print("enter a valid input")
        bus_schedule()



if (__name__ == "__main__"):
    bus_schedule()
