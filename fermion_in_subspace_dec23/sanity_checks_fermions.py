import scipy.special
#from itertools import product

def g(N,d,j):
    if N < 1 or N > d or j < 1 or j > d:
        print("Error")
        return("Error")
    out = scipy.special.comb(d, N, exact=True) - j * scipy.special.comb(d - j, N - 1, exact=True) - j * (d-j)
    return(out)

dmax = 10

# 2 fermions
d_with_found_j = []
d = 1
while d < dmax:
    d += 1
    j = 0
    while j < d:
        j += 1
        #print(d, j)
        if(g(2,d,j) <= 0 ): # here you set N = 2
            d_with_found_j.append([d,j])
            break
print(d_with_found_j)
print(len(d_with_found_j))

# d - 1 fermions
d_with_found_j = []
d = 1
while d < dmax:
    d += 1
    j = 0
    while j < d:
        j += 1
        #print(d, j)
        if(g(d - 1,d,j) <= 0 ): # here you set N = d - 1
            d_with_found_j.append([d,j])
            break
print(d_with_found_j)
print(len(d_with_found_j))

# d - 2 fermions
d_with_found_j = []
d = 2 # need min. 3 modes now!!
while d < dmax:
    d += 1
    j = 0
    while j < d:
        j += 1
        #print(d, j)
        if(g(d - 2,d,j) <= 0 ): # here you set N = d - 2
            d_with_found_j.append([d,j])
            break
print(d_with_found_j)
print(len(d_with_found_j))