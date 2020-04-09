import tensorflow as tf
import numpy as np

x = tf.constant([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y = tf.constant([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])

num = tf.size(x).numpy()

a = num*tf.reduce_sum(tf.multiply(x,y))

c = tf.multiply(tf.reduce_sum(x),tf.reduce_sum(y))

d = num*tf.reduce_sum(tf.square(x))

e = tf.square(tf.reduce_sum(x))

w = tf.divide(tf.subtract(a,c),tf.subtract(d,e))

f = tf.reduce_sum(y)

g = w*tf.reduce_sum(x)

b = tf.divide(tf.subtract(f,g),num)

print("w的值为：{}\nb的值为：{}".format(w,b))

