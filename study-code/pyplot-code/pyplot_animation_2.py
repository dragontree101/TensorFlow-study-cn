#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

####### 另外一种动图的写法
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)
line = ax.plot(x, y)
dot, = ax.plot([], [], 'ro')


def init_dot():
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1, 1)
    return line


def gen_dot():
    for i in np.linspace(0, 2 * np.pi, 200):
        new_dot = [i, np.sin(i)]
        yield new_dot


def update_dot(new_dot):
    dot.set_data(new_dot[0], new_dot[1])
    return dot,


ani = FuncAnimation(fig, update_dot, frames=gen_dot, interval=50, init_func=init_dot)

plt.show()
