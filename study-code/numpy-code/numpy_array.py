#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3
# numpy常用的构造和操作array的方法

import numpy as np

# 构建一个一维的数据, 数据维度为(3,)
one_dim = np.array([1, 2, 3], dtype='i4')
print('one_dim is \n', one_dim, '\none_dim shape is ', one_dim.shape)

# 生成从1开始到10,步长为2的一维数据
arange_array = np.arange(1, 10, 2, dtype=int)
print('arange_array is \n', arange_array, '\narange_array shape is ', arange_array.shape, ', dim is ',
      arange_array.ndim)

# 构建一个两维的数据, 数据维度为(2,2)
two_dim_1 = np.array([[1, 3], [2, 4]], dtype='i4')
print('two_dim_1 is \n', two_dim_1, '\ntwo_dim_1 shape is ', two_dim_1.shape)

# 通过一维的数据构建一个两维的矩阵, 数据维度为(1,5)
two_dim_2 = np.array([1, 2, 3, 4, 5], dtype='i4', ndmin=2)
print('two_dim_2 is \n', two_dim_2, '\ntwo_dim_2 shape is ', two_dim_2.shape)

# reshape把一个(2,3)的矩阵转化成一个(3,2)的矩阵
array_2_3 = np.array([[1, 2, 3], [4, 5, 6]], dtype='i4')
array_3_2 = array_2_3.reshape(3, 2)
print('array_2_3 is \n', array_2_3, '\narray_2_3 shape is ', array_2_3.shape, ', dim is ', array_2_3.ndim)
print('array_3_2 is \n', array_3_2, '\narray_3_2 shape is ', array_3_2.shape, ', dim is ', array_3_2.ndim)

# 生成数据, 通过ndim查看是几维矩阵
new_array = np.arange(24)
print('new_array is \n', new_array, '\nnew_array shape is ', new_array.shape, ', dim is ', new_array.ndim)

# 生成空数据
empty_array = np.empty([3, 2], dtype=int)
print('empty_array is \n', empty_array, '\nempty_array shape is ', empty_array.shape, ', dim is ', empty_array.ndim)

# 生成元素为0的数据
zero_array = np.zeros([4, 3], dtype=int)
print('zero_array is \n', zero_array, '\nzero_array shape is ', zero_array.shape, ', dim is ', zero_array.ndim)

# 生成元素为1的数据
one_array = np.ones([3, 4], dtype=int)
print('one_array is \n', one_array, '\none_array shape is ', one_array.shape, ', dim is ', one_array.ndim)

# 生成从1开始到10,一共有5个数的一维数据, retstep为True,则表示结果返回步长
(linspace_array, step) = np.linspace(1, 10, 7, retstep=True)
print('linspace_array is \n', linspace_array, '\nlinspace_array shape is ', linspace_array.shape, ', step is ', step)

# 矩阵的转置
array_3_4 = np.arange(12).reshape(3, 4)
print('array_3_4 is \n', array_3_4, '\narray_3_4 shape is ', array_3_4.shape)
array_4_3 = np.transpose(array_3_4)
print('array_4_3 is \n', array_4_3, '\narray_4_3 shape is ', array_4_3.shape)

# 扩充维度
two_dim = np.array(([1, 2], [3, 4]))
three_dim_1 = np.expand_dims(two_dim, axis=0)
three_dim_2 = np.expand_dims(two_dim, axis=1)
print('two_dim shape is ', two_dim.shape, ', three_dim_1 shape is ', three_dim_1.shape, ', three_dim_2 shape is ',
      three_dim_2.shape)

# 压缩维度为1的维
new_two_dim_1 = np.squeeze(three_dim_1)
new_two_dim_2 = np.squeeze(three_dim_2)
print('new_two_dim_1 shape is ', new_two_dim_1.shape, ', new_two_dim_2 shape is ', new_two_dim_2.shape)

# 连接矩阵, vstack 通过堆叠来生成竖直的单个数组
one_a = np.array([[1, 2], [3, 4]])
two_a = np.array([[5, 6], [7, 8]])
new_a = np.vstack((one_a, two_a))
print('new_a is \n', new_a, '\nnew_a shape is ', new_a.shape)

# 连接矩阵, hstack 通过堆叠来生成水平的单个数组
new_b = np.hstack((one_a, two_a))
print('new_b is \n', new_b, '\nnew_b shape is ', new_b.shape)
