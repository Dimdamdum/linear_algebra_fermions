import sys
import qiskit
import numpy as np
from qiskit.quantum_info import random_unitary
import scipy.linalg as LA
#print(sys.argv)
if(len(sys.argv)) != 5:
    print("Exiting. Arguments expected: dL dR NP m")
    sys.exit(1)
dL = int(sys.argv[1])
dR = int(sys.argv[2])
d = dL + dR
NP = int(sys.argv[3])
NH = d - NP
R=min(dL,dR,NP,NH)
print(R)
m = int(sys.argv[4])
U=np.zeros((d,d))
Udag=np.zeros((d,d))
P = np.copy(U)
for j in range(NP):
    P[j][j]=1
gamma=np.zeros((d,d))
gammaL=np.zeros((dL,dL))
gammaR=np.zeros((dR,dR))
#print(U)
#print(P)
for j in range(m):
    U = random_unitary(d)
    Udag = U.adjoint()
#    print(np.matmul(Udag,U).round(5))
    gamma = np.matmul(Udag,np.matmul(P,U))
#    print(LA.eigvals(gamma).round(5))
    gammaL = gamma[0:dL,0:dL]
    gammaR = gamma[dL:d,dL:d]
#    print(gamma.round(3), "\n")
#    print(gammaL.round(3))
#    print(gammaR.round(3))
    lambdaL = LA.eigvals(gammaL).round(5)
    lambdaR = LA.eigvals(gammaR).round(5)
    print("Evals of gammaL: ", lambdaL)
    print("Evals of gammaR: ", lambdaR)
    rel_lambdaL=[]
    rel_lambdaR=[]
    eps=0.0000001
    for j in range(dL):
        if lambdaL[j]>eps and lambdaL[j]<1-eps:
            rel_lambdaL.append(np.real(lambdaL[j]))
    for j in range(dR):
        if lambdaR[j]>eps and lambdaR[j]<1-eps:
            rel_lambdaR.append(np.real(lambdaR[j]))
    rel_lambdaL = np.sort(rel_lambdaL)
    rel_lambdaR = np.sort(rel_lambdaR)[::-1]
    print("R =", R, ",", len(rel_lambdaL), "relevant evals in gammaL,",len(rel_lambdaR), "relevant evals in gammaR, namely:")
    print(rel_lambdaL)
    print(rel_lambdaR)
    print("The pairwise sums (should be all 1):")
    print(rel_lambdaL + rel_lambdaR, "\n")