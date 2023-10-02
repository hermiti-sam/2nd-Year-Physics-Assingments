import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Circle, PathPatch
from mpl_toolkits.mplot3d import Axes3D 
import mpl_toolkits.mplot3d.art3d as art3d

class Object: #a function to assign parameters to objects, such as planets, rockets etc.
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
        f3 = -(G * Earth.Mass * x) / ((x**2 + y**2)**(3/2))
        return f3
    elif function == 'f4':
        f4 = -(G * Earth.Mass * y) / ((x**2 + y**2)**(3/2))
        return f4


    if function == 'f3moon': # i use if statements to specify which scenario to use
        f3moon = -(G * Earth.Mass * x) / ((x**2 + y**2)**(3/2)) - ((G * Moon.Mass * x) / (x**2 + (y-Rm)**2)**(3/2)) 
        # we have to take into account the separation of earth and moon in this scenario, hence the extra Rm term
        return f3moon
    if function == 'f4moon':
        f4moon = -(G * Earth.Mass * y) / ((x**2 + y**2)**(3/2)) - ((G * Moon.Mass * (y-Rm)) / (x**2 + (y-Rm)**2)**(3/2))
        return f4moon


def RungeKutta(x, y, vx, vy, t):
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


def RungeKuttaMoon(x, y, vx, vy, t):
    """
    This function creates the k values given in the notes and uses them to calculate the 
    required values for each time-step for the two-body simulation.

    """
    k1x = vx
    k1y = vy
    k1vx = givenfunctions(x, y, 'f3moon')
    k1vy = givenfunctions(x, y, 'f4moon')
    


    k2x = vx + (h / 2) * k1vx
    k2y = vy + (h / 2) * k1vy
    k2vx = givenfunctions(x + (h / 2) * k1x, y + (h / 2) * k1y, 'f3moon')
    k2vy = givenfunctions(x + (h / 2) * k1vx, y + (h / 2) * k1vy,  'f4moon')
    


    k3x = vx + (h / 2) * k2vx
    k3y = vy + (h / 2) * k2vy
    k3vx = givenfunctions(x + (h / 2) * k2x, y + (h / 2) * k2y, 'f3moon')
    k3vy = givenfunctions(x + (h / 2) * k2vx, y + (h / 2) * k2vy, 'f4moon')
    


    k4x = vx + h * k3vx
    k4y = vy + h * k3vy 
    k4vx = givenfunctions(x + h * k3x, y + h  * k3y, 'f3moon')
    k4vy = givenfunctions(x + h * k3vx, y + h * k3vy, 'f4moon')
   
    
    
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


def Energy(x, y, vx, vy, body = str):
    """
    This function calculates the kinetic (ek), potential (u), and the total energy(et) to 
    investigate conservation of energy for the orbital trajectories plotted.
    

    """

    Kinetic = (1 / 2) * Rocket.Mass * (vx ** 2 + vy ** 2) #kinetic energy, stays same, irrelevant of scenario

    if body == 'One': #for just the earth orbits
        Potential = (-G * Earth.Mass * Rocket.Mass) / (x ** 2 + y ** 2)**(1/2)

    elif body == 'Two': # for the earth-moon scenarios
        Potential = (-G * Earth.Mass * Rocket.Mass) / (x ** 2 + y ** 2)**(1/2) + (-G * Moon.Mass * Rocket.Mass)/(x ** 2 + y ** 2)**(1/2) #again we have to consider the separation

    Total = Kinetic + Potential #simple sum
    return Kinetic, Potential, Total






#def plotcircular(x, y, t, ek, u, et):
## here i give the objects properties and define constants to be used when plotting
Earth = Object('Earth', 6.371e6, 5.972e24)
Rocket = Object('Rocket',0, 4.276e6)
Moon = Object('Moon', 1.731e6, 7.342e22)
G = 6.67e-11 #gravitational constant
h = 1 #step-size
Rm = 3.844e8 #distance between earth and moon


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
    ax.set_xlabel('Horizontal Displacement(m)')
    ax.set_ylabel('Vertical Displacement(m)')


    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x = 6e6 * np.outer(np.cos(u), np.sin(v))
    y = 6e6* np.outer(np.sin(u), np.sin(v))
    z = 6e6 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='blue')
    ax.set_xlim3d(-1.5e7, 1.5e7)
    ax.set_ylim3d(-1.5e7, 1.5e7)
    ax.set_zlim3d(-1.5e7, 1.5e7)

    plt.show()
    


