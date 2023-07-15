import pandas as pd
import numpy as np
import scipy.stats as ss

def mymean(data):
    Sum = 0
    for i in data:
        Sum += i

    return Sum/len(data)

k = int(input("Enter the number of Treatments: "))
h = int(input("Enter the number of Blocks: "))

Treatment = input("Enter name of the Treatments: ")
Block = input("Enter name of the Blocks: ")

Data = []
for i in range(k):
    row = []
    while len(row) != h:
        row = np.array([float(i) for i in input(f"Enter {Treatment} {i+1} values: ").strip().split()])
    Data.append(row)

Data = np.array(Data)

alpha = float(input("Enter Level of Significance: "))

print(f"\nHypothesis Related to {Treatment}s:")
print(f"Null Hypothesis (H0): There is Homogenity among the {Treatment}s")
print(f"Alternate Hypothesis (H1): There is Heterogenity among the {Treatment}s")

print(f"\nHypothesis Related to {Block}s:")
print(f"Null Hypothesis (H0): There is Homogenity among the {Block}s")
print(f"Alternate Hypothesis (H1): There is Heterogenity among the {Block}s\n")

# Total no. of values (N):
N = k * h

# Sum of Treatments (Ti):
Ti = np.array([sum(i) for i in Data])
Ti2 = Ti**2
SumTi2 = sum(Ti2)

# Sum of Blocks (Bj):
Bj = Data[0]
for i in range(1,k):
    Bj = Bj + Data[i]

Bj2 = Bj**2
SumBj2 = sum(Bj2)

# Grand Total (G):
G = sum(Ti)

# Row Sum of Squares (RSS):
RSS = 0
for i in Data:
    for j in i:
        RSS += j**2

# Correction Factor (CF):
CF = G**2 / N

# Sum of Squares due to Total (SST):
SST = RSS - CF
# Sum of Squares due to Treatments (SSTr):
SSTr = SumTi2/h - CF
# Sum of Squares due to Blocks (SSB):
SSB = SumBj2/k - CF
# Sum of Squares due to Error (SSE):
SSE = SST - SSTr - SSB

# Mean Sum of Squares due to Treatments (MeanSSTr):
MeanSSTr = SSTr/(k-1)
# Mean Sum of Squares due to Blocks (MeanSSB):
MeanSSB = SSB/(h-1)
# Mean Sum of Squares due to Error (MeanSSE):
MeanSSE = SSE/((k-1)*(h-1))

# F calculated value of Treatments (F(Tr)):
F_Tr_cal = MeanSSTr / MeanSSE
# F calculated value of Blocks (F(B)):
F_B_cal = MeanSSB / MeanSSE

# F table value of Treatments:
F_Tr_Table = ss.f.ppf(1-alpha, k-1, (k-1)*(h-1))
# F table value of Blocks:
F_B_Table = ss.f.ppf(1-alpha, h-1, (k-1)*(h-1))

# Degrees of Freedom for Treatments:
F_Tr_DOF = f"~ F({k-1},{(k-1)*(h-1)})"
# Degrees of Freedom for Blocks:
F_B_DOF = f"~ F({h-1},{(k-1)*(h-1)})"

if F_Tr_cal < 1:
    F_Tr_cal = 1 / F_Tr_cal
    F_Tr_Table = ss.f.ppf(1-alpha,(k-1)*(h-1), k-1)
    F_Tr_DOF = f"~ F({(k-1)*(h-1)},{k-1})"

if F_B_cal < 1:
    F_B_cal = 1 / F_B_cal
    F_B_Table = ss.f.ppf(1-alpha,(k-1)*(h-1), h-1)
    F_B_DOF = f"~ F({(k-1)*(h-1)},{h-1})"

if F_Tr_cal < F_Tr_Table:
    print(f"We Accept H0(Tr)\nThere is Homogeneity among the {Treatment}s")
else:
    print(f"We Reject H0(Tr)\nThere is Heterogeneity among the {Treatment}s")

if F_B_cal < F_B_Table:
    print(f"We Accept H0(B)\nThere is Homogeneity among the {Block}s\n")
else:
    print(f"We Reject H0(B)\nThere is Heterogeneity among the {Block}s\n")
