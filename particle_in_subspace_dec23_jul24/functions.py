import scipy.special

def g_F(N,d,j):
    if N < 1 or N > d or j < 1 or j > d:
        print("Error")
        return("Error")
    out = scipy.special.comb(d, N, exact=True) - j * scipy.special.comb(d - j, N - 1, exact=True) - j * (d-j)
    return(out)

def g_B(N,d,j):
    if N < 1 or j < 1 or j > d: # now N may exceed d!
        print("Error")
        return("Error")
    out = scipy.special.comb(d + N - 1, N, exact=True) - j * scipy.special.comb(N + d - j - 2, N - 1, exact=True) - j * (d-j)
    return(out)