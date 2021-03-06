# -*- coding: utf-8 -*-
"""
Make the figuer 2 for Speedup of symmetric/asymmetric/dynamic multicores
                                   1
SpeedupSymemetric(f,n,r)=----------------------
                           1-f           f*r
                         --------  +  ---------
                         perf(r)      perf(r)*n

                                    1
SpeedupAsymemetric(f,n,r)=------------------------
                             1-f           f
                          --------  +  -----------
                           perf(r)     perf(r)+n-r

                                1
SpeedupDynamic(f,n,r)=----------------
                        1-f         f
                      --------  +  ---
                       perf(r)      n
                       
Hill, M. D. and M. R. Marty. "Amdahl's Law in the Multicore Era." Computer 
41(7): 33-38.

"""
import numpy as np
import matplotlib.pyplot as plt

def SpeedupSymmetric(f,n,r):
    s = 1.0/(((1-f)/Perf(r))+(f/(Perf(r)*(n/r))))
    return s
    
def SpeedupAsymmetric(f,n,r):
    s = 1.0/(((1-f)/Perf(r))+f/(Perf(r)+n-r))
    return s
    
def SpeedupDynamic(f,n,r):
    s = 1.0/(((1-f)/Perf(r))+f/n)
    return s

def Perf(r):
    return np.sqrt(r)
    

# parallel task ratio
f = [0.999, 0.99, 0.975, 0.9, 0.5]

fig, axs = plt.subplots(3,2)
fig.subplots_adjust(left=0.08,right=0.98,wspace=0.3,hspace=0.3)
fig.set_size_inches(8,9)

# rBCEs, the number of total BCEs
x = np.linspace(1, 16, num=16, endpoint=True)
#SpeedupSymmetric N=16
ax = axs[0,0]
line16f0, = ax.plot(x, SpeedupSymmetric(f[0], 16, x), color='red', 
                    linewidth=2.0,linestyle="-", label='f=0.999')
line16f1, = ax.plot(x, SpeedupSymmetric(f[1], 16, x), color='coral', 
                    linewidth=2.0,linestyle=":", label='f=0.99')
line16f2, = ax.plot(x, SpeedupSymmetric(f[2], 16, x), color='green', 
                    linewidth=2.0,linestyle="-.", label='f=0.975')
line16f3, = ax.plot(x, SpeedupSymmetric(f[3], 16, x), color='purple', 
                    linewidth=2.0,linestyle="--", label='f=0.9')
line16f4, = ax.plot(x, SpeedupSymmetric(f[4], 16, x), color='blue', 
                    linewidth=2.0,linestyle="-", label='f=0.5')

#ax.legend(loc='upper right',fontsize='small')
ax.set_xscale('log', basex=2)
ax.set_xlim(1, 16)
ax.set_ylim(2, 16)
ax.set_xticks([1,2,4,8,16])
ax.set_xticklabels(['0','2','4','8','16'],fontsize='small')
ax.set_yticks([2,4,6,8,10,12,14,16])
ax.set_yticklabels(['2','4','6','8','10','12','14','16'],fontsize='small')
ax.set_xlabel(r'$r$BCEs')
ax.set_ylabel(r'Speedup$_\mathrm{Symmetric}$')
fig.text(0.12,0.88,'Symmetric, n = 16',fontsize='small')
fig.text(0.01,0.64,'(a)')

# rBCEs, the number of total BCEs
x = np.linspace(1, 256, num=256, endpoint=True)
#SpeedupSymmetric N=256
ax = axs[0,1]
line256f0, = ax.plot(x, SpeedupSymmetric(f[0], 256, x), color='red', 
                    linewidth=2.0,linestyle="-", label='f=0.999')
line256f1, = ax.plot(x, SpeedupSymmetric(f[1], 256, x), color='coral', 
                    linewidth=2.0,linestyle=":", label='f=0.99')
line256f2, = ax.plot(x, SpeedupSymmetric(f[2], 256, x), color='green', 
                    linewidth=2.0,linestyle="-.", label='f=0.975')
