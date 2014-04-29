import matplotlib.pyplot as plt
from numpy import arange
from math import *
x_vals = []
t_vals = []
y_vals = []
x1_vals = []
x2_vals = []
x3_vals = []
t1_vals = []
t2_vals = []
t3_vals = []

def copyV(L):
    "return a copy of L"
    C=[k for k in L]
    return(C)

"""
Clears list x_vals, t_vals, and y_vals
"""
def clear_list():
    x_vals[:] = []
    t_vals[:] = []


"""
@param fn   function dx/dt (i.e. fn(t,x))
@param t    initial value of t
@param x    initial value of x
@param h    step size
"""
def euler(fn, t, x, y, h):
    clear_list()
    x_vals.append(x)
    t_vals.append(t)
    y_vals.append(y)
    slope = fn(t,x,y)
    table(t,x,y,slope)
    while(round(t,2) < 1.2):  # boundary condition
        x = x + (h * y) # x_k+1 = x_k + h * f(t_k, x_k)
        y = y + (h * fn(t,x,y))
        t = t + h
        slope = fn(t,x,y)     # slope of t_k+1, x_k+1
        x_vals.append(x)
        t_vals.append(t)
        y_vals.append(y)
        table(t,x,h,slope)



"""
@param fn   function dx/dt (i.e. fn(t,x))
@param t    initial value of t
@param x    initial value of x
@param h    step size
"""
def euler_modified(fn, t, x, y, h):
    clear_list()
    x_vals.append(x)
    t_vals.append(t)
    y_vals.append(y)
    slope = fn(t,x,y)
    table(t,x,y,slope)
    while(round(t,2) < 1.2):  # boundary condition
        x_mk = y
        y_mk = fn(t,x,y)
        
        x_star = x + (h * x_mk)
        y_star = y + (h * y_mk)

        t = t + h

        x_m_star = y_star
        y_m_star = fn(t,x_star,y_star)

        x = x + (h * ( (x_mk + x_m_star)/2.0))
        y = y + (h * ( (y_mk + y_m_star)/2.0))
        
        x_vals.append(x)
        t_vals.append(t)
        y_vals.append(y)
        slope = fn(t,x,y)     # slope of t_k+1, x_k+1
        table(t,x,h,slope)


def rk4(fn, t, x, y, h):
    clear_list()
    x_vals.append(x)
    t_vals.append(t)
    y_vals.append(y)
    slope = fn(t,x,y)
    table(t,x,y,slope)
    while(round(t,2) < 1.2):  # boundary condition
        xk1 = h * y
        yk1 = h * fn(t,x,y)
        
        xk2 = h * (y + (0.5)*(yk1))
        yk2 = h * fn((t + .5*h), (x + (.5*xk1)), (y + (0.5)*(yk1)))
        
        xk3 = h * (y + (0.5)*(yk2))
        yk3 = h * fn((t + .5*h), (x + (.5*xk2)), (y + (0.5)*(yk2)))
        
        xk4 = h * (y + yk3)
        yk4 = h * fn((t + h), (x + xk3), (y + yk3))

        t = t + h 
        x = x + (1./6)*(xk1 + 2*xk2 + 2*xk3 + xk4)
        y = y + (1./6)*(yk1 + 2*yk2 + 2*yk3 + yk4)
        
        x_vals.append(x)
        t_vals.append(t)
        y_vals.append(y)
        slope = fn(t,x,y)     # slope of t_k+1, x_k+1
        table(t,x,h,slope)





"""
@param name Title of the graph
"""
def solution_graph(name):
    t_pts = arange(0,2,.001)
    x_pts = [fn_x(i) for i in t_pts]

    # Plot it against the exact equation
    plt.plot(t_pts, x_pts, 'blue', label= r'$cos(2*pi*t)$')
    
    plt.plot(t_vals, x_vals, 'red', label=r'$Euler Method$')
    
    plt.title(name)
    
    plt.grid(True)
    plt.axis([0, 1.2, -1.5, 1.5], 'equal')

    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')

    plt.legend(loc='lower right')

    plt.show()

def error_graph(name,x1_vals,x2_vals,x3_vals,t1_vals,t2_vals,t3_vals):

    t_pts = arange(0,2,.001)
    x1_pts = [(fn_x(t1_vals[i]) - x1_vals[i]) for i in range(len(t1_vals))]
    x2_pts = [(fn_x(t2_vals[i]) - x2_vals[i]) for i in range(len(t2_vals))]
    x3_pts = [(fn_x(t3_vals[i]) - x3_vals[i]) for i in range(len(t3_vals))]

    # Plot it against the exact equation
    #plt.plot(t_pts, x_pts, 'blue', label= r'$cos(2*pi*t)$')
    
    plt.plot(t1_vals, x1_pts, 'red', label=r'$h=0.2$')
    plt.plot(t2_vals, x2_pts, 'blue', label=r'$h=0.1$')
    plt.plot(t3_vals, x3_pts, 'green', label=r'$h=0.5$')
    
    plt.title(name)
    
    plt.grid(True)
    plt.axis([0, 1.2, -.7, .5], 'equal')

    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')

    plt.legend(loc='lower right')

    plt.show()

