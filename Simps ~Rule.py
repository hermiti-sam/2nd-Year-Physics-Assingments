#Using simpsons rule to perform numerical integration and demonstrate Fresnel diffraction from an aperture

import matplotlib.pyplot as plt
import numpy as np


def fresnelmenu():
    """ simple menu function to offer the user a choice on which part of the demonstration they'd like to see.
    """
    Input = '0'
    while Input != 'q':
        Input = input("Please choose from the following letters: "
                      " \n 1D Simpsons Intensity plot with varying z - 'a'\n"
                      " 1D Simpsons Intensity plot for near field effects - 'b' \n "
                      "1D Simpsons Intensity plot with varying wavelength, \u03BB - 'c' \n"
                      " 2D Simpsons Diffraction pattern (Square) - 'd' \n "
                      "2D Simpsons Diffraction pattern (Rectangle) - 'e' \n "
                      "2D Simpsons Diffraction pattern for the near field (Square) - 'f' \n"
                      "2D Simpsonds Diffraction pattern for the near field (Rectangle) -'g'\n"
                      "Quit the Program - 'q': ")
        if Input == "a":
            ampplot()
        if Input == "b":
           apertureplot(200)
           apertureplot(100)
           apertureplot(70)
            
        if Input == "c":
            diffwavelength()
        if Input == "d":
            diffsquare()
        if Input == 'e':
            diffrect()
        if Input == 'f':
            diffnearsquare()
        if Input == 'g':
            diffnearrect()
        if Input == 'q':
            print("Goodbye, have a nice day")
            
        else:
            print("Please enter the letters shown :).")
            
        


            

#############################################################################    
def Simpson1D(x1, x2, z, x, N, lam):
    """function for performing numerical integration in the 1D case shown in
    pdf, it performs the integral via simpsons rule, and then squares the
    modulus of the result to show intensity"""
    Odds = 0
    Evens = 0 ### initialising variables 
    
    k = (2*np.pi) / (lam)
    C = (k * (1j)) / (2*z)  #defining our integral constants
    F_upper = np.exp(C * (x - x2)**2)
    F_lower = np.exp(C * (x - x1)**2)
    h = (x2 - x1) / N
    Sum = F_upper + F_lower #f(a) and f(b) from simpsons def (upper and lower bounds)
    E0 = 1
    A = (k * E0) / (2 * np.pi * z)
    for i in range(N):
        if i % 2 == 0 :
            Evens += 2 * np.exp(C * (x -(x1 + i*h))**2)
        else:
            Odds += 4 * np.exp(C * (x - (x1 + i*h))**2)
     
    simp = (h/3) * (Sum + Odds + Evens)
    Intensity = abs(A * (simp))**2 
    return Intensity

def ampplot():
    """plotting function to plot intensity against screen coordinate. Same 
    method as for previous exercise> We just fill arrays with values from our
    function for intensity and will define our x values. This also shows plots
    for 3 values of z"""
    numpoints = 200
    x_low = -2e-3
    x_up = 2e-3
    dx = (x_up - x_low) / (numpoints - 1)
    yvals= np.zeros(numpoints)
    yvals1= np.zeros(numpoints)
    yvals2= np.zeros(numpoints)
    xvals = np.zeros(numpoints)
    lam = 1e-6
    for i in range(numpoints):
        xvals[i] = x_low + i*dx
        yvals[i] = Simpson1D(-1e-5, 1e-5, 0.02, xvals[i], 200, lam)
        yvals1[i] = Simpson1D(-1e-5, 1e-5, 0.01, xvals[i], 200, lam)
        yvals2[i] = Simpson1D(-1e-5, 1e-5, 0.005, xvals[i], 200, lam)
    
    plt.plot(xvals, yvals, label = "z = 0.02")
    plt.plot(xvals, yvals1, label = "z = 0.01")
    plt.plot(xvals, yvals2, label = "z = 0.005")
    plt.ylabel('Intensity')
    plt.xlabel('Screen Coordinate (m)')
    plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
    plt.legend(loc = "upper left")
    plt.show()



    
def apertureplot(N):
    numpoints =200
    x_low = -5e-4
    x_up = 5e-4
    dx = (x_up - x_low) / (numpoints - 1)
    yvals= np.zeros(numpoints)

    xvals = np.zeros(numpoints)
    lam = 1e-6
    for i in range(numpoints):
        xvals[i] = x_low + i*dx
        yvals[i] = Simpson1D(-1e-4, 1e-4, 1.4e-3, xvals[i],N, lam)
        
    plt.plot(xvals, yvals, label = {"N=", N})
    
    
    plt.ylabel('Intensity')
    plt.xlabel('Screen Coordinate (m)')
    plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
    plt.legend(loc = 'upper right')
    
    plt.show()

   
