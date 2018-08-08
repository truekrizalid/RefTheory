import numpy as np
from scipy.optimize import leastsq
Xi=np.array([8.19,2.72,6.39,8.71,4.7,2.66,3.78])
Yi=np.array([7.01,2.78,6.47,6.71,4.1,4.23,4.05])
#print Xi,'\n',Yi
def func(p,x):
    k,b = p
    return k*x + b

def error(p,x,y,s):
    print s
    return func(p,x)-y

p0=[2,10]

s="Test the number of iteration"
Para=leastsq(error,p0,args=(Xi,Yi,s))
k,b=Para[0]
print"k=",k,'\n',"b=",b

import matplotlib.pyplot as plt
plt.figure(figsize=(8,12))
plt.scatter(Xi,Yi,color="red",label="Sample Point",linewidth=3) #画样本点
x=np.linspace(0,10,1000)
y=k*x+b
plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2) #画拟合直线
plt.legend()
plt.show()
