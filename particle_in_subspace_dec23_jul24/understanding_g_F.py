import functions
from plotting_several_lists import lists_to_plots

# fix d > 6, N with 2 < N < d - 2; let j = 1, ..., d vary
print("First analysis: d, N fixed, j varies \n")
dmin = 7
dmax = 10
d = dmin - 1
while(d < dmax):
    d += 1
    N = 2
    while(N < d - 3):
        N += 1
        print("\n d = ", d, "N = ", N)
        g_values = []
        for j in range(1, (d + 1 - N ) + 1): # upgraded july 4th: can set j <= d + 1 - N
            g_values.append(functions.g_F(N, d, j))
        print(g_values)

# fix d > 6, j with 1 <= j <= d; let N = 3, ... , d - 3 vary
print("\n Second analysis: d, j fixed, N varies \n")
d = dmin - 1
while(d < dmax):
    d += 1
    j = 0
    while(j < d):
        j += 1
        print("\n d = ", d, "j = ", j)
        g_values = []
        for N in range(3, d - 2):
            g_values.append(functions.g_F(N, d, j))
        print(g_values)
    
#the second analysis seems more fruitful, so we focus on fixing d, j and varying N

#let us pack the production of the list g_values into a function
def g_values_F(d, j):
    g_values = []
    #for N in range(3, d - 2):
    for N in range(3, min(d - 3, d - j + 1) + 1): # upgraded  on July 4th:
    # point is, for N > d - j + 1 \Delta_j contains states with N - 1 > d - j
    # fermions in d - j modes
        g_values.append(functions.g_F(N, d, j))
    return(g_values)

#create a list of lists "g_values" corresponding to desired values of d, j:
list_of_lists = []
d = 12
for j in range(1,d + 1):
    list_of_lists.append(g_values_F(d, j))
d = 30
for j in range(3, 6):
    list_of_lists.append(g_values_F(d, j))
for j in range(23, 26):
    list_of_lists.append(g_values_F(d, j))
#plot every list "g_values" contained in list_of_lists as a function i -> g_values[i]. This is same as N -> g(N, d, j) (up to a shift i <-> N)
lists_to_plots(list_of_lists) 

#BAD NEWS: N -> g(N, d, j) is i.g. not concave!
#GOOD NEWS: shape of N -> g(N, d, j) is still quite simple! like bell-shaped, with MINIMA FOR N = 3 OR N = d - 3