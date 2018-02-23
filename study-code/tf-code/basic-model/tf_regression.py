#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_points = np.linspace(-1, 1, 100)[:, np.newaxis]
print('x points shape is ', x_points.shape)

noise = np.random.uniform(-0.15, 0.15, size=x_points.shape)
# y_points = np.sqrt(1 - np.power(x_points, 2)) * np.power(-1, np.random.randint(1, 3, 100)[:, np.newaxis]) + noise
y_points = np.power(x_points, 3) + noise
print('y points shape is ', y_points.shape)

# plt.figure(1, figsize=(8, 6))
# plt.xlim(-2, 2)
# plt.ylim(-2, 2)
# plt.scatter(x_points, y_points)
# plt.show()

tf_x = tf.placeholder(tf.float32, x_points.shape)
tf_y = tf.placeholder(tf.float32, y_points.shape)

# l1 为 (100, 10)
l1 = tf.layers.dense(tf_x, 10, tf.nn.relu)

# 第三个参数activation为None的化，默认为线性变换
# output 为 (100, 1)
output = tf.layers.dense(l1, 1)

loss = tf.losses.mean_squared_error(tf_y, output)

# optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
optimizer = tf.train.AdamOptimizer(learning_rate=0.1)


train_op = optimizer.minimize(loss)

plt.ion()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(200):
        _, l, l1_, pred = sess.run(
            [train_op, loss, l1, output], {tf_x: x_points, tf_y: y_points})
        if step % 200 == 0:
            plt.cla()
            plt.scatter(x_points, y_points)
            plt.plot(x_points, pred, 'r-', lw=5)
            plt.text(0.5, 0, 'Loss=%.4f' %
                     l, fontdict={'size': 20, 'color': 'red'})
            plt.pause(0.1)

plt.ioff()
plt.show()
