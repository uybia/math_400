import matplotlib.pyplot as plt

from math   import *
from numpy  import *

def solution_graph(name):
    x_pts = arange(-5,15,.001)
    y_pts = [fn_x(i) for i in x_pts]

    # Plot it against the exact equation
    #plt.plot(t_pts, x_pts, 'blue', label= r'$cos(2*pi*t)$')

    plt.plot(x_pts, y_pts, 'red',label= r'$1.0/ (1 + e**-2x)$')

    y_pts = [cosx(i) for i in x_pts]
    plt.plot(x_pts, y_pts, 'blue',label= r'$-cos(x)$')
    plt.title(name)
    
    plt.grid(True)
    plt.axis([-2, 11, -1.3, 1.3], 'equal')

    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')

    plt.legend(loc='lower left')

    plt.show()


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
    plt.axis([0, 10, -.3, 2.1], 'equal')

    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')

    #plt.legend(loc='lower left')

    plt.show()

def fx_graph2(name):
    x_pts = arange(-5,15,.001)
    y_pts = [fx(i) for i in x_pts]

    # Plot it against the exact equation
    #plt.plot(t_pts, x_pts, 'blue', label= r'$cos(2*pi*t)$')

    plt.plot(x_pts, y_pts, 'red',label= r'$1.0/ (1 + e**-2x)$')

    #y_pts = [cosx(i) for i in x_pts]
    #plt.plot(x_pts, y_pts, 'blue',label= r'$-cos(x)$')
    plt.title(name)
    
    plt.grid(True)
    plt.axis([3, 3.3, -.05, .05], 'equal')

    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')

    #plt.legend(loc='lower left')

    plt.show()


def fn_x(x):
    return (1.0/ (1 + (e **(-2*x))))

def cosx(x):
    return (-cos(x))

def fx(x):
    return (1.0/ (1 + (e **(-2*x)))) + cos(x)

def f_prime(x):
    num = 2.0*(e**(-2.*x))
    denom = (1. + (e**(-2.*x)))**2
    return (num/denom) - sin(x)


# x is the initial guess.
def newtons_method(x):
    delta_x = (-fx(x)) / f_prime(x)
    return  x + delta_x



def main():
    x = 3.05
    for i in range(6):
        x = newtons_method(x)
        print "x (", i+1, ") = ", x, "\t f(x) =", fx(x)
    print "\n\n"
    x = 3.23
    for i in range(6):
        x = newtons_method(x)
        print "x (", i+1, ") = ", x, "\t f(x) =", fx(x)
        

main()
solution_graph("(1.0/ (1 + (e **(-2*x)))) vs. -cos(x)")
fx_graph("(1.0/ (1 + (e **(-2*x)))) + cos(x)")
fx_graph2("(1.0/ (1 + (e **(-2*x)))) + cos(x)")
