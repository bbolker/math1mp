import numpy as np
import matplotlib.pyplot as plt

def sirgrad(t,y,params):
    beta, gamma = params
    s, i, r = tuple(y)
    infrate = beta*s*i
    return([-infrate,infrate-gamma*i,gamma*i])

def euler(tvec,y0,grad,params):
    nt = len(tvec)
    dt = tvec[1]-tvec[0]
    res = np.zeros((len(tvec),len(y0)))
    res[0,:] = y0
    for i in range(nt-1):
        res[i+1,:] = res[i,:] + np.array(sirgrad(tvec[i],res[i,:],params))*dt
    return(res)

params = (3,1)
tvec = np.linspace(0,20,201)
y0 = (0.99,0.01,0)
print(np.array(sirgrad(tvec[0],y0,params)))

res = euler(tvec,y0,sirgrad,params)
plt.plot(tvec,res[:,1])
plt.show()
