import subprocess
import sys

if(len(sys.argv)) != 5:
    print("Exiting. Arguments expected: # left modes dL, # right modes dR, # v vectors per w vector, # w vectors = # times kaustavs_conjecture.py should be executed. Need dL >= dR")
    sys.exit(1)
dL = int(sys.argv[1])
dR = int(sys.argv[2])
m = int(sys.argv[3])

# command to be executed
base_command = "python kaustavs_conjecture.py "
command = f"{base_command} {dL} {dR} {m}"


# Number of times to execute the command = number of ws
num_iterations = int(sys.argv[4])

for _ in range(num_iterations):
    # Execute the command using subprocess
    subprocess.call(command, shell=True)