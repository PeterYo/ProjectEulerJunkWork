# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "ComPeter"
__date__ = "$Dec 10, 2016 7:17:02 AM$"

import math

def Euler1():
    sum = 0
    for num in range(0,1000):
        if num % 3 == 0:
            sum += num
        if num % 5 == 0:
            sum += num
        if num % 15 == 0: #this is to subtract out the 2nd time I will add any number by 15 since it is divisble by both 3 and 5
            sum -= num 
    return sum #this yield the correct answer

def Euler2(x):
    sum = 0
    a, b = 0, 1
    while a < x:
        a, b = b, a+b
        if(b % 2 ==0):
            sum += b
    return sum

def isPrime(n):
    if n == 1 or n == 2 or n == 3:
        return True
    for x in range(2, int(math.sqrt(n))+1):
        if(n % x == 0):
            return False
    return True

def Euler3(x):

    while not isPrime(x):
        for factor in range(2, int(math.sqrt(x)+1)):
            if isPrime(factor) and (x % factor == 0):
                x /= factor
                break

    return x

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def Euler4(x):
    retNum = 0;
    for value1 in range(10**(x-1), 10**(x)):
        for value2 in range(value1, 10**(x)):
            if(isPalindrome(value1*value2) and value1*value2 > retNum):
                retNum = value1*value2
    return retNum

def Euler5():
    for value in range(21,10000000000):
        if(value % 1000 == 0): #this was so I could monitor the progress, since these are really large numbers I wanted an indication of how far I'd gotten
            print(value)
        for divisor in range(2,21):
            if(value % divisor == 0):
                if divisor == 20:
                    return value
                else:
                    continue
            else:
                break
    
def Euler6():
    sumSq = 0
    sqSum = 0 
    for value in range(0,101):
        sumSq += value**2
        sqSum += value
        
    sqSum = sqSum**2
    
    return sqSum - sumSq
    
def Euler7():
    primeList = []
    for value in range(2,100000000000):
        if(isPrime(value)):
            primeList.append(value)
            if(len(primeList) > 10000):
                break
    return primeList[-1]

def Euler8():
    numToCheck = "731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243525849077116705560136048395864467063244157221553975369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474821663704844031998900088952434506585412275886668811642717147992444292823086346567481391912316282458617866458359124566529476545682848912883142607690042242190226710556263211111093705442175069416589604080719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606058861164671094050775410022569831552000559357297257163626956188267042825248360082325753042075296345"
    largestNum = 0
    saveIndex = 0
    
    for value in range(0,986):
        totalProd = 1
        for char in numToCheck[value:value+13]:
            totalProd *= int(char)
        
        if(totalProd > largestNum):
            largestNum = totalProd
            saveIndex = value
    
    return largestNum

def Euler9(): # a + b + sqrt(a + b) == 1000
    for value1 in range(3,1000):
        for value2 in range(value1,1000):
            cSquared = value1**2 + value2**2
            c = int(math.sqrt(cSquared))
            if(math.sqrt(cSquared) != c):
                continue
            if(value1 + value2 + c == 1000):
                print(str(value1) + " " + str(value2) + " " + str(c))
                return value1*value2*c

def Euler10(): #as a note, I could use my isPrime function, but it seems really wasteful since I will be recalculating the same prime numbers over and over again
    retVal = 0
    primeList = [2]
    for value in range(2,2000001):
        if( value % 1000 == 0):
            print(value)
        i = 0
        while(primeList[i] < int(math.sqrt(value)+1)):
            if(value % primeList[i] == 0):
                break
            else:
                i+=1
            
        if(primeList[i] > int(math.sqrt(value))): 
            primeList.append(value)    
            retVal += value
        
    return retVal
    
if __name__ == "__main__":
#    output = str (Euler1())
#    print ("Answer to Euler 1: " + output)
#    output = str (Euler2(4000000))
#    print ("Answer to Euler 2: " + output)
#    output = str (Euler3(600851475143))
#    print ("Answer to  3: " + output)
#    output = str(Euler4(3))
#    print("Answer to 4: " + output)
#    output = str(Euler5())
#    print("Answer to 5: " + output)
#    output = str(Euler6())
#    print("Answer to 6: " + output)
#    output = str(Euler7())
#    print("Answer to 7: " + output)
#    output = str(Euler8())
#    print("Answer to 8: " + output)
#    output = str(Euler9())
#    print("Answer to 9: " + output)
    output = str(Euler10())
    print("Answer to 10: " + output)
    output = str(Euler7())
    print("Answer to 7: " + output)
    


