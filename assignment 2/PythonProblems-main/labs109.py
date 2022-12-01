# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":
import random
import math
from collections import deque
from fractions import Fraction
'''
Questions 4,12,17,27,39,45,57,62,77,85
'''

def only_odd_digits(n): #question 4
    for i in str(n):
        if (int(i) % 2 == 0):
            return False
        else:
            if len(str(n)):
                pass

    return True

def give_change(amount,coins): #question 12
    curr_a = amount #current amount
    change = []
    for i in coins:
        num_c = curr_a // i
        if num_c <= 0:
            continue
        else:
            curr_a -= num_c*i
            for n in range(num_c):
                change.append(i)

    return change

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

def sort_by_digit_count(items): #question 77
    dig = 9 #digit we are comparing
    counter = 0 #counter to keep track of the index
    temp = 0 # temp variable to store the prev element
    t_sorted = 0 #how many times we've passed through the loop without sorting
    if len(items) == 1:
        return items
    while True:#run the loop as long as we want
        dig = 9 #reset digit at the start of the loop
        if counter > len(items)-2: #if index is the 2nd last
            counter = 0 #reset counter
        if t_sorted == len(items):#if the number of times we've gone through the list without sorting is
            break                   #equal to the number of items, that means we have sorted everything
        while True:#run the loop as long as digit is more than -1, 9 is compared first because it has the most weight
            if dig == -1:
                if p == q:
                    if items[counter] > items [counter+1]:
                        temp = items[counter]
                        items[counter] = items[counter+1]
                        items[counter+1] = temp
                    break
            curr = [int(x) for x in str(items[counter])] #splitting the integer into a list so that we can count how many digit nums we have
            next = [int(x) for x in str(items[counter+1])] #splitting the next integer into a list so that we can count how many digit nums we have
            p = curr.count(dig) # digit count
            q = next.count(dig) # the next elements digit count

            if p > q: # if the current element is greater than the next, than swap
                temp = items[counter]
                items[counter] = items[counter+1]
                items[counter+1] = temp
                t_sorted = 0 #reset the times we've not sorted
                break
            elif p == q: # if they have the same number of the current digit
                dig -= 1 #move to the next(or previous) digit
                continue
            else: #if it is already sorted
                t_sorted+=1 #add to the times we've not sorted
                break
        counter+=1 #keeping track of the index
    return items

def frequency_sort(items):#question 85
    items.sort() #sorting the items before hand to ensure the order of items in case of the frequency being the same
    count_dict = {}
    unsorted_list = []
    sorted_list = []
    temp = (0,0)
    if len(items) == 1:
        return items

    for ind in items:
        elem = items.count(ind)
        if ind not in count_dict:
            count_dict[ind] = elem

    for k,v in count_dict.items():
        unsorted_list.append((k,v))


    for sr in range(len(unsorted_list)):
        for m in range(sr+1, len(unsorted_list)):
            if unsorted_list[sr][1]<unsorted_list[m][1]:
                temp = unsorted_list[sr]
                unsorted_list[sr] = unsorted_list[m]
                unsorted_list[m] = temp
            elif unsorted_list[sr][1]==unsorted_list[m][1]:
                if unsorted_list[sr][0]>unsorted_list[m][0]:
                    temp = unsorted_list[sr]
                    unsorted_list[sr] = unsorted_list[m]
                    unsorted_list[m] = temp

    for i in unsorted_list:
        for j in range(i[1]):
            sorted_list.append(i[0])
    return sorted_list
