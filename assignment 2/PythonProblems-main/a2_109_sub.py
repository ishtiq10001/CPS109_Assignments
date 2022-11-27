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
 
            
    
#def candy_share(candies): #question 39
    #pass



def nearest_smaller(items):
    n = items
    while True:
        for i in range(len(items)):
            
            if (n[i] > n[i+1]):
                n[i]
            
        
            
        

    
    
    
    

if __name__ == "__main__":
    #print(question_4("13592"))
    #print(question_17((2, 1),(12, 10),(11, 12)))
    #print(question_27([99, 42, 17, 7, 1, 9, 12, 77, 15]))
    #print(candy_share([5, 1, 0, 0, 0, 0, 0, 1, 0]))
    
