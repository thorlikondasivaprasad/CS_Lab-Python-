import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import scipy.stats as ss
import pandas as pd

def mylen(data):
    size = 0
    for i in data:
        size = size + 1
    return size

def mysum(data):
    Sum = 0
    for i in data:
        Sum += i
    return Sum

def mymean(data):
    Sum = 0
    n = mylen(data)
    for i in data:
        Sum += i
    return Sum/n
    
def Rankify(data):
    N = len(data)
    
    Ranks = [None for i in range(N)]
 
    for i in range(N):
        BigNums = 1
        SameNums = 0
 
        # Count no of bigger elements from 0 to current number-1
        for j in range(i):
            if (data[j] > data[i]):
                BigNums += 1
            if (data[j] == data[i]):
                SameNums += 1
 
        # Count no of bigger elements from current number+1 to N-1
        for j in range(i+1, N):
            if (data[j] > data[i]):
                BigNums += 1
            if (data[j] == data[i]):
                SameNums += 1
 
        # Use Fractional Rank formula
        # fractional_rank = BigNums + SameNums/2
        Ranks[i] = BigNums + SameNums/2

    return Ranks

def RemDups(data):
    RemDups = []
    
    for i in data:
        if i not in RemDups:
            RemDups.append(i)
            
    return RemDups

def CF(x,y):
    cf = 0
    
    x = list(x)
    y = list(y)
    
    RemDups_x = RemDups(x)
    RemDups_y = RemDups(y)
    
    for i in RemDups_x:
        count = x.count(i)
        if count > 1:
            cf += (count * (count**2 - 1)) / 12
            
    for i in RemDups_y:
        count = y.count(i)
        if count > 1:
            cf += (count * (count**2 - 1)) / 12
    
    return cf

def SRCC(x, y):
    n = len(x)
    m = len(y)

    if n != m:
        print("Invalid Data: ")
        return
    
    RankX = np.array(Rankify(x))
    RankY = np.array(Rankify(y))
    
    # Difference of Ranks:
    Di = np.subtract(RankX, RankY)
    DiSq = np.square(Di)
    
    SumDiSq = mysum(DiSq)
    
    # Correction Factor:
    cf = CF(x,y)
    SumDiSq += cf

    SRCC = 1 - ((6 * SumDiSq) / (n * (n**2 - 1)))
    
    data = {
        "X values": x,
        "Y values": y,
        "Ranks of X": RankX,
        "Ranks of Y": RankY,
        "Di values": Di,
        "Di sq. values": DiSq,
    }
    
    dataframe = pd.DataFrame(data)
    print(dataframe)
    
    print("Correction Factor: ",cf)
    print("Sum of Di sq. = ",SumDiSq)
    print(f"The Spearman's Ranked Correlation Coefficient of the given data = {SRCC}")
    
x = np.array([float(i) for i in input("Enter x values: ").strip().split()])
y = np.array([float(i) for i in input("Enter y values: ").strip().split()])

# x = np.array([68, 64, 75, 50, 64, 80, 75, 40, 55, 64])
# y = np.array([62, 58, 68, 45, 81, 60, 68, 48, 50, 70])

SRCC(x, y)    
