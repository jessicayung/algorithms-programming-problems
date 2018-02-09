import tensorflow as tf


conv1 = tf.layers.conv2d(x, 32, 5, activation=tf.nn.relu)