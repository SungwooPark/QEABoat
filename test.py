import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad

def boat_plot(n,theta,d):
    plt.clf()

    axes = plt.gca()
    axes.set_xlim([-1,1])
    axes.set_ylim([-1.25, 0])

    y = np.linspace(-1,1,100) #range of function
    f1 = np.absolute(y)**n - 1
    f2 = -np.tan(theta)* y - d
    plt.plot(y,f1)
    plt.plot(y,f2)

    pts = intersection_point(f1,f2,y)    

    plt.plot(pts[0], pts[1], 'ro')

    plt.show()

def com(n,density):
    """
    Takes in value of n and density of a boat and returns a tuple of horizontal and vertiacal center of mass point
    """
    total_mass = dblquad(lambda z,y: density, -1,1, lambda y:np.absolute(y)**n-1,lambda y:0)[0]
    return (dblquad(lambda z,y: density*y,-1,1,lambda y:np.absolute(y)**n-1,lambda y:0)[0]/total_mass,dblquad(lambda z,y: density*z,-1,1,lambda y:np.absolute(y)**n-1,lambda y:0)[0]/total_mass)

def intersection_point(f1,f2,x):
    """
    Takes in input range x, two functions and returns an coordintaes of intersection points
    As a two list - one for x coordinates and one for y coordinate
    """
    idx = np.argwhere(np.isclose(f1,f2, atol=0.01)).reshape(-1)
    return (x[idx], f1[idx])

boat_plot(4,np.pi/4,1.2)

#print dblquad(lambda z,y: 100*y,-1,1,lambda y:np.absolute(y)**2-1,lambda y:0)
#print dblquad(lambda z,y: 100*z,-1,1,lambda y:np.absolute(y)**2-1,lambda y:0)

#print com(2,100)
#print com(3,100)
#print com(4,100)
