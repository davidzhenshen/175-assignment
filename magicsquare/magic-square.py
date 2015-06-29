#magic square
import math
def row(strings):
    sum1 = 0
    for i in range(0,len(strings)):
        for j in range(0, len(strings)):
            sum1 = sum1 + int(strings[i][j+j])
        return sum1 == (len(strings)*(len(strings)*len(strings)+1))/2
    
def column(strings):
    sum2 = 0
    for i in range(0,len(strings)):
        for j in range(0,len(strings)):
            sum2 = sum2 + int(strings[j][i+i])
        return sum2 == (len(strings)*(len(strings)*len(strings)+1))/2
        
def diagonal(strings):
    sum3 = 0
    for i in range(0,len(strings)):
        sum3 = sum3 + int(strings[i][i+i])
    return sum3 == (len(strings)*(len(strings)*len(strings)+1))/2
    for i in range(0, len(strings)):
        sum3 = sum3 + int(strings[i][4-2*i])
    return sum3 == (len(strings)*(len(strings)*len(strings)+1))/2    

def checkall(strings):
    valid = True
    if row(strings) and column(strings) and diagonal(strings)== True:
        return valid
    else:
        valid = False
    return valid
        

file = open('4x4-good.txt', 'r')
lines = file.readlines()

print(checkall(lines))
