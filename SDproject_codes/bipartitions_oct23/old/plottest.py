import matplotlib.pyplot as plt
import numpy as np
#import ..fun

import matplotlib.pyplot as plt
import numpy as np

# Create Data
M = 100
x = np.linspace(0., 1., M)
y = [np.sin(x[j]) for j in range(M)]
print(y[0],y[1])

# create the plot
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot prot')
plt.grid(True)
plt.gca().set_facecolor('white') 

# Display the Plot
#plt.show()

#save the plot
#plt.savefig('plottest.png')

a = 0
a += 2


file = open("counterexamples_to_conj.txt","a")
a = 3
output = f"{a} ttttettttttteetttest"
file.write(output)
file.close()