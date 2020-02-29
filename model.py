import os
import json
import numpy as np
import tensorflow as tf 

def init_placeholders(self):
# user id
self.u = tf.placeholder(tf.int32, [None,])

# item id 
self.i = tf.placeholder(tf.int32, [None,])

# item label
self.y = tf.placeholder(tf.float32, [None,])

# user's history item id
self.hist_i = tf.placeholder(tf.int32, [None, None])

# user's history item purchase time
self.hist_t  = tf.placeholder(tf.int32, [None, None])

# valid length of 'hist_i'
self.sl = tf.placeholder(tf.int32, [None,])

# learning rate 
self.lr = tf.placeholder(tf.float64, [])

# whether it's training or not 
self.is_training = tf.placeholder(tf.bool, [])
