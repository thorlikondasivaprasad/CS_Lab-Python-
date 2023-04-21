import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
x=np.array([1,2,3,4,5])
y=np.array([20,30,40,60,70])
n=len(x)
mx=np.mean(x)
my=np.mean(y)
xy=x*y
s_xy=sum(xy)
pro=mx*my
c_xy=(s_xy/n)-pro
xx=x*x
s_x=sum(xx)
sig_x=((s_x/n)-(mx**2))**(1/2)
print(sig_x)
yy=y*y
s_y=sum(yy)
sig_y=((s_y/n)-(my**2))**(1/2)
print(sig_y)
print(c_xy)

r=(c_xy)/(sig_x*sig_y)
print(r)
