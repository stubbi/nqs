#expected file name is 'in.qc'
import random
import sys
import math

numQubits = int(sys.argv[1])
numCycles = int(sys.argv[2])
qasmFile = sys.argv[3]

circuit = """
version 1.0
qubits 8

CZ q[1], q[3]
CZ q[2], q[4]
CZ q[3], q[5]
CZ q[4], q[6]
CZ q[5], q[7]
"""

f = open(qasmFile,'w')
print >>f, circuit
f.close()