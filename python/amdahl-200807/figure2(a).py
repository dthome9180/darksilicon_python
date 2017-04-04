"""
Make the figuer 2(a) for Speedup of symmetric multicore
                                    1
SpeedupSymemetric(f,n,r)=----------------------
                           1-f           f*r
                         --------  +  ---------
                         perf(r)      perf(r)*n

Hill, M. D. and M. R. Marty. "Amdahl's Law in the Multicore Era." Computer 
41(7): 33-38.

"""
import numpy as np
import matplotlib.pyplot as plt
import math

def SpeedupSymmetric(f,n,r):
    s = 1.0/((1-f)/np.sqrt(r)+(f*r)/(np.sqrt(r)*n))
    return s
    
x = np.linspace(0, 16, num=16, endpoint=True)
#dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off

fig, ax = plt.subplots()
line1, = ax.plot(x, SpeedupSymmetric(0.999, 16, x), 'r', linewidth=4,
                 label='Symmetric, n=16')
#line1.set_dashes(dashes)

#line2, = ax.plot(x, -1 * np.sin(x), dashes=[30, 5, 10, 5],
#                 label='Dashes set proactively')

ax.legend(loc='higher right')
ax.set_xscale('log')

plt.show()