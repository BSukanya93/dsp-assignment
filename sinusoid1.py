import numpy as np
from matplotlib import pyplot as plt
n=np.arange(0,500)
F1=250
Fs1=10000
s1=0.5*np.cos(2*np.pi*F1/Fs1*n+np.pi/2)
s2=1*np.cos(2*np.pi*F1/Fs1*n+np.pi/2)
s=s1+s2
plt.subplot(3,1,1)
plt.stem(n,s);

F2=20
Fs2=2000
s3=0.5*np.cos(2*np.pi*F1/Fs1*n+np.pi/2)
s4=0.5*np.cos(2*np.pi*F2/Fs2*n+np.pi/2)
a=s3+s4
plt.subplot(3,1,2)
plt.stem(n,a);

s5=0.5*np.cos(2*np.pi*F1/Fs1*n+np.pi/2)
s6=0.5*np.cos(2*np.pi*F1/Fs1*n+np.pi/4)
b=s5+s6
plt.subplot(3,1,3)
plt.stem(n,b);
plt.show()

