#implementation of DTFT
import numpy as np
import cmath
from matplotlib import pyplot as plt
a=np.pi
w=np.arange(-a,a,0.01*a)
x=np.random.rand(500)
y=[]
for i in range(0,len(w)):
	s=0
	for n in range(0,len(x)):
		s=s+x[n]*np.exp(-1*1j*w[i]*n)
	y.append(s)
print(y)
plt.subplot(2,1,1)
plt.stem(w,np.abs(y));
plt.subplot(2,1,2)
plt.stem(w,np.angle(y));
plt.show()
