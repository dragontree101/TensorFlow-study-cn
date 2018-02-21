#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-5, 5, 200)

# 常用的激活函数
# relu激活函数公式 f(x) = max(0, x)
# 收敛速度会比 sigmoid/tanh 快很多
y_relu = tf.nn.relu(x)

# sigmoid激活函数公式 f(x) = 1 / (1+ (e^-x)), 它能够把输入的连续实值压缩到0和1之间
# 在特征相差比较复杂或是相差不是特别大时效果比较好
# 反向传播时，很容易就会出现梯度消失的情况，从而无法完成深层网络的训练
y_sigmoid = tf.nn.sigmoid(x)

# tanh激活函数公式 f(x)=((e^x) - (e^-x)) / ((e^x) + (e^-x)) = 2 * sigmoid(2x) - 1
# 取值范围为[-1,1]
# anh在特征相差明显时的效果会很好，在循环过程中会不断扩大特征效果
y_tanh = tf.nn.tanh(x)

# softplus激活函数公式 f(x)=log(1 + e^x)
# 取值范围是(0, +∞)
y_soft_plus = tf.nn.softplus(x)

# softmax是基于概率的归一化, 用于多分类神经网络输出
# 取值范围是[0, 1]
y_softmax = tf.nn.softmax(x)

sess = tf.Session()
y_relu, y_sigmoid, y_tanh, y_soft_plus, y_softmax = sess.run(
    [y_relu, y_sigmoid, y_tanh, y_soft_plus, y_softmax])

sess.close()


plt.figure(1, figsize=(8, 6))
plt.subplot(221)
plt.plot(x, y_relu, c='red', label='relu')
plt.ylim((-1, 5))
plt.legend(loc='best')

plt.subplot(222)
plt.plot(x, y_sigmoid, c='red', label='sigmoid')
plt.ylim((-0.2, 1.2))
plt.legend(loc='best')

plt.subplot(223)
plt.plot(x, y_tanh, c='red', label='tanh')
plt.ylim((-1.2, 1.2))
plt.legend(loc='best')

plt.subplot(224)
plt.plot(x, y_soft_plus, c='red', label='soft_plus')
plt.ylim((-0.2, 6))
plt.legend(loc='best')

plt.show()


plt.plot(x, y_softmax, c='red', label='softmax')
plt.legend(loc='best')
plt.show()
