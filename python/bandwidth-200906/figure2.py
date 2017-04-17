import matplotlib.pyplot as plt
import numpy as np

def MissRate(p2,p1,s2,s1,m1,a):
    m2=(p2/p1)*((s2/s1)**(-1*a))*m1
    return m2

a=0.5

n1=16
p1=8
c1=n1-p1
s1=c1/p1
m1=1

n2=32
p2=np.linspace(1, 28, num=28, endpoint=True)
c2=n2-p2
s2=c2/p2

m2=MissRate(p2,p1,s2,s1,m1,a)

fig, axes =plt.subplots()

line1 = axes.plot(p2,m2,'b^-',label='New Traffic')
line2 = axes.plot(p2,np.ones(28),'bo-', label='Available off-chip bandwidth')

axes.set_xticks(np.arange(15)*2)
axes.set_yticks(np.arange(11))
axes.set_xlabel('Number of Cores')
axes.set_ylabel('Normallizated traffic')
axes.yaxis.grid(True)
axes.legend()

plt.show()
