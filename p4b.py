import matplotlib.pyplot as plt

from math   import *
from numpy  import *

def fx_graph(name):
    x_pts = arange(-5,15,.001)
    y_pts = [fx(i) for i in x_pts]

    # Plot it against the exact equation
    #plt.plot(t_pts, x_pts, 'blue', label= r'$cos(2*pi*t)$')

    plt.plot(x_pts, y_pts, 'red',label= r'$1.0/ (1 + e**-2x)$')

    #y_pts = [cosx(i) for i in x_pts]
    #plt.plot(x_pts, y_pts, 'blue',label= r'$-cos(x)$')
    plt.title(name)
    
    plt.grid(True)
    plt.axis([.4, .6, -.1, 0.1], 'equal')

    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')

    #plt.legend(loc='lower left')

    plt.show()


# x is the initial guess.
def newtons_method(x):
    delta_x = (-fx(x)) / f_prime(x)
    return  x + delta_x

def fx(x):
    return (9.*(x**3))-(x**2)-1.

def f_prime(x):
    return (27.*(x**2))-(2.*x)

def main():
    x = 0.4
    for i in range(12):
        x = newtons_method(x)
        print "x (", i, ") = ", x, "\t f(x) =", fx(x)
    print "\n"
    y = sqrt(3*(x**2))
    print "y = ", y
main()
fx_graph(" ")