def diffwavelength():
    numpoints = 200
    x_low = -2e-3
    x_up = 2e-3
    dx = (x_up - x_low) / (numpoints - 1)
    yvals= np.zeros(numpoints)
    yvals1= np.zeros(numpoints)
    yvals2= np.zeros(numpoints)
    xvals = np.zeros(numpoints)
    lam1 = 1e-6
    lam2 = 1e-5
    lam3 = 0.5e-6
    for i in range(numpoints):
        xvals[i] = x_low + i*dx
        yvals[i] = Simpson1D(-1e-5, 1e-5, 0.02, xvals[i], 100, lam1)
        yvals1[i] = Simpson1D(-1e-5, 1e-5, 0.02, xvals[i], 100, lam2)
        yvals2[i] = Simpson1D(-1e-5, 1e-5, 0.02, xvals[i], 100, lam3)
    
    plt.plot(xvals, yvals, label = "\u03BB = 1\u03BCm")
    plt.plot(xvals, yvals1, label = "\u03BB = 10\u03BCm")
    plt.plot(xvals, yvals2, label = "\u03BB = 0.5\u03BCm")
    plt.ylabel('Intensity')
    plt.xlabel('Screen Coordinate (m)')
    plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
    plt.legend(loc = "upper left")
    plt.show()
        
############################################################################
def xsimp(x1, x2, z, x, N):
    Odd = 0
    Even = 0 ### initialising variables 
    k = (2*np.pi) / (1e-6)
    C = (k * (1j)) / (2*z)  #defining our integral constants
    bigboi = np.exp(C * (x - x2)**2)
    smallboi = np.exp(C * (x - x1)**2)
    h = (x2 - x1) / N
    ends = bigboi + smallboi #f(a) and f(b) from simpsons def (upper and lower bounds)
    E0 = 1
    A = (k * E0) / (2 * np.pi * z)
    for i in range(N-1):
        if i % 2 == 0 :
            Even += 2 * np.exp(C * (x - (x1 + i*h))**2)
        else:
            Odd += 4 * np.exp(C * (x - (x1 + i*h))**2)
        i+=1
    middle = Even + Odd
    simp = ((h/3) * (ends + middle))
    bye = A * simp
    return bye
   
def ysimp(y_1, y_2, z, y, N):
    Odd = 0
    Even = 0
    k = (2*np.pi) / (1e-6)
    C = (k * (1j)) / (2*z) 
    bigboi = np.exp(C * (y - y_2)**2)
    smallboi = np.exp(C * (y - y_1)**2)
    h_y = (y_2 - y_1) / N
    ends = bigboi + smallboi
    for i in range(N-1): 
        if i % 2 ==0:
            Even += 2 * np.exp(C * (y - (y_1 + i*h_y))**2)
        else:
            Odd += 4 * np.exp(C * (y - (y_1 + i*h_y))**2 )
        i+=1
    middle = (Odd + Even)
    ysimp = ((h_y/3) * ((ends + middle)))
    return ysimp


def diffrect():
    numpoints = 100
    y_low = -10e-3
    x_low = -10e-3
    x_up = 10e-3
    z = 2
    N = 100
    I = np.zeros((numpoints, numpoints))
    dx = (x_up - x_low) / (numpoints - 1)
    for i in range(numpoints):
        x = x_low + i*dx
        for j in range (numpoints):
            y = y_low + j*dx
            I[i,j] = abs(xsimp(-1e-3, 1e-3, z, x, N) * ysimp(-0.5e-3, 0.5e-3, z, y, N) )
    plt.imshow(I, cmap = 'inferno')
    plt.axis('off')
    plt.title('Far Field Rectangular Pattern, z=2m, N=100')
    plt.show()

def diffsquare():
    numpoints = 100
    y_low = -5e-3
    x_low = -5e-3
    x_up = 5e-3
    
    z = 2
    N = 100
    I = np.zeros((numpoints, numpoints))
    dx = abs(x_up - x_low) / (numpoints - 1)
    for i in range(numpoints):
        x = x_low + i*dx
        for j in range (numpoints):
            y = y_low + j*dx
            I[i,j] = abs(xsimp(-1e-3,1e-3, z, x, N) * ysimp(-1e-3,1e-3, z, y, N) )
            
    plt.imshow(I, cmap = 'inferno',  )
    plt.axis('off')
    plt.title('Far Field Square Pattern, z=2m, N=100')
    plt.show()
    
def diffnearsquare():
    numpoints = 100
    y_low = -5e-3
    x_low = -5e-3
    x_up = 5e-3
    
    z=0.1
    N=100
    I = np.zeros((numpoints, numpoints))
    dx = abs(x_up - x_low) / (numpoints - 1)
    for i in range(numpoints):
        x = x_low + i*dx
        for j in range (numpoints):
            y = y_low + j*dx
            I[i,j] = abs(xsimp(-1e-3,1e-3, z, x, N) * ysimp(-1e-3,1e-3, z, y, N) )
            
    plt.imshow(I, cmap = 'inferno',  )
    plt.axis('off')
    plt.title('Near Field Pattern, z=0.1m, N = 100')
    plt.show()
    
    
def diffnearrect():
    numpoints = 100
    y_low = -5e-3
    x_low = -5e-3
    x_up = 5e-3
    
    z=0.1
    N=40
    
    I = np.zeros((numpoints, numpoints))
    dx = (x_up - x_low) / (numpoints - 1)
    for i in range(numpoints):
        x = x_low + i*dx
        for j in range (numpoints):
            y = y_low + j*dx
            I[i,j] = abs(xsimp(-1e-3, 1e-3, z, x, N) * ysimp(-0.5e-3, 0.5e-3, z, y, N) )
    plt.imshow(I, cmap = 'inferno')
    plt.axis('off')
    plt.title('Near Field Pattern, z=0.1m, N = 100')
    
    plt.show()
fresnelmenu()
