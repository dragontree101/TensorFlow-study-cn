#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

import numpy as np

a_array = np.arange(12).reshape(3, 4)
b_array = np.array([10, 10, 10, 10])

# 新增加一维，并且把之前的每个元素作为新的一维
c_array = b_array[:, np.newaxis]
print('c_array is \n', c_array, '\nc_array shape is ', c_array.shape, ', dim is ', c_array.ndim)

num = 100

# 矩阵每一行加上b_array
add_array_1 = a_array + b_array
print('add_array_1 is \n', add_array_1, '\nadd_array_1 shape is ', add_array_1.shape, ', dim is ', add_array_1.ndim)

# 矩阵每一行加上b_array
add_array_2 = np.add(a_array, b_array)
print('add_array_2 is \n', add_array_2, '\nadd_array_2 shape is ', add_array_2.shape, ', dim is ', add_array_2.ndim)

# 矩阵的每个元素加上num
add_array_3 = a_array + num
print('add_array_3 is \n', add_array_3, '\nadd_array_3 shape is ', add_array_3.shape, ', dim is ', add_array_3.ndim)

# 矩阵的每个元素乘 (乘法运算符和multiply是一样的操作)
multi_array_1 = a_array * b_array
print('multi_array_1 is \n', multi_array_1, '\nmulti_array_1 shape is ', multi_array_1.shape, ', dim is ',
      multi_array_1.ndim)

multi_array_2 = np.multiply(a_array, b_array)
print('multi_array_2 is \n', multi_array_2, '\nmulti_array_2 shape is ', multi_array_2.shape, ', dim is ',
      multi_array_2.ndim)

# 矩阵的点乘, 标准的矩阵的乘法  x行y列的矩阵乘以y行z列的矩阵，得到的是x行z列的矩阵
multi_array_3 = np.dot(a_array, c_array)
print('multi_array_3 is \n', multi_array_3, '\nmulti_array_3 shape is ', multi_array_3.shape, ', dim is ',
      multi_array_3.ndim)

one_array = np.arange(12).reshape(2, 2, 3)
print('one_array is \n', one_array)

# 这些函数从给定数组中的元素沿指定轴返回最小值和最大值
# 如果axis=None，则表示得到所有元素的最大和最小值
# 如果axis=0, 则表示，结果是(2,3)的矩阵，比较第1和第2维组成的矩阵的大小值
# 如果axis=2, 则表示，结果是(2,2)的矩阵，比较第0和第1维组成的矩阵的大小值
# 其他所有计算方法，比如mean, average等，都是可以这样进行计算
min_array = np.amin(one_array, 0)
max_array = np.amax(one_array, 0)
print('min_array is \n', min_array, '\nmax_array is \n', max_array)

# 这两个函数分别沿给定轴返回最大和最小元素的索引
min_index = np.argmin(one_array, 0)
max_index = np.argmax(one_array, 0)
print('min_index is \n', min_index, '\nmax_index is \n', max_index)


