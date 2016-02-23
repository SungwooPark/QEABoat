
'''
Quantitative Engineering Analysis course Spring 2016
Boat Design calculation code
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.optimize import fsolve
import math

def righting_arm(n,theta):
    '''
        Returns a coordinate and magitude of righting moment of the boat
    '''
    
    d = .5 #compare() will replace this

    y = np.linspace(-1,1,1000)
    f1 = np.absolute(y)**n - 1 #Hull function without lambda    
    f2 = -np.tan(theta)*y - d

    hull_function = lambda y: np.absolute(y)**n - 1
    d = compare(hull_function,n,theta)
    water_line = lambda y: -np.tan(theta)*y - d
    
    print 'd: ', d

    #print "cob: ", cob(hull_function, water_line,n,theta,d)

    #varying_theta_calc_displacement(n,d)
  
    f2 = -np.tan(theta)*y - d

    plot_graph(f1, f2,hull_function,water_line,intersection(hull_function,water_line,n,theta,d))
   
def intersection(hull_func,water_func,n,theta,d):
    '''
        Takes in function representation of hull and water line and then returns the roots
    '''
    func_difference = lambda y: (-np.tan(theta)*y - d) - (np.absolute(y)**n - 1)
    root = fsolve(func_difference,[-10,10])

    #print 'init root: ',root
    if theta > math.radians(80) and theta < math.radians(90):
        root[0] = fsolve(water_func,0)
        root[1] = fsolve(func_difference,0)
    elif theta > math.radians(90) and theta < math.radians(100):
        root[0] = fsolve(func_difference,0)
        root[1] = fsolve(water_func,0)
    elif np.absolute(root[0]) > 1:
        root[0] = fsolve(water_func,0)
    elif np.absolute(root[1]) >1:
        root[1] = fsolve(water_func,0)
    #print 'this is root', root
    return root

def displacement(hull_func, water_func,n,theta,m):
    '''
        returns a volume under water
        args: limits - a list with 2 elements (roots)
    '''
    limits = intersection(hull_func, water_func,n,theta,m)
    func_difference_down = lambda y: (-np.tan(theta)*y - m)- (np.absolute(y)**n - 1)
    func_difference_up = lambda y: (-np.tan(theta)*y - m)
    
   # print "root value: ", abs(water_func(limits[0]))

    if abs(water_func(limits[0]))<0.01:
        area1 = np.absolute(integrate.quad(hull_func,-1,limits[0])[0])
        #print 'area1: ',area1
        area2 = integrate.quad(func_difference_down,limits[0],limits[1])[0]
        #print 'area2: ',area2
        displacement = area1 + area2
        #print 'displacement: ',displacement
    elif abs(water_func(limits[1]))<0.01:
        area1 = np.absolute(integrate.quad(hull_func,-1,limits[0])[0])
        #print 'area1: ',area1
        area2 = np.absolute(integrate.quad(func_difference_up,limits[0],limits[1])[0])
        #print 'area2: ',area2
        displacement = area1 + area2
        #print 'displacement: ',displacement
    else:     
        displacement = integrate.quad(func_difference_down,limits[0],limits[1])[0]
        #print "displacement volume: ", displacement
    return displacement
    
def total_mass(hull_func,n,theta):
    '''
        returns a total mass of hull in kg / m^3
    '''
    density = 31.7 #kg/m^3
    volume = -integrate.quad(hull_func,-1,1)[0]
    mass = density * volume
    return mass

def compare(hull_func,n,theta):
    '''
        returns a value of d in which buoyancy = gravitational force
    '''
    d = np.linspace(-10,10,20000)
    for num in d:
        displaced_water = displacement(hull_func,lambda y: -np.tan(theta)*y - num,n,theta,num)
        buoyancy = 1000 * displaced_water
        #print "buoyancy: ", buoyancy
        #print "dispaced_water", displaced_water
        #print "total mass: ", total_mass(hull_func,n,theta)
        #print "diff: ", np.absolute(total_mass(hull_func,n,theta)-buoyancy)
        if np.absolute(total_mass(hull_func,n,theta)-buoyancy) < 0.5:
            return num
    return "Error 404: d not found"
 
def plot_graph(hull,waterline,lambda_hull,lambda_waterline,intersection_points):
    '''
        plots the graph of the hull and water line
        args: intersection_points - a list of x coord of intersection of boat and waterline
    '''
    
    #Reset axes
    axes = plt.gca()
    axes.set_xlim([-1.7,1.7])
    axes.set_ylim([-2,2]) 

    root1 = intersection_points[0]
    root2 = intersection_points[1]

    y = np.linspace(-1,1,1000)
    plt.plot(y,hull)
    plt.plot(y,waterline)
    plt.plot([-2,2],[0,0])

    if np.absolute(lambda_waterline(root1)) < 0.01 or np.absolute(lambda_waterline(root2)) < 0.01:
        plt.plot([root1,root2],[lambda_waterline(root1),lambda_waterline(root2)], 'ro')
    else:
        plt.plot([root1,root2],[lambda_hull(root1),lambda_hull(root2)], 'ro')
    
    plt.show()

def varying_theta_calc_displacement(n,d):
    thetas = np.linspace(0,math.radians(140),80)
    displacements = []
    for angle in thetas:
        #print 'angle: ',angle
        displacements.append(displacement(lambda y: np.absolute(y)**n - 1,
            lambda y: -np.tan(angle)*y - d,n,angle,d))
    #print displacements
    axes = plt.gca()
    axes.set_ylim([0.4,0.8])
    plt.plot(thetas,displacements)
    plt.show()

def cob(hull_func, water_func,n,theta,m):
    disp = displacement(hull_func, water_func,n,theta,m)

    limits = intersection(hull_func, water_func,n,theta,m)
    
    #this is just here for reference, equations for mass of watah
    func_difference_down = lambda y: (-np.tan(theta)*y - m)- (np.absolute(y)**n - 1)
    func_difference_up = lambda y: (-np.tan(theta)*y - m)
    
    #equations for moment in z direction
    func_difference_down_z = lambda y: ((-np.tan(theta)*y - m)- (np.absolute(y)**n - 1))*y
    func_difference_up_z = lambda y: ((-np.tan(theta)*y - m)*y)*y
    hull_func_z = lambda y: (np.absolute(y)**n - 1)*y
   
    #equations for moment in y direction
    func_difference_down_y = lambda y: .5*((-np.tan(theta)*y - m)**2- (np.absolute(y)**n - 1)**2)
    func_difference_up_y = lambda y: .5*((-np.tan(theta)*y)**2 - m**2)
    hull_func_y = lambda y: .5*(-(np.absolute(y)**n - 1)**2)

    if abs(water_func(limits[0]))<0.01:
        area1_z = np.absolute(integrate.quad(hull_func_z,-1,limits[0])[0])
        area1_y = np.absolute(integrate.quad(hull_func_y,-1,limits[0])[0])
        #print 'area1: ',area1
        area2_z = integrate.quad(func_difference_down_z,limits[0],limits[1])[0]
        area2_y = integrate.quad(func_difference_down_y,limits[0],limits[1])[0]
        #print 'area2: ',area2
        disp_z = .5*(area1_z + area2_z)
        disp_y = .5*(area1_y + area2_y)
        #print 'displacement: ',displacement
    elif abs(water_func(limits[1]))<0.01:
        area1_z = np.absolute(integrate.quad(hull_func_z,-1,limits[0])[0])
        area1_y = np.absolute(integrate.quad(hull_func_y,-1,limits[0])[0])
        #print 'area1: ',area1
        area2_z = np.absolute(integrate.quad(func_difference_up_z,limits[0],limits[1])[0])
        area2_y = np.absolute(integrate.quad(func_difference_up_y,limits[0],limits[1])[0])
        #print 'area2: ',area2
        disp_z = .5*(area1_z + area2_z)
        disp_y = .5*(area1_y + area2_y)
        #print 'displacement: ',displacement
    else:     
        disp_z = integrate.quad(func_difference_down_z,limits[0],limits[1])[0]
        disp_y = integrate.quad(func_difference_down_y,limits[0],limits[1])[0]

        #print "displacement volume: ", displacement
    print "z: ", (-1 + disp_z)
    print "y: ", (-1 + disp_y) 
    return (disp_y,disp_z)


righting_arm(2, math.radians(130))
