from gaussian_elim import *
import sys

orig_stdout = sys.stdout
f = file('p4.txt', 'w')
sys.stdout = f


# Problem 4
# Finds the inverse of a Hilbert matrix
# for values 1 to 25

for i in range(1, 26):
    H = hilbertMatrix(i)
    b = BMatrix(i)
    r1 = inverseNaive(H)
    r2 = inverseScaled(H)

    print("Naive Gaussian Elimination Inverse:")
    show(r1)

    print("\nGaussian Elimination with Scaled Partial Pivoting Inverse:")
    show(r2)

    print("\nExact Inverse:")
    show(hilbertInverse(i))
    
    print(" ")
    print("------------------------------------------------------------------")
    print(" ")
    
sys.stdout = orig_stdout
f.close()

