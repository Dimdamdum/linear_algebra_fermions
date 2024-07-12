import functions

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
            if(functions.g_B(N,d,j) <= 0.1 ):
            #    print("!!! ",d)
                print(" d =",d, " N =",N," j =",j, " g value =",functions.g_B(N,d,j))