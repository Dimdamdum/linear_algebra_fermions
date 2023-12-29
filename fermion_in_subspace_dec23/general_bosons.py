import scipy.special

def g(N,d,j):
    if N < 1 or j < 1 or j > d: # now N may exceed d!
        print("Error")
        return("Error")
    out = scipy.special.comb(d + N - 1, N, exact=True) - j * scipy.special.comb(N + d - j - 2, N - 1, exact=True) - j * (d-j)
    return(out)


dmax = 100
Nmax = 1000
d = 0

while (d < dmax):
    d += 1
    print(d)
    N = 1
    while (N < Nmax):
        N += 1
        j = 0
        while (j<d):
            j+=1
            #print(d,N,j)
            if(g(N,d,j) <= 0.1 ):
            #    print("!!! ",d)
                print(" d =",d, " N =",N," j =",j, " g value =",g(N,d,j))