import matplotlib.pyplot as plt
import numpy as np
import sympy as smp

# Def the function
def h(x,y): return np.sin((np.square(x)+np.square(y))/5)
    
# Make data to graph
X = np.arange(-8, 8, 0.2)
Y = np.arange(-8, 8, 0.2)
X, Y = np.meshgrid(X, Y)

# -Gradient Descent-
# We redefine the function to work with derivatives (symbolic, in this case)

x, y = smp.symbols ('x y', real=True)
f = smp.sin((x**2+y**2)/5)

# Define a starting point (SP)  
xSP = 3.0       #-IMPUT PARAMETER HERE-
ySP = 0.0      #-IMPUT PARAMETER HERE-

# Create a list to graph 
listGrad = [[xSP,ySP]]

# Set the number of steps, alpha and tolerance
steps = 100     #-IMPUT PARAMETER HERE-
alpha = 0.1      #-IMPUT PARAMETER HERE-
tolerance = 10e-06 #-IMPUT PARAMETER HERE-

steps_taken = 0
progress = 1


# Loop tracking progress
while (progress > tolerance) and (steps_taken < steps): 
    steps_taken = steps_taken + 1  # Count steps
    
    # Calculate derivatives
    dFx= f.diff(x)
    dFy= f.diff(y)

    # Evaluate derivatives in SP
    subs_dFx = dFx.subs(x, xSP).subs(y, ySP)
    subs_dFy = dFy.subs(x, xSP).subs(y, ySP)
    
    # Replace old SP with new SP
    xSP = xSP - alpha * subs_dFx
    ySP = ySP - alpha * subs_dFy
    
    # Add SP to a list
    listGrad.append([xSP,ySP])
    
print(listGrad) #To ferify

#Graph Gradient Descend
x_graph_grad, y_graph_grad = zip(*listGrad)
plt.plot(x_graph_grad,y_graph_grad, 'o', label="Puntos")
plt.xlabel('x')
plt.ylabel('y')
plt.plot(*zip(*listGrad), label='Recta')
plt.grid()
plt.legend()
plt.show()

# plt.scatter(*zip(*listGrad))
 
    
# -Graph h(x, y)-

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
# Plot the surface.
surf = ax.plot_surface(X, Y, h(X,Y), cmap='viridis')

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