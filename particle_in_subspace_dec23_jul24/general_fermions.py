import functions

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
            if(functions.g_F(N,d,j) <= 0.1 ):
                print(" d =",d, " N =",N," j =",j, " g value =",functions.g_F(N,d,j))