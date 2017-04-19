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

fig = plt.figure(1, figsize=[7,2.5])

axes=plt.gca()

line1 = axes.plot(p2,m2,'b^-',label='New Traffic')
line2 = axes.plot(p2,np.ones(28),'bo-', label='Available off-chip bandwidth')

axes.set_xticks(np.arange(15)*2)
axes.set_yticks(np.arange(11))
axes.set_xlabel('Number of Cores',fontsize=8)
axes.set_ylabel('Normallizated traffic',fontsize=8)
axes.yaxis.grid(True)
axes.legend(loc='best', fontsize=8)

axes.annotate('BW Limited Scaling', xy=(11, 1),
            xytext=(11,5), fontsize=8,
            arrowprops=dict(facecolor='black',alpha=0.5),
            horizontalalignment='right', verticalalignment='top')
axes.annotate('Ideal Scaling', xy=(16, 2),
            xytext=(16,6), fontsize=8,
            arrowprops=dict(facecolor='black',alpha=0.5),
            horizontalalignment='right', verticalalignment='top')


plt.show()
