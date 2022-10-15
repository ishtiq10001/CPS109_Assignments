from math import * # importing math module
from random import * #importing random module for shuffle

"""
This is a simple program that shows the user a bus schedule

User inputs a time and the program shows the bus schedule for that time
OR - user inputs a specific bus and the program gives the all the times the bus is scheduled for 
OR - user gets the whole bus schedule

Notes on using this program:

Enter the time in 24 hour and single/double digit format.
For example: 1 pm would simply be 13 and midnight would be 0

Enter bus number in this format with no spaces:
17D

The user can choose if the output should be in 24 hour or 12 hour format


"""
#explanation on what this program does and how to use it    


def bus_schedule(bus_list): #bus schedule, takes bus list [LIST] as an argument
    
    twentyFour_clock = False # time format, default is false, which is 12 hour format
    inp_clock = input("enter 0 for 12 hour and 1 for 24 hour clock for the output\n")
    def twentyFour(inp): # asking if the user wants a 24 hour clock or 12 hour clock
        if (inp == "0"): # if the user inputs 0, return false
            return False # which would mean the user wants a 12 hour clock as the output
        else:
            return True  # return true if the user inputs anything but 0  
    
    twentyFour_clock = twentyFour(inp_clock) #assigning the boolean value that was gotten from the user
    
    
    
    
             
    #letting the user decide whether they want the bus schedule for that hour
    #or if they want to enter the bus number and see at what times the bus is scheduled.        
    #or if they want to see the whole bus schedule
    inp_user = input("""enter 1 to enter the time to see what bus is scheduled then
enter 2 to enter the bus to see at what times it is scheduled
enter 3 for the whole bus schedule
-> """)

    #1
    if (inp_user == str(1)):#if user input is 1, promt them to input the hour of the bus schedule
        inp_time = int(input("""enter the hour of the day to see the bus schedule at
that hour(enter 6 for 6 am or 23 for 11 pm, etc): \n"""))
        try:
            if (inp_time < 12 and inp_time > 0):#time formatting, am if time is before noon and after midnight
                if (twentyFour_clock == False): #time formatting if the user chose a 12 hour clock 
                    print("All the buses for " + str(inp_time) + " am\n" + bus_list[int(inp_time)])
                elif (twentyFour_clock == True and int(inp_time) < 10):#time formatting if the user chose a 24 hour clock 
                    print("All the buses for 0" + str(inp_time) + "00 hours\n" + bus_list[int(inp_time)])
                elif (twentyFour_clock == True):#time formatting if the user chose a 24 hour clock
                    print("All the buses for " + str(inp_time) + "00 hours\n" + bus_list[int(inp_time)])
            elif (inp_time > 12 and inp_time < 24):#time formatting, pm if time is after noon and before midnight
                if (twentyFour_clock == True):
                    print("All the buses for " + str(inp_time) + "00 hours\n" + bus_list[int(inp_time)])#24 hour clock format
                elif (twentyFour_clock == False): #12 hour clock format 
                    print("All the buses for " + str(inp_time-12) + " pm\n" + bus_list[int(inp_time)])
                
            elif (inp_time == 0 or inp_time == 24):#time formatting, if time is midnight
                print("All the buses for mid night" + bus_list[0])
            elif (inp_time == 12):#time formatting, if time is noon
                print("All the buses for noon\n" + bus_list[0])
            elif (inp_time == "exit"):
                exit()
            else:#if time is invalid
                print("Invalid Time")

        except:# if the user inputs an invalid time, when time < 0 or time > 24
            print("enter a valid time in the format described above")
            
    #2             
    elif (inp_user == str(2)):#if user input is 1, promt them to input the bus number
        inp_bus = input("""enter the bus number to see when the bus is scheduled \n""") # user input
        counter = 0
        
        for char in bus_list:
            if str(inp_bus) in char:
                try:    
                    if (counter < 12 and counter > 0): #time formatting, output
                        if (twentyFour_clock == False): #time formatting, output
                            print(str(inp_bus) + " is scheduled at " +  str(counter) +  " am")

                        elif (twentyFour_clock == True and counter < 10): #time formatting
                            print(str(inp_bus) + " is scheduled at 0" + str(counter) +"00 hours")
                        elif (twentyFour_clock == True and counter >= 10):
                            print(str(inp_bus) + " is scheduled at " + str(counter) +"00 hours")

                                
                    elif (counter > 12 and counter < 24): #time formatting, output
                        if (twentyFour_clock == False):
                            print(str(inp_bus) + " is scheduled at " + str(counter-12) + " pm")
                            
                        elif (twentyFour_clock == True):
                            print(str(inp_bus) + " is scheduled at " + str(counter) + "00 hours")
                        
                            
                    elif (counter == 12): #time formatting, output
                        print(str(inp_bus) + " is scheduled at "+"noon")

                    elif (counter == 0): #time formatting, output
                        print(str(inp_bus) + " is scheduled at "+"midnight")
                except: #if the input format is wrong
                    pass
            counter += 1
    #3
    elif (inp_user == str(3)):
        counter = 0
        
        for char in bus_list: 
            if (counter < 12 and counter > 0): #time formatting, output
                if (twentyFour_clock == False): #time formatting, output
                    print("Buses for " + str(counter) +  " am: " + char)
                elif (twentyFour_clock == True and counter < 10): #time formatting, output
                    print("Buses for 0" + str(counter) +  "00 hours: " + char)
                elif (twentyFour_clock == True and counter): #time formatting, output
                    print("Buses for " + str(counter) +  "00 hours: " + char)
            elif (counter > 12 and counter < 24): #time formatting, output
                if (twentyFour_clock == False):  #time formatting, output
                    print("Buses for " + str(counter) +  " pm: " + char)
                elif (twentyFour_clock == True): #time formatting, output
                    print("Buses for " + str(counter) +  "00 hours: " + char)
            

            elif (counter == 12): #time formatting, output
                print("Buses for noon: " + char)

            elif (counter == 0): #time formatting, output
                print("Buses for midnight: " + char)
                   
            counter +=1
    #exception, wrong input format
    else:
        print("enter a valid input")
        bus_schedule()



