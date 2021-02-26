"""
一图胜千言
动图胜万言
python 生成
gif, mp4
"""
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

# y = x ** 2
'''
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
'''

fig, ax = plt.subplots()
xdata = []
ydata = []

line, = plt.plot(xdata, ydata, 'r-')


def init():
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 30)
    return line,


def update(frame):  # 帧
    print(frame)
    xdata.append(frame)
    ydata.append(frame ** 2)

    line.set_data(xdata, ydata)
    return line,


ani = animation.FuncAnimation(
    fig=fig,
    func=update,
    # frames=[1, 2, 3],
    frames=np.linspace(0, 5, 100),
    # frames=5,
    init_func=init,
    interval=100,  # 时间间隔: 毫秒
    repeat=False
)
# plt.show()
ani.save('1.gif', writer='pillow')
# ani.save('1.mp4')
