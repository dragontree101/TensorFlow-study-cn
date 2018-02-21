#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

import tensorflow as tf

# 占位符, 在实际运算的时候传入值
tf_placeholder_1 = tf.placeholder(dtype='int32', shape=[1, 2])
tf_placeholder_2 = tf.placeholder(dtype='int32', shape=[1, 2])
tf_placeholder_3 = tf.placeholder(dtype='int32', shape=[2, 1])

add_result = tf_placeholder_1 + tf_placeholder_2
matmul_result_1 = tf.matmul(add_result, tf_placeholder_3)
matmul_result_2 = tf.matmul(tf_placeholder_1, tf_placeholder_3)

with tf.Session() as sess:
    matmul_result_1, matmul_result_2 = sess.run(
        [matmul_result_1, matmul_result_2],
        feed_dict={
            tf_placeholder_1: [[1, 2]],
            tf_placeholder_2: [[3, 4]],
            tf_placeholder_3: [[5], [6]]
        })
    print(matmul_result_1)
    print(matmul_result_2)
