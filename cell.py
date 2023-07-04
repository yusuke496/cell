import numpy as np
import matplotlib.pyplot as plt

n=50
mx=21
my=21
theta=0
d=100
x0=0
x0d=0
y0=0
y0d=0
rx=133.108
ry=133.108
ti=0
N=50

dd=np.matrix([[1,d,0,0],[0,1,0,0],[0,0,1,d],[0,0,0,1]])
r=np.matrix([[1,0,0,0],[-2/rx,1,0,0],[0,0,1,0],[0,0,-2/ry,1]])
t=np.matrix([[np.cos(ti),0,np.sin(ti),0],[0,np.cos(ti),0,np.sin(ti)],[-np.sin(ti),0,np.cos(ti),0],[0,-np.sin(ti),0,np.cos(ti)]])
z0=np.matrix([[x0],[x0d],[y0],[y0d]])
rr=np.linalg.inv(t)@r@t
c=rr@dd@rr@dd
zn=c**N
zn=zn@z0
print(zn)