if (__name__ == "__main__"):
    print("""
This is a simple program that gives the user some options to choose from
and solves that problem for them.

Bus Schedule List
- user inputs a time and the program shows the bus schedule for that time
OR - user inputs a specific bus and the program gives the times for that bus 
OR - user gets the whole bus schedule

Notes on using this program:
Enter the time in 24 hour and single digit format.
For example: 1 pm would simply be 13 and midnight would be 0

Enter bus number in this format with no spaces:
17D

The output is in in 12 hour format

""") #explains the user what this program does and instruction on how to use this app
    busList = ["70C,20B","19A,70C,15D","19B,19C,21D","17C,19A,21D",
                "16C,19A,21D","19A,21D","77A,21D,24A","9B,7B,12B",
                "67C,293,256C","7C,6D,5B","16C,9A,19C","19A,15D",
                "67C,181","9C,17C,15D","","17C,19A,21D",
                "6C,17B,12A","12B,17C","17C,15B","9C,7C,15D",
                "19B,19C,12D","19C,18D,17D","70C,20A,19B","19C,256"]
    #bus list where index is the time/hour
    #so the index 6 would refer to time 0600 (24 hour clock) or 6 am(12 hour clock)
    shuffle(busList) #nothing too dramatic, just a bus list randomizer
    #randomizing bus schedule so that its not the same every time
    while not False: 
        bus_schedule(busList) # calling our bus schedule function
        if input("press enter to continue or enter exit to quit\n") == "exit": 
            break #after the app has finished its job it asks the user if they want to exit the app or keep running
        else:
            pass #if the user doesnt want to exit, it just simply goes back to the loop and runs the app again
        
