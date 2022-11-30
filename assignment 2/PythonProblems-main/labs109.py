# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":
import random
import math
from collections import deque
from fractions import Fraction

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



def only_odd_digits(n): #question 4
    for i in str(n):
        if (int(i) % 2 == 0):
            return False
        else:
            if len(str(n)):
                pass

    return True

def knight_jump(knight, start, end): #question 17
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


def tukeys_ninthers(items): # question 27
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

def candy_share(candies): #question 39
    counter = 0
    while True:
        cand_i = []
        for i in range(len(candies)):
            if candies[i] > 1:
                cand_i.append(i)
        if len(cand_i) == 0:
            return counter
        for j in cand_i:
            if j == 0:
                candies[j] -= 2
                candies[j+1] +=1
                candies[-1] +=1
            elif j == len(candies)-1:
                candies[j] -= 2
                candies[j-1] +=1
                candies[0] +=1
            else:
                candies[j] -= 2
                candies[j+1] +=1
                candies[j-1] +=1
        counter +=1

def remove_after_kth(items,k): #question 45
    item_dict = {}
    r_list = []
    counter = 0
    for i in items:
        if i in item_dict:
            counter = item_dict[i]
            counter +=1
            item_dict[i] = counter
            if counter <= k:
                r_list.append(i)

        else:
            item_dict[i] = 1
            counter = item_dict[i]
            if counter <= k:
                r_list.append(i)
    return(r_list)

def calkin_wilf(n): #question 57
    p = 1
    q = 1
    deq_frac = deque()
    deq_frac.append(Fraction(p/q))

    for i in range(n):
        g = Fraction(deq_frac.popleft())

        p = Fraction(g.numerator)
        q = Fraction(g.denominator)
        deq_frac.append(p/(p+q))
        deq_frac.append((p+q)/q)

        #
        if i == n-1:
            return g

def postfix_evaluate(items): #question 62
    itms_new = []
    a = 1

    for i in items:
        if type(i) is int:
            itms_new.append(i)
            a = i
        else:
            if i == '+':
                a = itms_new.pop(-2) + itms_new.pop(-1)

            elif i == '*':
                a = itms_new.pop(-2) * itms_new.pop(-1)

            elif i == '-':
                a = itms_new.pop(-2) - itms_new.pop(-1)

            elif i == '/':
                p = itms_new.pop(-2)
                q = itms_new.pop(-1)
                if q == 0:
                    a = 0
                else:
                    a = p // q
            itms_new.append(a)

    return itms_new[0]