line256f3, = ax.plot(x, SpeedupSymmetric(f[3], 256, x), color='purple', 
                    linewidth=2.0,linestyle="--", label='f=0.9')
line256f4, = ax.plot(x, SpeedupSymmetric(f[4], 256, x), color='blue', 
                    linewidth=2.0,linestyle="-", label='f=0.5')

ax.legend(loc='upper right', fontsize='small')
ax.set_xscale('log', basex=2)
ax.set_xlim(1, 256)
ax.set_ylim(2, 250)
ax.set_xticks([1,2,4,8,16,32,64,128,256])
ax.set_xticklabels(['0','2','4','8','16','32','64','128','256'],
                fontsize='small')
ax.set_yticks([50,100,150,200,250])
ax.set_yticklabels(['50','100','150','200','250'],fontsize='small')
ax.set_xlabel(r'$r$BCEs')
ax.set_ylabel(r'Speedup$_\mathrm{Symetric}$')
fig.text(0.60,0.88,'Symmetric, n=256',fontsize='small')
fig.text(0.51,0.64,'(b)')

# rBCEs, the number of total BCEs
x = np.linspace(1, 16, num=16, endpoint=True)
#SpeedupAsymmetric N=16
ax = axs[1,0]
aline16f0, = ax.plot(x, SpeedupAsymmetric(f[0], 16, x), color='red', 
                    linewidth=2.0,linestyle="-", label='f=0.999')
aline16f1, = ax.plot(x, SpeedupAsymmetric(f[1], 16, x), color='coral', 
                    linewidth=2.0,linestyle=":", label='f=0.99')
aline16f2, = ax.plot(x, SpeedupAsymmetric(f[2], 16, x), color='green',
                    linewidth=2.0,linestyle="-.", label='f=0.975')
aline16f3, = ax.plot(x, SpeedupAsymmetric(f[3], 16, x), color='purple', 
                    linewidth=2.0,linestyle="--", label='f=0.9')
aline16f4, = ax.plot(x, SpeedupAsymmetric(f[4], 16, x), color='blue', 
                    linewidth=2.0,linestyle="-", label='f=0.5')

#ax.legend(loc='upper right',fontsize='small')
ax.set_xscale('log', basex=2)
ax.set_xlim(1, 16)
ax.set_ylim(2, 16)
ax.set_xticks([1,2,4,8,16])
ax.set_xticklabels(['0','2','4','8','16'],fontsize='small')
ax.set_yticks([2,4,6,8,10,12,14,16])
ax.set_yticklabels(['2','4','6','8','10','12','14','16'],fontsize='small')
ax.set_xlabel(r'$r$BCEs')
ax.set_ylabel(r'Speedup$_\mathrm{Asymetric}$')
fig.text(0.24,0.59,'Asymmetric, n=16',fontsize='small')
fig.text(0.01,0.35,'(c)')

# rBCEs, the number of total BCEs
x = np.linspace(1, 256, num=256, endpoint=True)
#SpeedupAsymmetric N=256
ax = axs[1,1]
aline256f0, = ax.plot(x, SpeedupAsymmetric(f[0], 256, x), color='red', 
                    linewidth=2.0,linestyle="-", label='f=0.999')
aline256f1, = ax.plot(x, SpeedupAsymmetric(f[1], 256, x), color='coral', 
                    linewidth=2.0,linestyle=":", label='f=0.99')
aline256f2, = ax.plot(x, SpeedupAsymmetric(f[2], 256, x), color='green', 
                    linewidth=2.0,linestyle="-.", label='f=0.975')
aline256f3, = ax.plot(x, SpeedupAsymmetric(f[3], 256, x), color='purple', 
                    linewidth=2.0,linestyle="--", label='f=0.9')
aline256f4, = ax.plot(x, SpeedupAsymmetric(f[4], 256, x), color='blue', 
                    linewidth=2.0,linestyle="-", label='f=0.5')

#ax.legend(loc='upper right',fontsize='small')
ax.set_xscale('log', basex=2)
ax.set_xlim(1, 256)
ax.set_ylim(2, 250)
ax.set_xticks([1,2,4,8,16,32,64,128,256])
ax.set_xticklabels(['0','2','4','8','16','32','64','128','256']
                ,fontsize='small')
