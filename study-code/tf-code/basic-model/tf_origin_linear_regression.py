#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3
# 用比较原始的方法来完成线性回归算法

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_points = np.linspace(-1, 1, 100)[:, np.newaxis]
print('x points shape is ', x_points.shape)

noise = np.random.uniform(-0.15, 0.15, size=x_points.shape)
# y_points = np.sqrt(1 - np.power(x_points, 2)) * np.power(-1, np.random.randint(1, 3, 100)[:, np.newaxis]) + noise
y_points = np.power(x_points, 3) + noise
print('y points shape is ', y_points.shape)

tf_x = tf.placeholder("float")
tf_y = tf.placeholder("float")

tf_w = tf.Variable(np.random.randn(), name="weight")
tf_b = tf.Variable(np.random.randn(), name="bias")

# pred = wx + b
pred = tf.add(tf.multiply(tf_x, tf_w), tf_b)

cost = tf.reduce_sum(tf.pow(pred - tf_y, 2)) / (2 * x_points.shape[0])

optimizer = tf.train.GradientDescentOptimizer(0.1).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(200):
        for (x, y) in zip(x_points, y_points):
            sess.run(optimizer, feed_dict={tf_x: x, tf_y: y})

        # Display logs per epoch step
        if (epoch + 1) % 10 == 0:
            c = sess.run(cost, feed_dict={
                tf_x: x_points, tf_y: y_points})
            print("Epoch:", (epoch + 1), "cost=", c,
                  "W=", sess.run(tf_w), "b=", sess.run(tf_b))

    print("Optimization Finished!")
    training_cost = sess.run(
        cost, feed_dict={tf_x: x_points, tf_y: y_points})
    print("Training cost=", training_cost, "W=",
          sess.run(tf_w), "b=", sess.run(tf_b), '\n')

    # Graphic display
    plt.plot(x_points, y_points, 'ro', label='Original data')
    plt.plot(x_points, sess.run(tf_w) * x_points +
             sess.run(tf_b), label='Fitted line')
    plt.legend()
    plt.show()
