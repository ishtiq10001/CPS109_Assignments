import random
import math

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



# def candy_share(candies): #question 39
#     counter = 0
#     new_candies = candies
#
#     i=0
#     while True:
#         for x in candies:
#             if x > 1:
#                 #print(i)
#                 if i != 0 and i != len(candies)-1:
#                     new_candies[i] -= 2
#                     new_candies[i+1] +=1
#                     new_candies[i-1] +=1
#
#                 elif i == 0:
#                     new_candies[i] -= 2
#                     new_candies[i+1] +=1
#                     new_candies[-1] += 1
#                 elif i == len(candies) -1:
#                     new_candies[i] -= 2
#                     new_candies[i-1] +=1
#                     new_candies[0] += 1
#
#                 else:
#                     return new_candies
#                 i+=1
#             else:
#                 i+=1
#
#         i = 0
#         counter +=1
#         #print(candies)
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


def remove_after_kth(items,k):
    g = {}
    count1 = 0
    for i in items:
        count1 = g[i].value()
        count1+=1
        g[i]=count1
        print(i)

    print(g)












if __name__ == "__main__":
    #print(question_4("13592"))
    #print(question_17((2, 1),(12, 10),(11, 12)))
    #print(question_27([99, 42, 17, 7, 1, 9, 12, 77, 15]))
    print(candy_share([5, 1, 0, 0, 0, 0, 0, 1, 0]))
    remove_after_kth([0,1,0,1],2)
