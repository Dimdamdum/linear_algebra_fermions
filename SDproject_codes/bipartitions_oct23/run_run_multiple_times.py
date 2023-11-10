import subprocess
import sys

# per each couple dL dR execute only once run_kaustavs_conjecture_multiple_times.py
num_vs = 5000000 #can make this dL,dR dependent
num_ws = 1
dLmin = 3
dLmax = 3

# command to be executed
base_command = "python run_kaustavs_conjecture_multiple_times.py"
dL = dLmin -1
while dL < dLmax:
    dL += 1
    dR = 0
    while dR < dL:
        dR +=1 
        print("\n _______________________ \n _______________________ \n \n Now working with dimensions",dL, dR,"\n")
        command = f"{base_command} {dL} {dR} {num_vs} {num_ws}"
        subprocess.call(command, shell=True)