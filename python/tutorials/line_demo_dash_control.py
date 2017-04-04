"""
Demo of a simple plot with a custom dashed line.

a line object's ''set-dashes'' method allows you to specify dashes with
a series of on/off lengths (in points).
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
dashes1 = [10, 5, 100, 5] # 10 points on , 5 points off, 100 on, 5 off
dashes2 = [30, 5, 10, 5]

fig, ax = plt.subplots()
line1, = ax.plot(x, np.sin(x), '--', linewidth=2,
                 label='Dashes set retroactively')
line1.set_dashes(dashes1)

line2, = ax.plot(x, -1 * np.sin(x), dashes=[30, 5, 10, 5],
                 label='Dashes set proactively')
#line2.set_dashes(dashes2) 
                
ax.legend(loc='lower right')
plt.show()