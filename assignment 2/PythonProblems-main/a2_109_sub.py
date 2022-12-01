import random
import math
from collections import deque
from fractions import Fraction
def question_4(n):
    for i in n:
        if (int(i) % 2 == 0):
            return False
        else:
            if len(n):
                pass

    return True

def question_17(knight, start, end):
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

def med(L):
    a = L[0]
    b = L[1]
    c = L[2]
    if (a >= b or a >= c) and (a <= c or a <= b):
        return a        #a is the median
    elif (b >= a or b >= c) and (b <= a or b <= c):
        return b
    elif (c >= b or c >= a) and (c <= a or c <= b):
        return c
    else:
        return


def question_27(L):
    temp = []
    if len(L) == 1:
        return L[0]

    else:
        temp = med(L)

        L = L[3:len(L)]
        L.append(temp)
        return question_27(L)




def candy_share(candies):
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


def remove_after_kth(items,k):#question 45
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


def calkin_wilf(n):#question 57

    p = 1
    q = 1
    a = deque()
    a.append(Fraction(p/q))

    for i in range(n):
        g = Fraction(a.popleft())

        p = Fraction(g.numerator)
        q = Fraction(g.denominator)
        a.append(p/(p+q))
        a.append((p+q)/q)

        #
        if i == n-1:
            return g


def postfix_evaluate(items):#question 62
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
            print(itms_new)
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
        while True:#run the loop as long as digit is more than 0, 9 is compared first because it has the most weight
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

def frequency_sort(items):
    n = {}
    s = {}
    g = []
    for ind in items:
        elem = items.count(ind)
        if ind not in n:
            n[ind] = elem

    s = sorted(n.items(), key=lambda x:x[1],reverse=True)
    print(s)
    for i in s:
        s1 = i[1]
        for j in range(s1):
            g.append(i[0])

    return g



if __name__ == "__main__":
    #print(question_4("13592"))
    #print(question_17((2, 1),(12, 10),(11, 12)))
    #print(question_27([99, 42, 17, 7, 1, 9, 12, 77, 15]))
    #print(candy_share([5, 1, 0, 0, 0, 0, 0, 1, 0]))
    #print(remove_after_kth([1, 1, 1, -4], 1))
    #print(calkin_wilf(1000))
    #print(postfix_evaluate([4, 5, 7, '*', '/']))
    #print(4//35)
    #print(sort_by_digit([111, 19, 919, 1199, 911,999]))
    print(frequency_sort(['bob','bob','carl','alex','bob']))