def plotAll(name,x1_vals,x2_vals,x3_vals,t1_vals,t2_vals,t3_vals):
    t_pts = arange(0,2,.001)
    x_pts = [fn_x(i) for i in t_pts]
    
    # Plot it against the exact equation
    plt.plot(t_pts, x_pts, 'magenta', label= r'$cos(2*pi*t)$')
    
    plt.plot(t1_vals, x1_vals, 'red', label=r'$h=0.2$')
    plt.plot(t2_vals, x2_vals, 'blue', label=r'$h=0.1$')
    plt.plot(t3_vals, x3_vals, 'green', label=r'$h0.5$')
    
    plt.title(name)
    
    plt.grid(True)
    plt.axis([0, 1.2, -1.5, 1.5], 'equal')

    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')

    plt.legend(loc='lower right')

    plt.show()
    
def table(t, x, y, m):
    print("|  %.3f    |  %.7f    |  %.7f   |" %(t, x, y))

def fn_x(t):
    return cos(2*pi*t)

def dy_dt(t,x,y):
    return (-4)*(pi**2)*x

def main():
    print("EULER'S METHOD: h = 0.2")
    print("---------------------------------------------")
    print("|     t     |       x       |       y       |")
    print("---------------------------------------------")
    euler (dy_dt, 0, 1, 0, 0.2)
    print("---------------------------------------------")
    solution_graph("EULER'S METHOD: h = 0.2")
    x1_vals = copyV(x_vals)
    t1_vals = copyV(t_vals)
    
    print("EULER'S METHOD: h = 0.1")
    print("---------------------------------------------")
    print("|     t     |       x       |       y       |")
    print("---------------------------------------------")
    euler (dy_dt, 0, 1, 0, 0.1)
    print("---------------------------------------------")
    solution_graph("EULER'S METHOD: h = 0.1")
    x2_vals = copyV(x_vals)
    t2_vals = copyV(t_vals)

    

    print("EULER'S METHOD: h = 0.05")
    print("---------------------------------------------")
    print("|     t     |       x       |       y       |")
    print("---------------------------------------------")
    euler (dy_dt, 0, 1, 0, 0.05)
    print("---------------------------------------------")
    solution_graph("EULER'S METHOD: h = 0.05")
    x3_vals = copyV(x_vals)
    t3_vals = copyV(t_vals)
    error_graph("Error Graphs of Euler Method",x1_vals,x2_vals,x3_vals,t1_vals,t2_vals,t3_vals)
    plotAll("Euler methods vs exact solution",x1_vals,x2_vals,x3_vals,t1_vals,t2_vals,t3_vals)
    
"""
    print("EULER MODIFIED METHOD: h = 0.2")
    print("-------------------------------------------------------------")
    print("|     t     |       x       |       y       |     slope     |")
    print("-------------------------------------------------------------")
    euler_modified (dy_dt, 0, 1, 0, 0.2)
    print("-------------------------------------------------------------")
    solution_graph("EULER MODIFIED METHOD: h = 0.2")

    print("EULER MODIFIED METHOD: h = 0.1")
    print("-------------------------------------------------------------")
    print("|     t     |       x       |       y       |     slope     |")
    print("-------------------------------------------------------------")
    euler_modified (dy_dt, 0, 1, 0, 0.1)
    print("-------------------------------------------------------------")
    solution_graph("EULER MODIFIED METHOD: h = 0.1")

    print("EULER MODIFIED METHOD: h = 0.05")
    print("-------------------------------------------------------------")
    print("|     t     |       x       |       y       |     slope     |")
    print("-------------------------------------------------------------")
    euler_modified (dy_dt, 0, 1, 0, 0.05)
    print("-------------------------------------------------------------")
    solution_graph("EULER MODIFIED METHOD: h = 0.05")

    print("RK-4 METHOD: h = 0.20")
    print("-------------------------------------------------------------")
    print("|     t     |       x       |       y       |     slope     |")
    print("-------------------------------------------------------------")
    rk4 (dy_dt, 0, 1, 0, 0.2)
    print("-------------------------------------------------------------")
    solution_graph("RK-4 METHOD: h = 0.2")

    print("RK-4 METHOD: h = 0.1")
    print("-------------------------------------------------------------")
    print("|     t     |       x       |       y       |     slope     |")
    print("-------------------------------------------------------------")
    rk4 (dy_dt, 0, 1, 0, 0.1)
    print("-------------------------------------------------------------")
    solution_graph("RK-4 METHOD: h = 0.1")

    print("RK-4 METHOD: h = 0.05")
    print("-------------------------------------------------------------")
    print("|     t     |       x       |       y       |     slope     |")
    print("-------------------------------------------------------------")
    rk4 (dy_dt, 0, 1, 0, 0.05)
    print("-------------------------------------------------------------")
    solution_graph("RK-4 METHOD: h = 0.05")

"""
main()
