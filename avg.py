#moving average system
import numpy as np
from matplotlib import pyplot as plt
m=int(input("enter the order of the system"))
b=np.arange(0,500)
x=1*np.cos(2*np.pi*250/10000*b)
a=len(x)
y=np.zeros(len(x))
for n in range(0,len(x)):
	s=0
	for k in range(0,m):
		if n-k>=0:
			s=s+x[n-k]
	y[n]=s/m
print(x)
print(y)
plt.subplot(2,1,1)
plt.stem(b,x);
plt.subplot(2,1,2)
plt.stem(b,y);
plt.show()		


