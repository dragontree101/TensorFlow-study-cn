#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

import numpy as np

# 生成一个(3,3,3)的随机矩阵，元素的值在均匀分布(0, 1)之间
random_array_1 = np.random.random((3, 3, 3))
print('random_array_1 is \n', random_array_1, '\nrandom_array_1 shape is ', random_array_1.shape)

# 生成一个(3, 3)的随机矩阵，元素的值均匀分布[-10,10)中随机采样
random_array_2 = np.random.uniform(-10, +10, (3, 3))
print('random_array_2 is \n', random_array_2, '\nrandom_array_2 shape is ', random_array_2.shape)

# 生成一个(5,)的随机矩阵，元素的值均匀分布[0, 2)中随机的整数
random_array_3 = np.random.randint(0, 2, 5)
print('random_array_3 is \n', random_array_3, '\nrandom_array_3 shape is ', random_array_3.shape)


# 生成一个(2,2)的随机矩阵，元素的值满足正态分布，其中loc为平均值, scale为平方差
random_array_4 = np.random.normal(loc=0, scale=1, size=(2, 2))
print('random_array_4 is \n', random_array_4, '\nrandom_array_4 shape is ', random_array_4.shape)
