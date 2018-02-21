#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

import tensorflow as tf

tf_constant_1 = tf.constant([[2, 3]], shape=[1, 2])
tf_constant_2 = tf.constant([[4, 5]], shape=[1, 2])
tf_constant_3 = tf.constant([[6], [7]], shape=[2, 1])

add_operation = tf.add(tf_constant_1, tf_constant_2)

# 矩阵的点乘, 等同于np.multiply, 每个元素上面的值相乘
dot_operation_1 = tf.multiply(add_operation, tf_constant_3)
# 矩阵的乘法, 等同与np.dot, 行列相乘
dot_operation_2 = tf.matmul(add_operation, tf_constant_3)

with tf.Session() as sess:
    result_1 = sess.run(dot_operation_1)
    result_2 = sess.run(dot_operation_2)
    print('add operation is \n', add_operation.eval())
    print('result 1 is \n', result_1)
    print('result 2 is \n', result_2)



