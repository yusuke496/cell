import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from lmfit import Model
from scipy import optimize
import math

def zn(x0,x0d,y0,y0d):
    dd=np.matrix([[1,d,0,0],[0,1,0,0],[0,0,1,d],[0,0,0,1]])
    r=np.matrix([[1,0,0,0],[-2/rx,1,0,0],[0,0,1,0],[0,0,-2/ry,1]])
    t=np.matrix([[np.cos(ti),0,np.sin(ti),0],[0,np.cos(ti),0,np.sin(ti)],[-np.sin(ti),0,np.cos(ti),0],[0,-np.sin(ti),0,np.cos(ti)]])
    z0=np.matrix([[x0],[x0d],[y0],[y0d]])
    rr=np.linalg.inv(t)@r@t
    c=rr@dd@rr@dd
    zn=c**N
    zn=zn@z0
    return zn

N=100
mx=77
my=81
d=100
x0=0
x0d=10
y0=0
y0d=10
rx=114.3293
ry=158.259
ti=0#math.pi/4

print(zn(x0,x0d,y0,y0d))
#scipy.optimize.minimize_scalar(float(zn(x0d)[0]**2+zn(x0d)[2]**2)
print(float(zn(x0,x0d,y0,y0d)[0]**2+zn(x0,x0d,y0,y0d)[2]**2))
