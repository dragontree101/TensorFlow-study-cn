#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

import matplotlib.pyplot as plt
import numpy as np

x_axis_points = np.linspace(-5, 5, 100)
sin_y_axis_points = np.sin(x_axis_points)
cos_y_axis_points = np.cos(x_axis_points)

# 设置图的大小
plt.figure(1, figsize=(8, 6))

# 一个图片做成 1行2列的图片， 第1张图片
plt.subplot(121)

# scatter是通过点进行绘制
# 前面是x轴和y轴, color是点的颜色, label是对应的标签
plt.scatter(x_axis_points, sin_y_axis_points, color='red', label='sin')
plt.scatter(x_axis_points, cos_y_axis_points, color='green', label='cos')

# x轴的范围 (-5, 5)
plt.xlim((-5, 5))
# y轴的范围 (-1, 1)
plt.ylim((-1, 1))
# 用最合适的方式显示图例
plt.legend(loc='best')

# 一个图片做成 1行2列的图片， 第2张图片
plt.subplot(122)

# plot是通过线进行绘制
# 前面是x轴和y轴, color是点的颜色, linewidth是线宽度, label是对应的标签
plt.plot(x_axis_points, sin_y_axis_points, color='blue', linewidth='1.0', label='sin')
plt.plot(x_axis_points, cos_y_axis_points, color='black', linewidth='3.0', label='cos')

plt.xlim((-5, 5))
plt.ylim((-1, 1))
plt.legend(loc='best')

plt.show()
