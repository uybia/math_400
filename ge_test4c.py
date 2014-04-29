from gaussian_elim import *
import sys

orig_stdout = sys.stdout
f = file('p4c.txt', 'w')
sys.stdout = f


# Problem 4
# Takes the inverse matrix and get its inverse again
# in order to, hopefully, get the original Hilbert matrix.
# Compare the difference.

for i in range(1, 26):
    H = hilbertMatrix(i)
    b = BMatrix(i)
    r1 = inverseNaive(H)
    r2 = inverseScaled(H)
    iden = identityMatrix(i)

    print("Naive Gaussian Elimination Inverse:")
    inv1 = inverseNaive(r1)
    show(inv1)
    
    print("\nGaussian Elimination with Scaled Partial Pivoting Inverse:")
    inv2 = inverseNaive(r2)
    show(inv2)

    print(" ")
    print("------------------------------------------------------------------")
    print(" ")
    
sys.stdout = orig_stdout
f.close()

