import pylab
import numpy as np
from random import *
pi=np.pi
n=1000
ts=np.linspace(0,12*pi,n)
xs=np.sin(ts)*(np.exp(np.cos(ts))-2*np.cos(4*ts)-np.sin(ts/12)**5)
ys=np.cos(ts)*(np.exp(np.cos(ts))-2*np.cos(4*ts)-np.sin(ts/12)**5)
m=5
ds=8
#pylab.axis("off")
for i in range(m):
    for j in range(m):
        a=2*pi
        #a=2*pi*random()
        sina=np.sin(a)
        cosa=np.cos(a)
        xs2=cosa*xs-sina*ys+i*ds
        ys2=sina*xs+cosa*ys+j*ds        
        cs=[random()for k in range(3)]
        pylab.fill(xs2,ys2,color=cs)
