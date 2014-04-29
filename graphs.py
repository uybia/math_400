import trapezoid 
from math import *
import matplotlib.pyplot as plt
from numpy import arange

def graph1():
    x_vals = arange(0,2,.001)
    y_vals = [trapezoid.sin_pi(i) for i in x_vals]
    plt.plot(x_vals, y_vals)
    plt.grid(True)
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')
    plt.title(r'$sin(pi*x)$')
    plt.show()


def graph2():
    x_vals = arange(0,2.5,.001)
    y_vals = [trapezoid.e_2(i) for i in x_vals]
    plt.plot(x_vals, y_vals)
    plt.grid(True)
    #plt.axis([0.0, 2.0, 0.0, 1.0], 'equal')
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')
    plt.title(r'$e**((-x**2)/2)$')
    plt.show()

def graph3():
    x_vals = arange(-1.0,1.0,.001)
    y_vals = [trapezoid.sinc(i) for i in x_vals]
    plt.plot(x_vals, y_vals)
    plt.grid(True)
    plt.axis([-1.0, 1.0, -.30, 1.07], 'equal')
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')
    plt.title(r'$Sinc(2*pi*x)$')
    plt.show()


graph1()
graph2()
graph3()
