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




if __name__ == "__main__":
    #print(question_4("13592"))
    #print(question_17((2, 1),(12, 10),(11, 12)))
    #print(question_27([99, 42, 17, 7, 1, 9, 12, 77, 15]))
    #print(candy_share([5, 1, 0, 0, 0, 0, 0, 1, 0]))
    #print(remove_after_kth([1, 1, 1, -4], 1))
    print(calkin_wilf(1000))
