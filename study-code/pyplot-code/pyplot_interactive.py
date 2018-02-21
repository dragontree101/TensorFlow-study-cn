#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

import matplotlib.pyplot as plt
import numpy as np

x_axis_points = np.linspace(-1, 1, 100)
y_axis_points = np.ones(100)

plt.figure(1, figsize=(8, 6))
plt.xlim(-1, 1)
plt.ylim(-1, 1)

# 显示网格坐标
plt.grid()

line, = plt.plot(x_axis_points, y_axis_points, color='red')

# 开启交互试
plt.ion()

for i in np.linspace(-1, 1, 100):
    line.set_ydata(y_axis_points * i)
    plt.draw()

    # 间隔时间为0.1秒
    plt.pause(0.03)

# 关闭交互试
plt.ioff()

# 展示最终的图片
plt.show()
