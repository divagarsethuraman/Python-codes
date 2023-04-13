####################################
## Graph ploting of Real function ##
####################################

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
# Define the function:
def f(x):
    y = np.sin(x)     # You can modify as per your wish
    return y

# Creating empty space to store data values
x1=[]
y1=[]

# Defining the initial and final values of the graph
xi=int(input("Enter the initial x value of graph"))
xf=int(input("Enter the final x value of graph"))
s=xf-xi
d=float(input("Specify the difference between two x points"))
x=np.arange(xi,xf,d)

# Fetching the values for graph plotting
for n in x:
    x1.append(n)
for i in range(len(x1)):
    y1.append(f(x[i]))
    if s*abs(s)<0:
       x1[i]-=d
    if s*abs(s)>0:
       x1[i]+=d

# print operation of values
print("The x values are ",x1)
print("The f(x) values are",y1)

# Graph plotting operation
fig,ax=plt.subplots()
ax.spines["bottom"].set_position("zero")
ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.plot(x1,y1,marker="o")
plt.title("~Graph of a function~")
plt.xlabel("x values")
plt.ylabel("Function of x values")
plt.show()
