from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Imports
import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# the model is: y = softmax(W*x + b)


def main():
    mnist = input_data.read_data_sets("./MNIST-data", one_hot=True)

    x = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.matmul(x, W) + b
    y_ = tf.placeholder(tf.float32, [None, 10])
    print(y_, y)

    loss = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(
            labels=y_,
            logits=y
        )
    )
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()

    # train the model
    for (_) in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    # test the model
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print(sess.run(
        accuracy,
        feed_dict={x: mnist.test.images,
                   y_: mnist.test.labels}
    ))


if __name__ == "__main__":
    main()