import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad
from scipy.integrate import quad
from scipy.optimize import fsolve

# pos_moment = True
d_range = np.linspace(-1,1,1000)
d = d_range[0]
theta = np.pi/4
n = 4
flag = False

def func2(y):
    global d
    global theta
    global n
    return -np.tan(theta)*y - d - (np.absolute(y)**n -1)

def func1(y):
    global d
    global theta
    return -np.tan(theta)*y - d

def boat_plot():
    print "boat plot called"
    global d
    global theta
    global n
    global flag
   
    for num in d_range:
        #print 'Num is ;;;;', num
        d = num
        if flag == True:
            break
    
    # if theta > np.py/2:
    #     theta = np.py/2 - theta
    #     global pos_moment 

       #plt.clf()

        # axes = plt.gca()
        # axes.set_xlim([-1.7,1.7])
        # axes.set_ylim([-2, 2])

        y = np.linspace(-1,1,1000) #range of function
        f1 = np.absolute(y)**n - 1
        f2 = -np.tan(theta)* y - d
        # plt.plot(y,f1)
        # plt.plot(y,f2)

        pts = intersection_point(f1,f2,y)    
    #    print pts[1]


        #plt.plot(pts[0], pts[1], 'ro')

        #displacement(pts)
        print compare(pts)
        #plt.show()

    plt.clf()

    axes = plt.gca()
    axes.set_xlim([-1.7,1.7])
    axes.set_ylim([-2, 2])
    f1 = np.absolute(y)**n - 1
    f2 = -np.tan(theta)* y - d
    plt.plot(y,f1)
    plt.plot(y,f2)
    plt.plot(pts[0], pts[1], 'ro')
    plt.show()


<<<<<<< HEAD
def compare(intersect):
    global d
    global flag
    buoyancy = 1000*displacement(intersect)[0]
    total_mass = dblquad(lambda z,y: 500, -1,1, lambda y:np.absolute(y)**n-1,lambda y:0)[0]
    #print buoyancy
    if (abs(-float(buoyancy)-float(total_mass))) < 5:
        print "buoyancy: ", str(buoyancy)
        print "total_mass", total_mass
        print "difference is " + str(abs(-float(buoyancy)-float(total_mass)))
        flag = True
        print "flag", flag
        return d
    return "Not working need to figure out what the hell is going on. Why is my life consumed by code. I eat breathe sleep python. go paul and ben! paul plz answer my email!"

=======
    plt.plot(pts[0], pts[1], 'ro')
    center_of_mass = com(n,100)
    plt.plot([center_of_mass[0]],[center_of_mass[1]], 'ro') #plot com
>>>>>>> e04d82eeb262f9330afb18a0ab04e60cf45903c3


def com(density):
    """
    Takes in value of n and density of a boat and returns a tuple of horizontal and vertiacal coordinate of center of mass point
    """
    total_mass = dblquad(lambda z,y: density, -1,1, lambda y:np.absolute(y)**n-1,lambda y:0)[0]
    return (dblquad(lambda z,y: density*y,-1,1,lambda y:np.absolute(y)**n-1,lambda y:0)[0]/total_mass,dblquad(lambda z,y: density*z,-1,1,lambda y:np.absolute(y)**n-1,lambda y:0)[0]/total_mass)

def intersection_point(f1,f2,x):
    """
    Takes in input range x, two functions and returns an coordintaes of intersection points
    As two lists - one for x coordinates and one for y coordinate
    """

<<<<<<< HEAD
#def func2(y):
    #return np.absolute(y)**2 - 1- (-np.tan(np.pi/4)*y - 1.2)

    root = fsolve(func2,[-1,1])
    print 'this is root', np.absolute(root[0])
    if np.absolute(root[0]) > 1:
        #print ' this shit works yo'
        root[0] = fsolve(func1,0)
    print 'root', root
    print type(root)


  #  print 'root' + str(root)
  #  idx = np.argwhere(np.isclose(f1,f2, atol=0.005)).reshape(-1)
   # return (x[idx], f1[idx])
    return(root,[func1(root[0]),func1(root[1])])

def displacement(intersect):
    global d
    global theta
    global n
    y = np.linspace(-1,1,1000)
    f1 = np.absolute(y)**n - 1
    f2 = -np.tan(theta)* y - d
    #print intersect[0]
    print 'intersect', intersect[0][0]
    print 'if statement', abs(intersect[0] - 0)
    if abs(intersect[0][0] - 0) > 0.01:
        print 'booooat'
        start_y = intersect[0][0] 
        end_y = intersect[0][1]
        return quad(lambda y: -np.tan(theta)*y - d - np.absolute(y)**n -1,start_y,end_y)
    else: 
        p1 = intersect[0][0]
        integ1 = quad(lambda y: -np.absolute(y)**n-1,-1,p1)
        print 'integ1', integ1
        print 'asdassadsa'
        # new_f1 = 0
        # p1 = intersection_point(new_f1,f2,y)
        # p
        return (21312,)
    
boat_plot()
=======
boat_plot(3,np.pi/4,1.2)
boat_plot(1,np.pi/3,1.2)
>>>>>>> e04d82eeb262f9330afb18a0ab04e60cf45903c3

#print dblquad(lambda z,y: 100*y,-1,1,lambda y:np.absolute(y)**2-1,lambda y:0)
#print dblquad(lambda z,y: 100*z,-1,1,lambda y:np.absolute(y)**2-1,lambda y:0)

#print com(2,100)
#print com(3,100)
#print com(4,100)
