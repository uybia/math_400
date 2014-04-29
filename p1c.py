from math import *

def zeroMatrix(m,n):
    "Create zero matrix"
    new_mat = []
    for row in range(m):
        zero_row = []
        for col in range(n):
            zero_row.append(0)
        new_mat.append(zero_row)
    return(new_mat)

def zeroV(m):
    z = [0]*m
    return(z)

def showMatrix(mat):
    "Print out matrix"
    for row in mat:
        print(row)

def trapezoid_rule(no_subinterval, a, b):
    sum = 0
    x_vals = zeroV(no_subinterval+1)
    for i in range(0, (no_subinterval+1)):
        x_vals[i] = a + (i * ((b-a)/no_subinterval))
    for i in range(1, no_subinterval):
        sum += sinc(x_vals[i])
    return ((b-a)/(2*no_subinterval))*(sinc(a) + (2 * sum) + sinc(b))

def romberg(h,a,b):
    s = zeroMatrix(h, h)
    tmp = h
    for i in range(h):
        s[i][0] = trapezoid_rule((tmp),a,b)
        tmp *= 2
    for i in range(1, h):
        for j in range(i, h):
            s[j][i] = s[j][i-1] + ((s[j][i-1] - s[j-1][i-1]) / ((2**(2*i))-1))
    showMatrix(s)


def sin_pi(x):
    return sin(pi*x)

def e_2(x):
    return (e**((-x**2)/2))

def sinc(x):
    if (x==0):
        return 1
    else:
        return ((sin(2*pi*x))/(2*pi*x))


print("Trapezoidal Method")
print("------------------------------")
print("|  # points |      area      |")
print("------------------------------")
for j in range(2819,2850):
    print("|   %4d    |   %.7f    |" %(j+1,(trapezoid_rule(j, -1., 1.))))
print("------------------------------\n")

print("Romberg Integration")
romberg(4,-1.0,1.0)

