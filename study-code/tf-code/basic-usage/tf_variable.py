#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

import tensorflow as tf

# 定义一个变量，并且给定了一个明确的值
variable_1 = tf.Variable(tf.zeros([3, 4]))

add_operation = tf.add(variable_1, 1)

# 用add_operation来更新variable_1
update_operation = tf.assign(variable_1, add_operation)

with tf.Session() as sess:
    # 初始化全局变量
    sess.run(tf.global_variables_initializer())
    for _ in range(3):
        print(sess.run(variable_1))
        sess.run(update_operation)
