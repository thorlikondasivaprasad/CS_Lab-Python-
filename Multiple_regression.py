# Multiple Linear Regression Model:

import numpy as np
import scipy.stats as ss
from math import sqrt

def mymean(data):
    return sum(data)/len(data)

def GoodnessOfFit(y , Yfitted, alpha, Beta):
    print("\nTo Test Goodness of Fit using Determination of Coefficients (R2):")

    ybar = mymean(y)
    Residual = y - Yfitted
    y_ybar = y-ybar

    SSE = sum(Residual**2)
    SST = sum(y_ybar**2)
    SSR = SST - SSE

    Rsq = SSR/SST

    print(f"Coefficient of Determination (R2): {Rsq}")

    if Rsq < 0.9:
        print("The Multiple Regression Model is Not a Good Fit for the given data.")
    else:
        print("The Multiple Regression Model is a Good Fit for the given data.")

    print("\nTo Test Goodness of Fit using ANOVA:")
    n = len(y)
    p = len(Beta)

    MeanSSR = SSR/(p-1)
    MeanSSE = SSE/(n-p)

    Fcal = MeanSSR/MeanSSE
    F_table = ss.f.ppf(1-alpha, p-1, n-p)

    if Fcal < 1:
        Fcal = 1 / Fcal
        F_table = ss.f.ppf(1-alpha, n-p, p-1)

    if Fcal < F_table:
        print(f"Fcal < F-Table ({round(Fcal,4)} < {round(F_table,4)})")
        print("The Multiple Regression Model is Not a Good Fit for the given data.")
    else:
        print(f"Fcal > F-Table ({round(Fcal,4)} < {round(F_table,4)})")
        print("The Multiple Regression Model is a Good Fit for the given data.")

    return SSE

def ParameterTesting(XTX_inverse, alpha, Beta, SSE, DOF):
    print("\nTest for individual parameters:")

    T_table = ss.t.ppf(q = 1 - alpha/2, df = DOF)
    Tcal = []

    for i in range(len(Beta)):
        Tcal.append(Beta[i] / sqrt(SSE/DOF * XTX_inverse[i][i]))

        if Tcal[i] < T_table:
            print(f"Beta {i} is Not contributing to the model.")
        else:
            print(f"Beta {i} is contributing to the model.")

def mat_multiply(mat1, mat2):
    if mat1.shape[1] != mat2.shape[0]:
        print("Cannot multiply the matrices!!")
        return

    mat3 = np.zeros([mat1.shape[0],mat2.shape[1]], dtype=float)

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                mat3[i][j] += mat1[i][k] * mat2[k][j]

    return mat3

def mat_transpose(mat):
    result = np.zeros((mat.shape[1], mat.shape[0]), dtype=float)

    for i in range(mat.shape[0]):
       for j in range(mat.shape[1]):
           result[j, i] = mat[i, j]

    return result

X_dim = int(input("Enter number of X variables: "))

Y = np.array([[float(j)] for j in input(f"Enter Y values: ").strip().split()])

X = [np.array([1 for i in range(len(Y))])]
for i in range(1, X_dim):
    X_row =  np.array([float(j) for j in input(f"Enter X{i} values: ").strip().split()])
    X.append(X_row)

X = np.array(X)

alpha = float(input("Enter Level of Significance: "))

XTX = mat_multiply(X,mat_transpose(X))

XTX_inv = np.linalg.inv(XTX)

XTY = mat_multiply(X,Y)

result = mat_multiply(XTX_inv,XTY)

Beta = []
for i in result:
  Beta.append(i[0])

Beta = np.array(Beta)

Yfitted = 0
for i in range(len(X)):
    Yfitted += Beta[i]*X[i]

print("\nThe Multiple Linear Regression Model for the given data:")
output = f"Y = ({Beta[0]})"
for i in range(1, len(X)):
    output += f" + ({round(Beta[i],4)})X{i}"
print(output)

y = np.array([i[0] for i in Y])
SSE = GoodnessOfFit(y,Yfitted,alpha, Beta)

DOF = len(Y) - len(Beta)

ParameterTesting(XTX_inv, alpha, Beta, SSE, DOF)

---------------------------------------------------------------------
OUTPUT:

Enter number of X variables: 3
Enter Y values: 8 13 12 11 9 8 7 13 11 13
Enter X1 values: -1 -1 -1 -1 1 1 1 1 0 0
Enter X2 values: -1 1 1 1 -1 -1 -1 1 0 0
Enter Level of Significance: 0.05

The Multiple Linear Regression Model for the given data:
Y = (10.5) + (0.25)X1 + (2.25)X2

To Test Goodness of Fit using Determination of Coefficients (R2):
Coefficient of Determination (R2): 0.7525773195876289
The Multiple Regression Model is Not a Good Fit for the given data.

To Test Goodness of Fit using ANOVA:
Fcal > F-Table (10.6458 < 4.7374)
The Multiple Regression Model is a Good Fit for the given data.

Test for individual parameters:
Beta 0 is contributing to the model.
Beta 1 is Not contributing to the model.
Beta 2 is contributing to the model.
