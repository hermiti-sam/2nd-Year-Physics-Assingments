import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Circle, PathPatch
from mpl_toolkits.mplot3d import Axes3D 
import mpl_toolkits.mplot3d.art3d as art3d

class Object:
    def __init__(self, Name, Radius, Mass):
        self.Name = Name
        self.Radius = Radius
        self.Mass = Mass
        
        
def givenfunctions(x, y, function: str):
    """
    This function defines the 8 different derivatives needed to evaluate all the k's.
    These come directly from the notes provided
    """
    
    if function == 'f3':
        return -(G * Earth.Mass * x) / ((x**2 + y**2)**(3/2))
    elif function == 'f4':
        return -(G * Earth.Mass * y) / ((x**2 + y**2)**(3/2))
        

    

def RungeKutta(x, y, vx, vy, t, Body = str):
    """
    This function creates the k values given in the notes and uses them to calculate the 
    required values for each time-step.

    """
    k1x = vx
    k1y = vy
    k1vx = givenfunctions(x, y, 'f3')
    k1vy = givenfunctions(x, y, 'f4')
    


    k2x = vx + (h / 2) * k1vx
    k2y = vy + (h / 2) * k1vy
    k2vx = givenfunctions(x + (h / 2) * k1x, y + (h / 2) * k1y, 'f3')
    k2vy = givenfunctions(x + (h / 2) * k1vx, y + (h / 2) * k1vy,  'f4')
    


    k3x = vx + (h / 2) * k2vx
    k3y = vy + (h / 2) * k2vy
    k3vx = givenfunctions(x + (h / 2) * k2x, y + (h / 2) * k2y, 'f3')
    k3vy = givenfunctions(x + (h / 2) * k2vx, y + (h / 2) * k2vy, 'f4')
    


    k4x = vx + h * k3vx
    k4y = vy + h * k3vy 
    k4vx = givenfunctions(x + h * k3x, y + h  * k3y, 'f3')
    k4vy = givenfunctions(x + h * k3vx, y + h * k3vy, 'f4')
   
    
    
    k1 = k1x, k1y, k1vx, k1vy
    k2 = k2x, k2y, k2vx, k2vy
    k3 = k3x, k3y, k3vx, k3vy
    k4 = k4x, k4y, k4vx, k4vy



# Here I define the time-stepping equations given in the notes. It is comprised of the k values
#that have been defined and sorted into an array.
    x += (h / 6) * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
    y += (h / 6) * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    vx += (h / 6) * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2])
    vy += (h / 6) * (k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3])
    t += h 



    
    return x, y, vx, vy, t

def Energy(x, y, vx, vy):
    """
    This function calculates the kinetic (ek), potential (u), and the total energy(et) to 
    investigate conservation of energy for the orbital trajectories plotted
    

    """

    ek = (1 / 2) * Rocket.Mass * (vx ** 2 + vy ** 2)
    u = (G * Earth.Mass * Rocket.Mass) * (vx ** 2 + vy ** 2)
    et = ek + u
    return ek, u, et






#def plotcircular(x, y, t, ek, u, et):
## here i give the objects properties and define constants to be used when plotting
Earth = Object('Earth', 6.371e6, 5.972e24)
Rocket = Object('Rocket',0, 4.276e6)
Moon = Object('Moon', 1.731e6, 7.342e22)
G = 6.67e-11
h = 1


def circularorbit_3d():

    """
    Here i defined a function to plot the 3d orbital trajectory of the rocket for the
    circular orbit conditions
    """
    numpoints = 20000


    x = np.zeros(numpoints)
    y = np.zeros(numpoints)
    vx = np.zeros(numpoints)
    vy = np.zeros(numpoints)
    t = np.zeros(numpoints)
    
    x[0] = 6e6+Earth.Radius
    y[0] = 0
    vx[0] = 0
    vy[0] = np.sqrt(G * Earth.Mass / x[0])
    

    for i in range(0, numpoints - 1):
        x[i+1], y[i+1], vx[i+1], vy[i+1], t[i+1] = RungeKutta(x[i], y[i], vx[i], vy[i], t[i])
    
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    z = 0
    ax.plot(x, y, z, color = 'black', linewidth = 1,)
    #ax.axis('square')
    ax.set_xlabel('Horizontal Displacement (m)')
    ax.set_ylabel('Vertical Displacement (m)')


    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x = 6e6 * np.outer(np.cos(u), np.sin(v))
    y = 6e6* np.outer(np.sin(u), np.sin(v))
    z = 6e6 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='grey')
    ax.set_xlim3d(-1.5e7, 1.5e7)
    ax.set_ylim3d(-1.5e7, 1.5e7)
    ax.set_zlim3d(-1.5e7, 1.5e7)

    plt.show()
    


def circularorbit_2d():
    
    numpoints = 200000

    x = np.zeros(numpoints)
    y = np.zeros(numpoints)
    vx = np.zeros(numpoints)
    vy = np.zeros(numpoints)
    t = np.zeros(numpoints)
    
    x[0] = 6e6+Earth.Radius
    y[0] = 0
    vx[0] = 0
    vy[0] = np.sqrt(G * Earth.Mass / x[0])
    

    for i in range(0, numpoints - 1):
        x[i+1], y[i+1], vx[i+1], vy[i+1], t[i+1] = RungeKutta(x[i], y[i], vx[i], vy[i], t[i])
    fig, ax = plt.subplots()
    ax.plot(x, y, color = 'black', linewidth = 1)
    ax.axis('square')
    ax.set_xlabel('Horizontal Displacement (m)')
    ax.set_ylabel('Vertical Displacement (m)')
    ax.add_patch(plt.Circle((0, 0), 6.371e6, color='darkgray', label='Earth'))
    plt.show()







