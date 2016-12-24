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

def Euler11(): #could use some pretty-ing up
    
    rowIndex = 0
    columnIndex = 0
    returnProd = 0
    inputRows = []
    multCount = 0
    
    inputRows.append("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08")
    inputRows.append("49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00")
    inputRows.append("81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65")
    inputRows.append("52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91")
    inputRows.append("22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80")
    inputRows.append("24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50")
    inputRows.append("32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70")
    inputRows.append("67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21")
    inputRows.append("24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72")
    inputRows.append("21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95")
    inputRows.append("78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92")
    inputRows.append("16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57")
    inputRows.append("86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58")
    inputRows.append("19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40")
    inputRows.append("04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66")
    inputRows.append("88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69")
    inputRows.append("04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36")
    inputRows.append("20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16")
    inputRows.append("20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54")
    inputRows.append("01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")
    
    totalGrid = [line.split() for line in inputRows]
    totalGrid = [[int(text) for text in line] for line in totalGrid]
    print(totalGrid)
    
    while(rowIndex < 20):
        while(columnIndex < 20):
            if(columnIndex < 17):
                multCount +=1
                prod = 1
                i = 0
                while(i<4):
                    prod *= totalGrid[rowIndex][columnIndex+i]
                    i+=1
                if(prod > returnProd):
                    returnProd = prod
            if(rowIndex < 17):
                multCount +=1
                prod = 1
                i = 0
                while(i<4):
                    prod *= totalGrid[rowIndex+i][columnIndex]
                    i+=1
                if(prod > returnProd):
                    returnProd = prod
            if(rowIndex < 17 and columnIndex < 17):
                multCount +=1
                prod = 1
                i = 0
                while(i<4):
                    prod *= totalGrid[rowIndex+i][columnIndex+i]
                    i+=1
                if(prod > returnProd):
                    returnProd = prod
            if(rowIndex > 3 and columnIndex < 17):
                multCount +=1
                prod = 1
                i = 0
                while(i<4):
                    prod *= totalGrid[rowIndex-i][columnIndex+i]
                    i+=1
                if(prod > returnProd):
                    returnProd = prod
            columnIndex +=1
        columnIndex = 0
        rowIndex +=1
    return returnProd

    

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
#    output = str(Euler10())
#    print("Answer to 10: " + output)
    output = str(Euler11())
    print("Answer to 11: " + output)
    


