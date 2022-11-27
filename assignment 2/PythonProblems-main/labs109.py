# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":
import random
import math


##def ryerson_letter_grade(n):
##    if n < 50:
##        return 'F'
##    elif n > 89:
##        return 'A+'
##    elif n > 84:
##        return 'A'
##    elif n > 79:
##        return 'A-'
##    tens = n // 10
##    ones = n % 10
##    if ones < 3:
##        adjust = "-"
##    elif ones > 6:
##        adjust = "+"
##    else:
##        adjust = ""
##    return "DCB"[tens - 5] + adjust



def only_odd_digits(n):
    for i in str(n):
        if (int(i) % 2 == 0):
            return False
        else:
            if len(str(n)):
                pass

    return True

def knight_jump(knight, start, end):
    l_knight = list(knight)
    d = 0
    for i in range(len(start)):
        d = abs(start[i]-end[i])
        if d in l_knight:
            l_knight.pop(l_knight.index(d))
            if len(l_knight) == 0:
                return True
            
        else:
            return False

        
def tukeys_ninthers(items):
    def med(L):#finds the median between 3 numbers
        a = L[0]
        b = L[1]
        c = L[2]
        if (a >= b or a >= c) and (a <= c or a <= b):
            return a        #a is the median
        elif (b >= a or b >= c) and (b <= a or b <= c):
            return b        #b is the median
        elif (c >= b or c >= a) and (c <= a or c <= b):
            return c        #c is the median
        else:
            return          #return none in any other case
    #not the wisest to have a function inside a function but
        #idk if we're allowed to use functions outside our problem function
    L = items
    temp = []
    if len(L) == 1:
        return L[0]

    else:
        temp = med(L)
        L = L[3:len(L)]
        L.append(temp)
        return tukeys_ninthers(L)
     
          


