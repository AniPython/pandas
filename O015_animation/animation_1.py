"""
一图胜千言
动图胜万言
.gif, mp4
"""
import matplotlib.pyplot as plt
from matplotlib import animation

# y = x ** 2

fig, ax = plt.subplots()
ax.set_xlim(0, 5)
ax.set_ylim(0, 10)

line, = plt.plot([1], [1], 'ro')
plt.savefig('1.png')

line.set_data([1, 2], [1, 4])
plt.plot(line.get_xdata(), line.get_ydata(), 'ro')
plt.savefig('2.png')

line.set_data([1, 2, 3], [1, 4, 9])
plt.plot(line.get_xdata(), line.get_ydata(), 'ro')
plt.savefig('3.png')

