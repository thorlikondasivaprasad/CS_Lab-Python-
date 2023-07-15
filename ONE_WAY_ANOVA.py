import pandas as pd
import numpy as np
import scipy.stats as ss

k = int(input("Enter the number of Treatments: "))
Treatment = input("Enter name of the Treatments: ")

Data = []
for i in range(k):
    a = np.array([float(j) for j in input(f"Enter {Treatment} {i+1} values: ").strip().split()])
    Data.append(a)

Data = np.array(Data)

alpha = float(input("Enter Level of Significance: "))

print(f"\nNull Hypothesis (H0): There is Homogenity among the {Treatment}s")
print(f"Alternate Hypothesis (H1): There is Heterogenity among the {Treatment}s\n")

# Total No. of values (N):
# Sum of Treatments (Ti):
# Row sum of squares (RSS):
N = Ti = Ti2 = RSS = 0
for i in Data:
    Ti += sum(i)
    Ti2 += sum(i)**2 / len(i)
    RSS += sum(i**2)
    N += len(i)

# Correction Factor (CF):
CF = Ti**2 / N

# Sum of Squares due to Total (SST):
SST = RSS - CF
# Sum of Squares due to Treatments (SSTr):
SSTr = Ti2 - CF
# Sum of Squares due to Error (SSE):
SSE = SST - SSTr

# Mean Sum of Squares due to Treatments (MeanSSTr):
MeanSSTr = SSTr/(k-1)
# Mean Sum of Squares due to Error (MeanSSE):
MeanSSE = SSE/(N-k)

# F calculated value:
Fcal = MeanSSTr / MeanSSE

# F table value:
FTable = ss.f.ppf(1-alpha, k-1, N-k)

# Degrees of Freedom:
DOF = f"~ F({k-1},{N-k})"

if(Fcal < 1):
    Fcal = 1 / Fcal
    FTable = ss.f.ppf(1-alpha, N-k, k-1)
    DOF = f"~ F({N-k},{k-1})"

print("Sum of Squares due to Total (SST): {:.4f}".format(SST))
print("Sum of Squares due to Treatments (SSTr): {:.4f}".format(SSTr))
print("Sum of Squares due to Error (SSE): {:.4f}\n".format(SSE))

print("Mean Sum of Squares due to Treatments (Mean SSTr): {:.4f}".format(MeanSSTr))
print("Mean Sum of Squares due to Error (Mean SSE): {:.4f}\n".format(MeanSSE))

ANOVA_One_Way_Classification_Table = {
    "S O V": [Treatment, "Error", "Total"],
    "S O S": ["{:.4f}".format(SSTr), "{:.4f}".format(SSE), "{:.4f}".format(SST)],
    "D O F": [k-1, N-k, N-1],
    "M S O S": ["{:.4f}".format(MeanSSTr), "{:.4f}".format(MeanSSE), " - "],
    "V R": ["F-cal = {:.4f}".format(Fcal), DOF, ""]}

data_frame = pd.DataFrame(ANOVA_One_Way_Classification_Table)

print("ANOVA One Way Classification Table:")
print(data_frame)

print("\nF-Calculated value: {:.4f}".format(Fcal))
print("F-Table value: {:.4f}\n".format(FTable))

if Fcal < FTable :
    print(f"We Accept H0\nThere is Homogeneity among the {Treatment}s")
else:
    print(f"We Reject H0\nThere is Heterogeneity among the {Treatment}s")


Output::



Enter the number of Treatments: 4
Enter name of the Treatments: Technician
Enter Technician 1 values: 6 14 10 8 11
Enter Technician 2 values: 14 9 12 10 14
Enter Technician 3 values: 10 12 7 15 11
Enter Technician 4 values: 9 12 8 10 11
Enter Level of Significance: 0.01

Null Hypothesis (H0): There is Homogenity among the Technicians
Alternate Hypothesis (H1): There is Heterogenity among the Technicians

Sum of Squares due to Total (SST): 114.5500
Sum of Squares due to Treatments (SSTr): 12.9500
Sum of Squares due to Error (SSE): 101.6000

Mean Sum of Squares due to Treatments (Mean SSTr): 4.3167
Mean Sum of Squares due to Error (Mean SSE): 6.3500

ANOVA One Way Classification Table:
        S O V     S O S  D O F M S O S             V R
0  Technician   12.9500      3  4.3167  F-cal = 1.4710
1       Error  101.6000     16  6.3500       ~ F(16,3)
2       Total  114.5500     19      -                 

F-Calculated value: 1.4710
F-Table value: 26.8269

We Accept H0
There is Homogeneity among the Technicians
