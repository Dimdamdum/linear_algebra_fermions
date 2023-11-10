import numpy as np
def h(x):
    eps = 1e-10
    if(-eps < x < eps or 1-eps < x < 1 + eps):
        return(0.)
    return(-x*np.log(x)-(1-x)*np.log(1-x))

def H(w):
    summ = 0.
    for j in range(len(w)):
        summ += h(w[j])
    return(summ)

def majorizes(array1, array2): # does not check equality of "traces"!
    if array1.size != array2.size:
        return False

    # Sort the arrays in non-increasing order
    sorted_array1 = np.sort(array1)
    sorted_array2 = np.sort(array2)

    #print(sorted_array1)
    #print(sorted_array2)

    cumulative_sum1 = cumulative_sum2 = 0

    for i in range(len(sorted_array1)-1):
        cumulative_sum1 += sorted_array1[i]
        cumulative_sum2 += sorted_array2[i]
        #print(cumulative_sum1)
        
        if cumulative_sum1 > cumulative_sum2:
            return False

    return True