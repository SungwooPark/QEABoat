import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad

def boat_plot(n,theta,d):
    plt.clf()

    axes = plt.gca()
    axes.set_xlim([-1,1])
    axes.set_ylim([-1.25, 0])

    y = np.linspace(-1,1,100)
    f1 = np.absolute(y)**n - 1
    f2 = -np.tan(theta)* y - d
    plt.plot(y,f1)
    plt.plot(y,f2)

    plt.show()

def com(n,density):
    #still have to divide this thing by total mass
    total_mass = dblquad(lambda z,y: density, -1,1, lambda y:np.absolute(y)**n-1,lambda y:0)[0]
    return (dblquad(lambda z,y: density*y,-1,1,lambda y:np.absolute(y)**n-1,lambda y:0)[0]/total_mass,dblquad(lambda z,y: density*z,-1,1,lambda y:np.absolute(y)**n-1,lambda y:0)[0]/total_mass)

#boat_plot(4,np.pi/4,1.2)

#print dblquad(lambda z,y: 100*y,-1,1,lambda y:np.absolute(y)**2-1,lambda y:0)
#print dblquad(lambda z,y: 100*z,-1,1,lambda y:np.absolute(y)**2-1,lambda y:0)

print com(2,100)
print com(3,100)
print com(4,100)
