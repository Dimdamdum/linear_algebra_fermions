import qiskit
import numpy as np
from qiskit.quantum_info import random_unitary
import scipy.linalg as LA
from numpy import random
import functions

#This code checks that Thompon's inequalities (https://doi.org/10.1016/0375-9601(85)90622-X) do not imply the majorization inequalities conjectured by kaustav.
# We work out the case of 6x6 matrices with block structure 3 + 3. Counterexamples turn out to be rare but not very rare.
# The result is that the inequalities conjectured by Kaustav, which I think hold, are independent of Thompson's.

##########
# PART 1 #
##########
#we sample 3-tuples a,b,c. For those which verify all 36 of thompson's inequalities, we check wheter majorization inequalities as conjecture by kaustav can be violated. (Spoiler:yes, as expected)

count = 0
truecount = 0
truecountmax = 10000
countcounterexupper = 0
countcounterexlower = 0

while(truecount < truecountmax):
    count += 1
    a = np.random.rand(3)
    b = np.random.rand(3)
    c = np.random.rand(6)
    a = np.sort(a)[::-1]
    b = np.sort(b)[::-1]
    c = np.sort(c)[::-1]
    #print(a)
    trace = np.sum(a) + np.sum(b)
    a = a/trace
    b = b/trace
    c = c/np.sum(c)
    #print(np.sum(a)+np.sum(b))
    #print(a)
    #print(np.sort(-a)[::-1])

     # also checking on -a,-b,-c!
    aneg = np.sort(-a)[::-1]
    bneg = np.sort(-b)[::-1]
    cneg = np.sort(-c)[::-1]
    #print(cneg)
    if(functions.check_ineq(a,b,c) and functions.check_ineq(aneg,bneg,cneg)):
        #now check if nontrivial majorization inequalities are fulfilled
        truecount += 1
        if(c[1] + c[4] > a[0] + b[0]):
            #print("Upper bound on c[1] + c[4] violated")
            countcounterexupper +=1
        if(c[1] + c[4] < a[2] + b[2]):
            #print("Lower bound on c[1] + c[4] violated")
            countcounterexlower +=1


print("Number of sampled 3-tuples (a,b,c) which satisfy the 36 of Thompson inequalities: ", truecount)
print('Ratio of sampled 3-tuples (a,b,c) which satisfy the 36 of Thompson inequalities: ',float(truecount)/float(count)) #looks like about 30% of the sampled 3-tuples (a,b,c) satisfy all 18 + 18 Thompson's ineqaulities 
print('Number of 3-tuples satisfying T inequalities but do not satisfy the target upper bound: ',countcounterexupper)
print('Number of 3-tuples satisfying T inequalities but do not satisfy the target lower bound: ',countcounterexlower)


##########
# PART 2 #
##########
# Here we see a specific counterexample, i.e. a 3-uple a,b,c which verifies Thompson's inequalities but not the target upper bound

print("\n Now some checks on a specific counterexample...")
a = np.array( [0.20890941, 0.20159637, 0.09837491] )
b = np.array( [0.17090591 , 0.16607657, 0.15413682] )
c = np.array(  [0.31338467, 0.30821003, 0.16374221, 0.11874102, 0.08332326, 0.01259882] )

print(sum(a) + sum(b) - sum(c))

print(functions.check_ineq(a,b,c)) #i also double checked manually,on another code

print(c[1] + c[4])
print(a[0] + b[0])

##########
# PART 3 #
##########
#further last check: generate a,b,c from actual matrices, check that T's inequalities are fulfilled, and that majorization inequalities (Kaustav's) also are. No surprises

print('\n Now sampling with actual spectra...')

#copying stuff from old code
d = 6
dL = dR = 3
gamma = np.zeros((d,d))
gammaL = np.zeros((dL,dL))
gammaR = np.zeros((dR,dR))
lambL = np.zeros((dL))
lambR = np.zeros((dR))
diag_c = np.zeros((d,d))

number_spectra = 20000

for j in range(number_spectra):
    # also sample random spectra of whole unitary
    c = np.random.rand(6)
    for k in range(d):
        diag_c[k][k] = c[k]
    U = random_unitary(d)
    Udag = U.adjoint()
    gamma = np.matmul(Udag,np.matmul(diag_c,U))
    gammaL = gamma[0:dL,0:dL]
    gammaR = gamma[dL:d,dL:d]
    a = np.real(LA.eigvals(gammaL))
    b = np.real(LA.eigvals(gammaR))
    a = np.sort(a)[::-1]
    b = np.sort(b)[::-1]
    c = np.sort(c)[::-1]
    sth_wrong = False
    if(functions.check_ineq(a,b,c) == False):
        print("Thompson is wrong or you cant code!")
        sth_wrong = True
    if(c[1] + c[4] > a[0] + b[0] or c[1] + c[4] < a[2] + b[2]):
        print("Kaustav's conjectured majorization is wrong or you cant code!")
        sth_wrong = True
if(sth_wrong == False):
    print("Nothing went wrong, no surprises with the", number_spectra,"sampled actual spectra.")