def circularorbit_2d():
    """
    Function to plot the orbital trajectory of the rocket, aswell as it's energy components for the entire trip
    """
    numpoints = 30000 #num of numpoints in the simulations

    x = np.zeros(numpoints) #start with arrays of zeros to fill them later
    y = np.zeros(numpoints)
    vx = np.zeros(numpoints)
    vy = np.zeros(numpoints)
    Kinetic = np.zeros(numpoints)
    Potential = np.zeros(numpoints)
    Total = np.zeros(numpoints)
    t = np.zeros(numpoints)
    
    x[0] = 6e6+Earth.Radius #initial conditions
    y[0] = 0
    vx[0] = 0
    vy[0] = np.sqrt(G * Earth.Mass / x[0])
    

    for i in range(numpoints - 1):
        x[i+1], y[i+1], vx[i+1], vy[i+1], t[i+1] = RungeKutta(x[i], y[i], vx[i], vy[i], t[i])
        Kinetic[i], Potential[i], Total[i] = Energy(x[i], y[i], vx[i], vy[i], 'One')

    fig = plt.figure() 
    ax = plt.gca()
    ax.plot(x, y, color = 'black', linewidth = 1)
    ax.axis('square')
    ax.set_xlabel('Horizontal Displacement(m)')
    ax.set_ylabel('Vertical Displacement(m)')
    ax.add_patch(plt.Circle((0, 0), 6.371e6, color='blue', label='Earth'))
    plt.show()

    plt.plot(t, Kinetic, label = 'Kinetic Energy')
    plt.plot(t, Potential, label = 'Gravitational Potential Energy')
    plt.plot(t, Total, label = 'Sum of Kinetic and Potential Energies')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy (J)')
    plt.legend()
    plt.show()
    print("Initial Velocity: ", np.sqrt(G * Earth.Mass / 6e6+Earth.Radius))




def ellipticalorbit2d():
    """
    Function to plot the elliptical orbit of the rocket, aswell as it's energy components
    """


    numpoints = 293527

    x = np.zeros(numpoints)
    y = np.zeros(numpoints)
    vx = np.zeros(numpoints)
    vy = np.zeros(numpoints)
    Kinetic = np.zeros(numpoints)
    Potential = np.zeros(numpoints)
    Total = np.zeros(numpoints)
    t = np.zeros(numpoints)
    
    x[0] = 6e6+Earth.Radius
    y[0] = 0
    vx[0] = 0
    vy[0] = 7600 #have to specify the initial velocity here, found just by increasing it from 7000, until the orbit required was obtained

    for i in range(numpoints - 1):
        x[i+1], y[i+1], vx[i+1], vy[i+1], t[i+1] = RungeKutta(x[i], y[i], vx[i], vy[i], t[i])
        Kinetic[i], Potential[i], Total[i] = Energy(x[i], y[i], vx[i], vy[i], 'One')
    fig = plt.figure() 
    ax = plt.gca()
    ax.plot(x, y, color = 'black', linewidth = 1)
    ax.axis('square')
    ax.set_xlabel('Horizontal Displacement (m)')
    ax.set_ylabel('Vertical Displacement (m)')
    ax.set_ylim(-4e7, 4e7)
    ax.add_patch(plt.Circle((0, 0), 6.371e6, color='blue', label='Earth'))
    plt.show()

    plt.plot(t, Kinetic, label = 'Kinetic Energy')
    plt.plot(t, Potential, label = 'Gravitational Potential Energy')
    plt.plot(t, Total, label = 'Sum of Kinetic and Potential Energies')
    plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
    plt.xlabel('Time (s)')
    plt.ylabel('Energy (J)')
    plt.legend()
    plt.show()


def ellipticalorbit_3d():

    """
    Here i defined a function to plot the 3d orbital trajectory of the rocket for the
    circular orbit conditions
    """
    numpoints = 293527


    x = np.zeros(numpoints)
    y = np.zeros(numpoints)
    vx = np.zeros(numpoints)
    vy = np.zeros(numpoints)
    t = np.zeros(numpoints)
    
    x[0] = 6e6+Earth.Radius
    y[0] = 0
    vx[0] = 0
    vy[0] = 7600
    

    for i in range(0, numpoints - 1):
        x[i+1], y[i+1], vx[i+1], vy[i+1], t[i+1] = RungeKutta(x[i], y[i], vx[i], vy[i], t[i])
    
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    z = 0
    ax.plot(x, y, z, color = 'black', linewidth = 1,)
    #ax.axis('square')
    ax.set_xlabel('Horizontal Displacement(m)')
    ax.set_ylabel('Vertical Displacement(m)')


    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x = 6e6 * np.outer(np.cos(u), np.sin(v))
    y = 6e6* np.outer(np.sin(u), np.sin(v))
    z = 6e6 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='blue')
    ax.set_xlim3d(-1.2e8, 0.6e8)
    ax.set_ylim3d(-1.2e8, 0.6e8)
    ax.set_zlim3d(-1.2e8, 0.6e8)
    
    plt.show()




