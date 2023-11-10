import sys
import qiskit
import numpy as np
from qiskit.quantum_info import random_unitary
import scipy.linalg as LA
from numpy import random
import fun

moreinfo = False

# this program works with a SINGLE random w vector. exectue this program several times to sample many w vectors

if(len(sys.argv)) != 4:
    print("Exiting. Arguments expected: # left modes dL, # right modes dR, # v vectors. Need dL >= dR")
    sys.exit(1)
dL = int(sys.argv[1])
dR = int(sys.argv[2])
m = int(sys.argv[3])
d = dL + dR
w = np.zeros((d))
for j in range(d):
    w[j] = random.rand()
w = np.sort(w)

# write in counterexamples_to_conj that you are executing this program
with open('number_w_and_counterex.txt', 'r') as file:
    count = int(file.read())
with open('number_w_and_counterex.txt', 'w') as file:
    file.write(f"{count + 1}")
#print("it went on")

#conjectured variables:
vbest_conj = np.copy(w)
for j in range(dR):
    vbest_conj[j] = vbest_conj[-j-1] = (w[j] + w[-j-1])/2
Imax_conj = fun.H(vbest_conj)
#print(fun.H(vbest_num)-fun.H(vbest_conj))
#print(fun.majorizes(w,vbest_conj))
#print(sum(w))
#print(sum(vbest_conj))
diag_w = np.zeros((d,d))
for j in range(d):
    diag_w[j][j] = w[j]

# relevant variables for sampling:
#conj_maj = True
eps = 100.
Imax_num = 0.
vbest_num = np.copy(w) 
gamma = np.zeros((d,d))
gammaL = np.zeros((dL,dL))
gammaR = np.zeros((dR,dR))
lambL = np.zeros((dL))
lambR = np.zeros((dR))
v = np.zeros((d))

# sampling:
if(moreinfo):
    print("The upcoming 'epsilons' are values of Imax_conj - Imax_num")
for j in range(m):
    U = random_unitary(d)
    Udag = U.adjoint()
    gamma = np.matmul(Udag,np.matmul(diag_w,U))
#    print(w)
#    print(LA.eigvals(gamma).round(5))
    gammaL = gamma[0:dL,0:dL]
    gammaR = gamma[dL:d,dL:d]
#    print(gamma.round(3), "\n")
#    print(gammaL.round(3))
#    print(gammaR.round(3))
    lambL = LA.eigvals(gammaL)
    lambR = LA.eigvals(gammaR)
    for k in range(dL):
        v[k] = np.real(lambL[k])
    for k in range(dR):
        v[-k-1] = np.real(lambR[k])
#    print(lambL.round(10))
#    print(lambR.round(3))
#    print(v.round(3))
#    print(sum(v)-sum(w))
    if(fun.majorizes(v,vbest_conj) == False):
        output = "Found a counterexample to conjecture via maj relation! \n"
        print(output)
        with open('number_w_and_counterex.txt', 'a') as file:
            file.write(output)
            file.write(f"w is {w} and the unitary is \n {U} \n \n")

    # within sampling: check how accurate the sample is
    if(Imax_num < fun.H(v)):
        Imax_num = fun.H(v)
        eps = Imax_conj - Imax_num
        vbest_num = np.copy(v)
        if(moreinfo):
            print("eps = ",eps)
        if(eps < 0):
            output = "Found a counterexample to conjecture while computing H values! \n"
            print(output)
            with open('number_w_and_counterex.txt', 'a') as file:
                file.write(output)
                file.write(f"w is {w} and the unitary is \n {U} \n \n")
print("The sorted numerical and conjectured best v vector are, respectively: \n", np.sort(vbest_num).round(3),"\n", np.sort(vbest_conj).round(3),"\n and Imax_conj - Imax_num = eps =", eps, "\n")

