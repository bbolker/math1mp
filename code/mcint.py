import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import numpy as np
import numpy.random as npr

c = ((2,2.5),(4,3),(1,2))
r = (1.5,3,2)
cc = ('red','blue','green')
def plot_circles(ctrs,radii,cols,alpha):
    """plot circles with specified centres, colours, etc."""
    for c,r,cc in zip(ctrs,radii,cols):
        ax1.add_patch(mpatches.Circle(xy=c,radius=r,color=cc,alpha=alpha))
    return(None)
	
fig, ax1 = plt.subplots(figsize=(4,4))
ax1.set_xlim(0,10)
ax1.set_ylim(0,10)
plot_circles(c,r,cc,0.2)


npr.seed(101)
x = npr.uniform(c[0][0]-r[0],c[0][0]+r[0],size=1e6)
y = npr.uniform(c[0][1]-r[0],c[0][1]+r[0],size=1e6)
tests = np.tile(True,1e6)
def incirc(x,y,ctr,radius):
    """determine whether (x,y) point is within a specified circle"""
    dsq = (x-ctr[0])**2+(y-ctr[1])**2
    return(dsq<radius**2)

for (c0,r0) in zip(c,r):
    tests = tests & incirc(x,y,c0,r0)
    print(np.mean(tests))

fig, ax1 = plt.subplots(figsize=(4,4))
ax1.set_xlim(-2,8)
ax1.set_ylim(-2,8)
plot_circles(c,r,cc,0.2)
ax1.add_patch(mpatches.Rectangle(xy=(c[0][0]-r[0],c[0][1]-r[0]),width=2*r[0],height=2*r[0],fill=False,ec='black'))

ax1.scatter(x[tests],y[tests],marker=".",edgecolors="none",alpha=0.1)
fig.savefig("pix/mc1.png")
r[0]**2*np.mean(tests)