def slingshot():
    """
    This function handles plotting the orbital trajectory of the rocket for the Earth-Moon scenario as described in the notes.
    """
    numpoints = 647075
    x = np.zeros(numpoints)
    y = np.zeros(numpoints)
    vx = np.zeros(numpoints)
    vy = np.zeros(numpoints)
    Kinetic = np.zeros(numpoints)
    Potential = np.zeros(numpoints)
    Total = np.zeros(numpoints)
    t = np.zeros(numpoints)

    x[0] = 0 #initial conditions
    y[0] = -6800e3 #picked without any significance
    vx[0] = 10729.6 #found by increasing from 10000
    vy[0] = 0
    


    for i in range(0, numpoints - 1):
        x[i+1], y[i+1], vx[i+1], vy[i+1], t[i+1] = RungeKuttaMoon(x[i], y[i], vx[i], vy[i], t[i])
        Kinetic[i], Potential[i], Total[i] = Energy(x[i], y[i], vx[i], vy[i], 'Two')
    fig, ax = plt.subplots()
    ax.plot(x, y, color = 'black', linewidth = 1)
    ax.axis('equal')
    ax.set_xlabel('Horizontal Displacement (m)')
    ax.set_ylabel('Vertical Displacement (m)')
    ax.add_patch(plt.Circle((0, 0), Earth.Radius, color='blue', label='Earth'))
    ax.add_patch(plt.Circle((0, 3.84e8), Moon.Radius, color='darkgray', label='Moon'))
    
    plt.show()

    plt.plot(t, Kinetic, label = 'Kinetic Energy')
    plt.plot(t, Potential, label = 'Gravitational Potential Energy')
    plt.plot(t, Total, label = 'Sum of Kinetic and Potential Energies')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy (J)')
    plt.legend()
    plt.show()



def slingshotfo8():
    """
    This function handles plotting the orbital trajectory of the rocket for the Earth-Moon scenario as described in the notes for the 'figure of 8' trajectory.

    """

    numpoints = 828671 #found by starting at 1000000 and reducing it to current number by finding the corresponding numpoint to the peak of the potential energy.
    x = np.zeros(numpoints)
    y = np.zeros(numpoints)
    vx = np.zeros(numpoints)
    vy = np.zeros(numpoints)
    Kinetic = np.zeros(numpoints)
    Potential = np.zeros(numpoints)
    Total = np.zeros(numpoints)
    t = np.zeros(numpoints)

    x[0] = 0
    y[0] = -7500e3 #chose a bigger starting position.
    vx[0] = 10191
    vy[0] = 0
    


    for i in range(0, numpoints - 1):
        x[i+1], y[i+1], vx[i+1], vy[i+1], t[i+1] = RungeKuttaMoon(x[i], y[i], vx[i], vy[i], t[i])
        Kinetic[i], Potential[i], Total[i] = Energy(x[i], y[i], vx[i], vy[i], 'Two')
    fig, ax = plt.subplots()
    ax.plot(x, y, color = 'black', linewidth = 1)
    ax.axis('equal')
    ax.set_xlabel('Horizontal Displacement (m)')
    ax.set_ylabel('Vertical Displacement (m)')
    ax.add_patch(plt.Circle((0, 0), Earth.Radius, color='blue', label='Earth'))
    ax.add_patch(plt.Circle((0, 3.84e8), Moon.Radius, color='darkgray', label='Moon'))
    ax.legend()
    
    plt.show()

    plt.plot(t, Kinetic, label = 'Kinetic Energy')
    plt.plot(t, Potential, label = 'Gravitational Potential Energy')
    plt.plot(t, Total, label = 'Sum of Kinetic and Potential Energies')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy (J)')
    plt.legend()
    plt.show()
    
    
    
    
Input = '0' #menu function as given in the notes, and as used in the last exercise
while Input != 'q':
    Input = input("Please choose from the following letters:\n\n"
                  "Circular orbit around earth - 'a'\n"
                  "Elliptical orbit around earth - 'b'\n"
                  "Two-Body slingshot orbit - 'c'\n"
                  "Two-Body figure of 8 orbit - 'd'\n"
                  "Quit the program - 'q': "
                  ) 

    if Input == "a":

        while True: #modification here to handle the option of having no 3-d plots to save time if need be. This is more significant for the two-body scenario
            try:
                threedimensional = input("Generate 3-D plots of the orbit?: (y/n): ")
                if threedimensional == "y" or threedimensional == "n":
                    break 
                else:
                    raise ValueError()
            except ValueError:
                print("Please only enter a 'y' or 'n'")
                continue
        if threedimensional == "y":
            print("Generating plots of the circular orbit...")
            circularorbit_2d()
            circularorbit_3d()
        elif threedimensional == "n":
            print("Generating 2-D plot of the circular orbit...")
            circularorbit_2d()


    elif Input =="b":
        ellipticalorbit2d()
        ellipticalorbit_3d()
    elif Input == "c":
        slingshot()
    elif Input == "d":
        slingshotfo8()

    elif Input == "q":
        print("Goodbye, have a nice day.")