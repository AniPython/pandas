"""
一图胜千言
动图胜万言
python 生成
gif, mp4
"""
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

fig, ax = plt.subplots()

# 固定的线
plt.plot([1, 2], [10, 20], 'b-')

# 线1
xdata = []
ydata = []
line, = plt.plot(xdata, ydata, 'r-')
# 线2
xdata2 = []
ydata2 = []
line2, = plt.plot(xdata2, ydata2, 'g-')

# 文字
x_template = 'x = %.2f'
x_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 30)
    return line, line2, x_text


def update(frame, n):  # 帧
    print(frame)
    # 线1
    xdata.append(frame)
    ydata.append(frame ** 2)
    line.set_data(xdata, ydata)
    # 线2
    xdata2.append(frame)
    ydata2.append(frame ** n)
    line2.set_data(xdata2, ydata2)

    # 文字
    x_text.set_text(x_template % frame)
    return line, line2, x_text


ani = animation.FuncAnimation(
    fig=fig,
    func=update,
    # frames=[1, 2, 3],
    frames=np.linspace(0, 5, 100),
    # frames=5,
    init_func=init,
    interval=100,  # 时间间隔: 毫秒
    repeat=False,
    blit=True,
    fargs=(4,)
)
plt.show()
# ani.save('1.gif', writer='pillow')
# ani.save('1.mp4')
