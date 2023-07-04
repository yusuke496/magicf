	###########################################################
	## This program calculates the magic F for given I and J ##
	###########################################################
import numpy as np
import sys
import matplotlib.pyplot as plt

#Initial values
Ist = input("Input I :")
I = float(Ist)
Jst = input("Input J :")
J = float(Jst)

#Setting the parameters

Fmax = I+J
Fmin = abs(I-J)
F = Fmax + 1
l = int(0)

#calculate magic f
while F > Fmin +0.01:
  F = F - 1
  l=l+1

print("number of hfs", l)

a=np.array([np.array([float(0) for i1 in range(l)]),np.array([float(0) for i2 in range(l)])])

#print(a)

i1 = 0
F = Fmax + 1
while F > Fmin + 0.01 :
    F = F - 1
    K = F*(F+1) - I*(I+1) - J*(J+1)
    print("F=", F, "\t", "K=", "\t", K)
    a[0][i1] = F
    a[1][i1] = K
    i1 = i1 + 1

#print(a)

i1 = 0
i2 = 0
i3 = 0
for i1 in range(l-1) :
    for i2 in range(1,l-i1) :
        if abs(a[1][i1+i2]*(a[1][i1+i2]+1)-a[1][i1]*(a[1][i1]+1))\
        < 0.0000001 :
            print(a[1][i1], "\t", a[1][i1+i2])
            print("magic F", "\t", "(F1,F2)", "(", a[0][i1],a[0][i1+i2], ")")
            i3 = 1

if i3 == 0 :
    print("Ther is no magic F.")
else :
    print("Congratulations!")
