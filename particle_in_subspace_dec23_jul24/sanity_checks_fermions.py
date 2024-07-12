import functions

dmax = 10 

# 2 fermions
d_with_found_j = []
d = 1 # ... means dmin = 2
while d < dmax:
    d += 1
    j = 0
    while j < d:
        j += 1
        #print(d, j)
        if(functions.g_F(2,d,j) <= 0 ): # here you set N = 2
            d_with_found_j.append([d,j])
            break
print(d_with_found_j)
print(len(d_with_found_j))

# d - 1 fermions
d_with_found_j = []
d = 1 # ... means dmin = 2
while d < dmax:
    d += 1
    j = 0
    while j < d:
        j += 1
        #print(d, j)
        if(functions.g_F(d - 1,d,j) <= 0 ): # here you set N = d - 1
            d_with_found_j.append([d,j])
            break
print(d_with_found_j)
print(len(d_with_found_j))

# d - 2 fermions
d_with_found_j = []
d = 2 # need dmin = 3, min 3 modes now!!
while d < dmax:
    d += 1
    j = 0
    while j < d:
        j += 1
        #print(d, j)
        if(functions.g_F(d - 2,d,j) <= 0 ): # here you set N = d - 2
            d_with_found_j.append([d,j])
            break
print(d_with_found_j)
print(len(d_with_found_j))

# 2 fermions bis (july 3, just to refamiliarize)
d = 1 # ... means dmin = 2
while d < dmax:
    d += 1
    j = int(d/2)
    if(functions.g_F(2,d,j) > 0 ): # here you set N = 2
        print("ouch sth is weird!")