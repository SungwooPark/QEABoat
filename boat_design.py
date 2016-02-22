'''
Quantitative Engineering Analysis course Spring 2016
Boat Design calculation code
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.optimize import fsolve

def righting_arm(n,theta):
    '''
        Returns a coordinate and magitude of righting moment of the boat
    '''
    
    d = 1 #compare() will replace this

    y = np.linspace(-1,1,1000)
    f1 = np.absolute(y)**n - 1 #Hull function without lambda    
    f2 = -np.tan(theta)*y - d

    hull_function = lambda y: np.absolute(y)**n - 1
    water_line = lambda y: -np.tan(theta)*y - d
    
    displacement(hull_function, water_line,n,theta,d) 
    plot_graph(f1, f2)
   
def intersection(hull_func,water_func,n,theta,d):
    '''
        Takes in function representation of hull and water line and then returns the roots
    '''
    func_difference = lambda y: (-np.tan(theta)*y - d) - (np.absolute(y)**n - 1)
    root = fsolve(func_difference,[-1,1])
    if np.absolute(root[0]) > 1:
        root[0] = fsolve(water_func,0)
    elif np.absolute(root[1]) >1:
        root[1] = fsolve(water_func,0)
    return root

def displacement(hull_func, water_func,n,theta,d):
    '''
        Finds a volume under water
        args: limits - a list with 2 elements (roots)
    '''
    limits = intersection(hull_func, water_func,n,theta,d)
    func_difference = lambda y: (-np.tan(theta)*y - d)- (np.absolute(y)**n - 1)
    
    if abs(water_func(limits[0]))<0.01:
        area1 = np.absolute(integrate.quad(hull_func,-1,limits[0])[0])
        print 'area1: ',area1
        area2 = integrate.quad(func_difference,limits[0],limits[1])[0]
        print 'area2: ',area2
        displacement = area1 + area2
        print 'displacement: ',displacement
    else:     
        limits = intersection(hull_func, water_func,n,theta,d)
        result = integrate.quad(func_difference,limits[0],limits[1])
        print "displacement volume: ", result[0]
 
def plot_graph(hull,waterline):
    '''
        plots the graph of the hull and water line
    '''
    
    #Reset axes
    axes = plt.gca()
    axes.set_xlim([-1.7,1.7])
    axes.set_ylim([-2,2])    

    y = np.linspace(-1,1,1000)
    plt.plot(y,hull)
    plt.plot(y,waterline)
    plt.plot([-1,1],[0,0])
    plt.show()

righting_arm(2,np.pi/2-0.03)
