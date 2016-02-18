import numpy as np
import matplotlib.pyplot as plt

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

boat_plot(4,np.pi/4,1.2)
