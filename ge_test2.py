from gaussian_elim import *
import sys

orig_stdout = sys.stdout
f = file('p2.txt', 'w')
sys.stdout = f

# Problem 2
# Finds the solution vector, using three different method.

A = [[10.0,10.0,10.0,1e17],
    [1.0, 1e-3, 1e-3,1e-3],
    [1.0,1.0,1e-3,1e-3],
    [1.0,1.0,1.0,1e-3]]

b = [1e17,1.0,2.0,3.0]

r1 = ge_1(A,b)
r2 = ge_2(A,b)
r3 = ge_3(A,b)

print("Naive Gaussian Elimination:")
print("Row Reduced Matrix:")
show(r1[0])
print("Solution Vector")
print(r1[1])
print("Residual Vector")
print(residualVector(A,r1[1],b))

print("\nGaussian Elimination with Partial Pivoting:")
print("Row Reduced Matrix:")
show(r2[0])
print("Solution Vector")
print(r2[1])
print("Residual Vector")
print(residualVector(A,r2[1],b))

print("\nGaussian Elimination with Scaled Partial Pivoting:")
print("Row Reduced Matrix:")
show(r3[0])
print("Solution Vector")
print(r3[1])
print("Residual Vector")
print(residualVector(A,r3[1],b))

sys.stdout = orig_stdout
f.close()
