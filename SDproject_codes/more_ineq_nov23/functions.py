import numpy as np

# takes as input two 3-dimensional np arrays and a 6-dimensional np array and checks whether Thompon's inequalities are fulfilled. 
def check_ineq(a,b,c):
    # order arrays: done in main 
    # a = np.sort(a_unord)[::-1]
    # b = np.sort(b_unord)[::-1]
    # c = np.sort(c_unord)[::-1]
    # print(a)

    # first round of checks
    for i in range(3):
        for j in range(3):
            if c[i+j] + c[5] >  a[i] + b[j]:
                return(False)

    #second round of checks
    for i1 in range(2):
        for i2 in range(i1 + 1,3):
            for j1 in range(2):
                for j2 in range(j1+1,3):
                    if(c[i1 + j1] + c[i2 + j2 - 1] + c[4] + c[5] > a[i1] + a[i2] + b[j1] + b[j2]):
                        return(False)
    return(True)