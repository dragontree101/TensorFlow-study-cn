#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 另外一种初始化的方式, 在plt.figure的基础上可以得到ax坐标轴
fig, ax = plt.subplots()

x_data, y_data = [], []
line, = ax.plot([], [], 'r-')


def init_line():
    # 同等于 fig.xlim
    ax.set_xlim(0, 2 * np.pi)
    # 同等于 fig.ylim
    ax.set_ylim(-1, 1)
    return line,


def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame))
    line.set_data(x_data, y_data)
    return line,


# blit决定是更新整张图的点(False)还是只更新变化的点(True)
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 128),
                    init_func=init_line, blit=True, interval=50)
plt.show()
