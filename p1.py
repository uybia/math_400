import matplotlib.pyplot as plt
from numpy import arange
from math import *
x_vals = []
t_vals = []

"""
@param fn   function dx/dt (i.e. fn(t,x))
@param t    initial value of t
@param x    initial value of x
@param h    step size
"""
def euler(fn, t, x, h):
    clear_list()
    x_vals.append(x)
    t_vals.append(t)
    slope = fn(t,x)
    table(t,x,h,slope)
    while(round(t,2) < 2):  # boundary condition
        t = t + h           # t_k+1 = t_k + h
        x = x + (h * slope) # x_k+1 = x_k + h * f(t_k, x_k)
        slope = fn(t,x)     # slope of t_k+1, x_k+1
        x_vals.append(x)
        t_vals.append(t)
        table(t,x,h,slope)

"""
@param fn   function dx/dt (i.e. fn(t,x))
@param t    initial value of t
@param x    initial value of x
@param h    step size
"""
def euler_modified(fn, t, x, h):
    clear_list()
    x_vals.append(x)
    t_vals.append(t)
    slope = fn(t,x)
    table(t,x,h,slope)
    while(round(t,2) < 2):  # boundary condition
        t = t + h           # t_k+1
        x_star = x + (h * slope)    # x*_k+1 = x_k + (h * m_k)
        m_star = fn(t, x_star)      # m*_k+1 = f(t_k+1, x*_k+1)
        x = x + (h * ((slope + m_star)/2.0)) # x_k+1
        x_vals.append(x)
        t_vals.append(t)
        slope = fn(t,x)     # slope of t_k+1, x_k+1
        table(t,x,h,slope)

def rk4(fn, t, x, h):
    clear_list()
    x_vals.append(x)
    t_vals.append(t)
    slope = fn(t,x)
    table(t,x,h,slope)
    while(round(t,2) < 2):  # boundary condition
        k1 = h * fn(t, x)
        k2 = h * fn((t + 0.5*h), (x + 0.5*k1))
        k3 = h * fn((t + 0.5*h), (x + 0.5*k2))
        k4 = h * fn((t + h), (x + k3))
        t = t + h #t_k+1
        x = x + (1./6)*(k1 + 2*k2 + 2*k3 + k4)
        x_vals.append(x)
        t_vals.append(t)
        slope = fn(t,x)     # slope of t_k+1, x_k+1
        table(t,x,h,slope)
        
"""
Clears list x_vals and t_vals
"""
def clear_list():
    x_vals[:] = []
    t_vals[:] = []

    
    
#############################################


"""
@param name Title of the graph
"""
def solution_graph(name):
    t_pts = arange(0,2,.001)
    x_pts = [fn_x(i) for i in t_pts]

    #plt.plot(t_pts, x_pts, 'blue', label= r'$x(t)$')
    plt.plot(t_vals, x_vals, 'red')
    
    plt.title(name)
    
    plt.grid(True)
    plt.axis([0, 2, 0.3, 1], 'equal')

    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')

    plt.legend(loc='upper right')

    plt.show()
    
def table(t, x, h, m):
    print("|  %.3f    |  %.7f    |  %.7f   |" %(t, x, m))
 

def fn_x(t):
    return ((5/4.0)*(e**(-2*t))) + ( (1.0/4)*((2*t)-1))

def function(t,x):
    return t - 2*x


def main():
    print("EULER'S METHOD: h = 0.2")
    print("----------------------------------------")
    print("|     t     |     x     |     slope     |")
    print("----------------------------------------")
    euler (function, 0, 1, 0.2)
    print("----------------------------------------") 
    solution_graph("EULER'S METHOD: h = 0.2")

    print("\n\nEULER MODIFIED METHOD:  h = 0.2")
    print("----------------------------------------")
    print("|     t     |     x     |     slope     |")
    print("----------------------------------------")
    euler_modified (function, 0, 1, 0.2)
    print("----------------------------------------")
    solution_graph("EULER MODIFIED METHOD:  h = 0.2")

    print("\n\nRK-4 METHOD: h = 0.2")
    print("----------------------------------------")
    print("|     t     |     x     |     slope     |")
    print("----------------------------------------")
    rk4(function, 0, 1, 0.2)
    print("----------------------------------------")
    solution_graph("RK-4 METHOD: h = 0.2")

    print("\n\nEULER'S METHOD: h = 0.1")
    print("----------------------------------------")
    print("|     t     |     x     |     slope     |")
    print("----------------------------------------")
    euler (function, 0, 1, 0.1)
    print("----------------------------------------")
    solution_graph("EULER'S METHOD: h = 0.1")

    print("\n\nEULER MODIFIED METHOD: h = 0.1")
    print("----------------------------------------")
    print("|     t     |     x     |     slope     |")
    print("----------------------------------------")
    euler_modified (function, 0, 1, 0.1)
    print("----------------------------------------")
    solution_graph("EULER MODIFIED METHOD: h = 0.1")

    print("\n\nRK-4 METHOD: h = 0.1")
    print("----------------------------------------")
    print("|     t     |     x     |     slope     |")
    print("----------------------------------------")
    rk4(function, 0, 1, 0.1)
    print("----------------------------------------")
    solution_graph("RK-4 METHOD: h = 0.1")

    print("EULER'S METHOD: h = 0.05")
    print("----------------------------------------")
    print("|     t     |     x     |     slope     |")
    print("----------------------------------------")
    euler (function, 0, 1, 0.05)
    print("----------------------------------------")
    solution_graph("EULER'S METHOD: h = 0.05")

    print("\n\nEULER MODIFIED METHOD: h = 0.05")
    print("----------------------------------------")
    print("|     t     |     x     |     slope     |")
    print("----------------------------------------")
    euler_modified (function, 0, 1, 0.05)
    print("----------------------------------------")
    solution_graph("EULER MODIFIED METHOD: h = 0.05")

    print("\n\nRK-4 METHOD: h = 0.05")
    print("----------------------------------------")
    print("|     t     |     x     |     slope     |")
    print("----------------------------------------")
    rk4(function, 0, 1, 0.05)
    print("----------------------------------------")
    solution_graph("RK-4 METHOD: h = 0.05")

main()
