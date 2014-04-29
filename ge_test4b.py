from gaussian_elim import *
import sys

orig_stdout = sys.stdout
f = file('p4b.txt', 'w')
sys.stdout = f


# Problem 4
# Multiplies the Hilbert matrix with the inverse.
# Compares the result with identity matrix.

for i in range(1, 26):
    H = hilbertMatrix(i)
    b = BMatrix(i)
    r1 = inverseNaive(H)
    r2 = inverseScaled(H)
    iden = identityMatrix(i)
    #r3 = gaussSeidel(H,b,50)
    print("Naive Gaussian Elimination Inverse:")
    inv1 =matMult(H,r1)
    show(inv1)
    
    print("\n\nGaussian Elimination with Scaled Partial Pivoting Inverse:")
    inv2 = matMult(H,r2)
    show(inv2)

    
    print(" ")
    print("------------------------------------------------------------------")
    print(" ")
    
sys.stdout = orig_stdout
f.close()

