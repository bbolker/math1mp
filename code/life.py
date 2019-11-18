## https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
def count_nbr(w,i,j):
    return np.sum(w[i-1:i+2,j-1:j+2])-w[i,j]

def life_show(w,ax):
    ax.imshow(w, interpolation="none")
    ax.axis("off")
    return None

def life_step(w,nw):
    size = w.shape[0]
    for i in range(size):
        for j in range(size):
            nbrs = count_nbr(w,i,j)
            if (w[i,j]==0 and nbrs==3) or (w[i,j]==1 and nbrs in (2,3)):
                nw[i,j]=1
            else:
                nw[i,j]=0
    return w, nw

def life_init(size=40,init_dens=0.2):
    world = np.zeros(shape=(size,size))
    ## initialize randomly
    n_init = round(init_dens*size**2)
    for i in range(n_init):
        world[npr.randint(size),npr.randint(size)] = 1
    return world

def do_step(plot=True):
    life_step(world,next_world)
    if plot:
        ax.imshow(world,interpolation="none")
    world, next_world = next_world, world
    return None

def life(size=40,init_dens=0.2,nt=100):
    fig, ax = plt.subplots()
    world = life_init(size,init_dens)
    next_world = world.copy()
    for t in range(nt):
        do_step()

if __name__=="__main__":
    npr.seed(101)
    from matplotlib.animation import FuncAnimation
    world = life_init()
    next_world = world.copy()
    fig, ax = plt.subplots()
    for i in range(20):
        do_step()
##    FuncAnimation(fig, do_step, frames=np.linspace(0, 2*np.pi, 128),
##                  blit = True)
