import scipy.special

def g(N,d,j):
    if N < 1 or N > d or j < 1 or j > d:
        print("Error")
        return("Error")
    out = scipy.special.comb(d, N, exact=True) - j * scipy.special.comb(d - j, N - 1, exact=True) - j * (d-j)
    return(out)

dmin = 6
dmax = 1000

d = 5
while (d < dmax):
    d += 1
    print(d)
    N = 2
    while (N < d- 3):
        N += 1
        #print(d,N)
        j = 0
        while (j<d):
            j+=1
            #print(d,N,j)
            if(g(N,d,j) <= 0.1 ):
                print(" d =",d, " N =",N," j =",j, " g value =",g(N,d,j))