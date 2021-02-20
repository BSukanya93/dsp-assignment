#implementation of DTFT
import numpy as np
import cmath
from matplotlib import pyplot as plt
a=np.pi
w=np.arange(-a,a,0.01*a)
b=np.arange(0,500)
x=1*np.cos(2*np.pi*250/10000*b)
l=len(x)
N=l
y=[]
for k in range(0,l):
	s=0
	for n in range(0,len(x)):
		s=s+x[n]*np.exp(-1*1j*(2*a)*k/N*n)
	y.append(s)
print(y)
plt.subplot(2,1,1)
plt.stem(w,np.abs(y));
plt.subplot(2,1,2)
plt.stem(w,np.angle(y));
plt.show()
