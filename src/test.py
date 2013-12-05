'''
Created on Nov 30, 2013

@author: Wilson Yan
'''
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols
from sympy.plotting import plot, plot3d
import matplotlib.pyplot as plt
import numpy as np

def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)  
    plt.show()
    
def graph2(x,y):
    plt.plot(x,y)
    plt.show()


