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

# scaling factor n2 = n1*(2^s)
s=4
# scaling bandwidth 10% every generation.
bs=0.1

n2=n1*(2**s)
p2=np.linspace(1, n2/2, num=n2/2, endpoint=True)
c2=n2-p2
s2=c2/p2

m2=MissRate(p2,p1,s2,s1,m1,a)

fig = plt.figure(1, figsize=[7,4])

axes=plt.gca()

line1 = axes.plot(p2,m2,'b^-',label='New Traffic')
line2 = axes.plot(p2,np.ones(n2/2)*((bs+1)**s),'bo-', label='Available off-chip bandwidth')

#axes.set_xticks(np.arange(n2/2)*2)
#axes.set_xlabel('Number of Cores',fontsize=8)
#axes.set_ylabel('Normallizated traffic',fontsize=8)
#axes.yaxis.grid(True)
#axes.legend(loc='upper left', fontsize=8)

plt.show()
