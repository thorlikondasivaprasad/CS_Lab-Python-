import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([10,20,30,40,50])
n=len(x)
s_x=sum(x)
s_y=sum(y)
xy=x*y
s_xy=sum(xy)
xx=x*x
s_xx=sum(xx)
ss_x=s_x*s_x
m=((n*s_xy)-(s_x*s_y))/((n*s_xx)-(ss_x))
print(m)
c=((s_y)-(m*(s_x)))/n
print(c)

y1=(m*x)+c
print(y1,end=" ")

#plot

plt.scatter(x,y,color="black")
plt.plot(x,y1,color="orange")
plt.xlabel("revenue")
plt.ylabel("profit")
plt.title("The revenue of RVRJC")
plt.show()


# r^2=1-(SSE/SST)

z=(y-y1)*(y-y1)
ss_e=sum(z)
ym=np.mean(y)
a=(y-ym)*(y-ym)
ss_t=np.var(a)
r=1-(ss_e/ss_t)
print(r)
if(r>0.99):
    print("Best Fit")
else:
    print("Not a best fit")
