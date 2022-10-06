from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import sympy as smp
from sympy.utilities.lambdify import lambdify
from sympy import symbols, diff, Symbol
from sympy.solvers import solve

# Def the function
def h(x,y): 
    return np.sin((np.square(x)+np.square(y))/5)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


# Make data
X = np.arange(-8, 8, 0.2)
Y = np.arange(-8, 8, 0.2)
X, Y = np.meshgrid(X, Y)

# -Gradient Descent-
# We redefine the function to work with derivatives (symbolic, in this case)

x, y = smp.symbols ('x y', real=True)
f = smp.sin((x**2+y**2)/5)

# Define a starting point (SP)  -IMPUT PARAMETER HERE--IMPUT PARAMETER HERE-
xSP = np.array([3,0])

# Function of gradient, calculate derivatives
def g(xSP, f):
    dfdx = smp.diff(f, x)
    dfdy = smp.diff(f, y)
    return np.array([lambdify(x, dfdx)(xSP[0]), lambdify(y, dfdy)(xSP[1])]) 
    # What we did is generate the gradient and evaluate in xSP
    
# Generate a loop. We are using steps and a algorithm

# Set the number os steps -IMPUT PARAMETER HERE--IMPUT PARAMETER HERE-
steps = 3 

# Automatic algorithm to track progress and stop if necessary

# Get a float value evaluating the function in the SP
progress = [float(smp.sin((xSP[0]**2+xSP[1]**2)/5)) ]
print(float(smp.sin((xSP[0]**2+xSP[1]**2)/5)))

# Loop tracking progress, 0.00001 is the tolerance
# We add a fraction of the negative gradient to travel
while np.sqrt(float(g(xSP,f)[0]**2) + float(g(xSP,f)[1]**2)) > 0.00001 and steps>0:
    steps -= steps  # Count steps
    s = -g(xSP, f) # Negative of gradient is where we go!
    a = Symbol('a')
    a = 0.5  # How much we move -IMPUT PARAMETER HERE--IMPUT PARAMETER HERE-
    
    xSP = xSP + a*s # Update SP
    progress.append(float(smp.sin((xSP[0]**2+xSP[1]**2)/5))) # We evaluate to keep track
    print(float(smp.sin((xSP[0]**2+xSP[1]**2)/5)))




# -Graph h(x, y)-
# Plot the surface.
surf = ax.plot_surface(X, Y, h(X,Y), cmap=cm.coolwarm)

# Set limits 
ax.set_xlim3d(-8, 8)
ax.set_ylim3d(-8, 8)
ax.set_zlim3d(-8, 8)

#Set labels
ax.set_title('3D Surface plot of g(x,y)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add a color bar which maps values to colors.
fig.colorbar(surf,shrink=0.5)

plt.show()         
