import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

## (alpha,beta,delta,nu,r)
pars = (0.025,0.02,0.01,3,0.03)
phi_par = (0.04/(1-0.04**2),0.04**3/(1-0.04**2))
## lambda is a reserved word in Python ...
def phi(lam,phi0=phi_par[0],phi1=phi_par[1]):
    return(phi_par[1]/(1-lam)**2-phi0)
kappa_par = (-0.0065,np.exp(-5),20)
def kappa(x,kappa0=kappa_par[0],kappa1=kappa_par[1],kappa2=kappa_par[2]):
    return(kappa0+kappa1*np.exp(kappa2*x))

## eqs 
def keen_grad(y,t,pars):
   omega,lam,d = y
   alpha,beta,delta,nu,r = pars
   return(np.array([
          ## wage share
          omega*(phi(lam)-alpha),
		  ## employment
          lam*(kappa(1-omega-r*d)/nu - alpha - beta - delta),
		  ## debt
          d*(r-kappa(1-omega-r*d)/nu+delta)+kappa(1-omega-r*d)-(1-omega)]))

## try to recreate Figure 4 (stable equilibrium)
t_vec=np.arange(0,300,step=0.1)
keen_sol1 = scipy.integrate.odeint(keen_grad,
                y0 = (0.75,0.75,0.1),
				t=t_vec,
				args=(pars,))

fig, ax = plt.subplots()
ax.plot(t_vec,keen_sol1)
ax.legend(("wage share","employment","debt"))
fig.savefig("pix/keen1.png")






