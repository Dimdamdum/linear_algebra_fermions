import functions
from plotting_several_lists import lists_to_plots

# fix d > 0, 2 <= N <= Nmax; let j = 1, ..., d vary
print("First analysis: d, N fixed, j varies \n")
dmin = 1
dmax = 6
Nmax = 10
d = dmin - 1
while(d < dmax):
    d += 1
    N = 1
    while(N < Nmax):
        N += 1
        print("\n d = ", d, "N = ", N)
        g_values = []
        for j in range(1, d + 1):
            g_values.append(functions.g_B(N, d, j))
        print(g_values)

# fix d > 0, j with 1 <= j <= d; let N = 2, ... , Nmax vary

print("\n Second analysis: d, j fixed, N varies \n")
d = dmin - 1
while(d < dmax):
    d += 1
    j = 0
    while(j < d):
        j += 1
        print("\n d = ", d, "j = ", j)
        g_values = []
        for N in range(2, Nmax + 1):
            g_values.append(functions.g_B(N, d, j))
        print(g_values)

#the second analysis seems more fruitful, so we focus on fixing d, j and varying N

#let us pack the production of the list g_values into a function
def g_values_B(Nmax, d, j):
    g_values = []
    for N in range(2, Nmax + 1):
        g_values.append(functions.g_B(N, d, j))
    return(g_values)

#create a list of lists "g_values" corresponding to desired values of d, j and with a certain Nmax:
list_of_lists = []
d = 9
Nmax = 2
for j in range(1,d + 1):
    list_of_lists.append(g_values_B(Nmax, d, j))
d = 10
for j in range(1,d + 1):
    list_of_lists.append(g_values_B(Nmax, d, j))
#plot every list "g_values" contained in list_of_lists as a function i -> g_values[i]. This is same as N -> g(N, d, j) (up to a shift i <-> N)
lists_to_plots(list_of_lists) 

#convexity and monotonicity really seem to be there!!
    