ax.set_yticks([50,100,150,200,250])
ax.set_yticklabels(['50','100','150','200','250'],fontsize='small')
ax.set_xlabel(r'$r$BCEs')
ax.set_ylabel(r'Speedup$_\mathrm{Asymetric}$')
fig.text(0.60,0.59,'Symmetric, n=256',fontsize='small')
fig.text(0.51,0.35,'(d)')

# rBCEs, the number of total BCEs
x = np.linspace(1, 16, num=16, endpoint=True)
#SpeedupDynamic N=16
ax = axs[2,0]
dline16f0, = ax.plot(x, SpeedupDynamic(f[0], 16, x), color='red', 
                    linewidth=2.0,linestyle="-", label='f=0.999')
dline16f1, = ax.plot(x, SpeedupDynamic(f[1], 16, x), color='coral', 
                    linewidth=2.0,linestyle=":", label='f=0.99')
dline16f2, = ax.plot(x, SpeedupDynamic(f[2], 16, x), color='green', 
                    linewidth=2.0,linestyle="-.", label='f=0.975')
dline16f3, = ax.plot(x, SpeedupDynamic(f[3], 16, x), color='purple', 
                    linewidth=2.0,linestyle="--", label='f=0.9')
dline16f4, = ax.plot(x, SpeedupDynamic(f[4], 16, x), color='blue', 
                    linewidth=2.0,linestyle="-", label='f=0.5')

#ax.legend(loc='upper right',fontsize='small')
ax.set_xscale('log', basex=2)
ax.set_xlim(1, 16)
ax.set_ylim(2, 16)
ax.set_xticks([1,2,4,8,16])
ax.set_xticklabels(['0','2','4','8','16'],fontsize='small')
ax.set_yticks([2,4,6,8,10,12,14,16])
ax.set_yticklabels(['2','4','6','8','10','12','14','16'],fontsize='small')
ax.set_xlabel(r'$r$BCEs')
ax.set_ylabel(r'Speedup$_\mathrm{Dynamic}$')
fig.text(0.09,0.30,'Symmetric, n=16',fontsize='small')
fig.text(0.01,0.06,'(e)')

# rBCEs, the number of total BCEs
x = np.linspace(1, 256, num=256, endpoint=True)
#SpeedupDynamic N=256
ax = axs[2,1]
dline256f0, = ax.plot(x, SpeedupDynamic(f[0], 256, x), color='red', 
                    linewidth=2.0,linestyle="-", label='f=0.999')
dline256f1, = ax.plot(x, SpeedupDynamic(f[1], 256, x), color='coral', 
                    linewidth=2.0,linestyle=":", label='f=0.99')
dline256f2, = ax.plot(x, SpeedupDynamic(f[2], 256, x), color='green', 
                    linewidth=2.0,linestyle="-.", label='f=0.975')
dline256f3, = ax.plot(x, SpeedupDynamic(f[3], 256, x), color='purple', 
                    linewidth=2.0,linestyle="--", label='f=0.9')
dline256f4, = ax.plot(x, SpeedupDynamic(f[4], 256, x), color='blue', 
                    linewidth=2.0,linestyle="-", label='f=0.5')

#ax.legend(loc='upper right',fontsize='small')
ax.set_xscale('log', basex=2)
ax.set_xlim(1, 256)
ax.set_ylim(2, 250)
ax.set_xticks([1,2,4,8,16,32,64,128,256])
ax.set_xticklabels(['0','2','4','8','16','32','64','128','256']
                ,fontsize='small')
ax.set_yticks([50,100,150,200,250])
ax.set_yticklabels(['50','100','150','200','250'],fontsize='small')
ax.set_xlabel(r'$r$BCEs')
ax.set_ylabel(r'Speedup$_\mathrm{Dynamic}$')
fig.text(0.60,0.30,'Symmetric, n=256',fontsize='small')
fig.text(0.51,0.06,'(c)')

fig.savefig('./figure2.png')
#plt.show()