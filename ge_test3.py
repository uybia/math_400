from gaussian_elim import *
import sys

orig_stdout = sys.stdout
f = file('p3.txt', 'w')
sys.stdout = f


# Problem 3
# Finds the solution, c, of the Hilbert matrices using
# naive Gaussian, Gaussian elimination with scaled
# partial pivoting, and Gauss-Seidel iteration.
# Gauss-Seidel is set to have a max iteration of 50.

for i in range(1, 26):
    H = hilbertMatrix(i)
    b = BMatrix(i)
    r1 = ge_1(H,b)
    r2 = ge_3(H,b)
    #r3 = gaussSeidel(H,b,50)
    print("Naive Gaussian Elimination:")
    #print("Row Reduced Matrix:")
    #show(r1[0])
    print("Solution Vector")
    print(r1[1])
    print("Residual Vector")
    print(residualVector(H,r1[1],b))

    print("\nGaussian Elimination with Scaled Partial Pivoting:")
    #print("Row Reduced Matrix:")
    #show(r2[0])
    print("Solution Vector")
    print(r2[1])
    print("Residual Vector")
    print(residualVector(H,r2[1],b))

    print("\nGauss-Seidel Iteration:")
    print("Solution Vector with 50 iteration")
    r3 = gaussSeidel(H,b,50)
    print(r3)
    print("Residual Vector")
    print(residualVector(H,r3,b))
    print(" ")
    print("------------------------------------------------------------------")
    print(" ")
    
sys.stdout = orig_stdout
f.close()

