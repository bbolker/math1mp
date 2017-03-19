## ----logist1-------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
## parameters
r=1
K=4
## time info
dt=0.1
t_tot=15
t_vec = np.arange(0,t_tot,step=dt)
x = np.zeros(len(t_vec))
x[0]=0.1  ## initial conditions
for i in range(1,len(t_vec)):
   g = r*x[i-1]*(1-x[i-1]/K)
   x[i] = x[i-1]+g*dt
fig, ax = plt.subplots()
ax.plot(t_vec,x)
fig.savefig("pix/logist1.png")

## ----logist2-------------------------------------------------------------
def logist_grad(x,t,params):
   r,K = params  ## unpack parameters
   return(r*x*(1-x/K))

## now run the loop
for i in range(1,len(t_vec)):
    x[i] = x[i-1]+logist_grad(t_vec[i-1],x[i-1],params=(1,4))*dt

## ----logist3-------------------------------------------------------------
def euler_solve(t_vec,x0,gradfun,params):
   """solve differential equation by Euler's method"""
   x = np.zeros(len(t_vec))
   dt = t_vec[1]-t_vec[0] ## assume evenly spaced ...
   x[0] = x0
   for i in range(1,len(t_vec)):
      x[i] = x[i-1]+gradfun(x[i-1],t_vec[i-1],params=params)*dt
   return(x)

logist_sol = euler_solve(t_vec,x0=0.1,gradfun=logist_grad,params=(1,4))


## ----logist4-------------------------------------------------------------
def theta_logist_grad(x,t,params):
   r,K,theta = params
   return(r*x*(1-x/K)**theta)

tlogist_sol1 = euler_solve(t_vec,x0=0.1,gradfun=theta_logist_grad,params=(1,4,2))
## need to make the step length smaller for this one ...
t_vec2 = np.arange(0,t_tot,step=0.001)
tlogist_sol2 = euler_solve(t_vec2,x0=0.1,gradfun=theta_logist_grad,params=(1,4,0.8))

ax.plot(t_vec,tlogist_sol1)
ax.plot(t_vec2,tlogist_sol2)
fig.savefig("pix/logist2.png")

## ----euler_msolve--------------------------------------------------------
def euler_msolve(t_vec,x0,gradfun,params):
   """solve differential equation by Euler's method"""
   x = np.zeros((len(t_vec),len(x0)))
   dt = t_vec[1]-t_vec[0] ## assume evenly spaced ...
   x[0,:] = x0
   for i in range(1,len(t_vec)):
      x[i,:] = x[i-1,:]+gradfun(x[i-1,:],t_vec[i-1],params=params)*dt
   return(x)

## ----SIR_grad------------------------------------------------------------
def SIR_grad(x,t,params):
   beta,gamma = params
   S,I,R = x
   return(np.array([-beta*S*I, beta*S*I-gamma*I, gamma*I]))

## ----SIR_sol1------------------------------------------------------------
SIR_sol1 = euler_msolve(t_vec,x0=(0.99,0.01,0),
                        gradfun=SIR_grad,params=(2,1))

## ----SIR_plot1-----------------------------------------------------------
fig, ax = plt.subplots()
ax.plot(t_vec,SIR_sol1)
ax.legend(("S","I","R"))
fig.savefig("pix/SIR1.png")


## ----scipy---------------------------------------------------------------
import scipy.integrate
SIR_sol2 = scipy.integrate.odeint(SIR_grad,
                       y0=(0.99,0.01,0),
                       t=t_vec,
                       args=((2,1),))

