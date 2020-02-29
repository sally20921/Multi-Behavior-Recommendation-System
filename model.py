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

def attention_net(enc, sl, dec, num_units, num_heads, num_blocks, 
                  dropout_rate, is_training, reuse):
  


def  multihead_attention(queries, queries_length, keys, keys_length, 
                         num_units=None, num_heads=8, dropout_rate=0, is_training=true,
                         scope="multihead_attention", reuse=None):
  '''
  queries: A 3d tensor with shape of [N, T_q, C_q]
  keys: A 3d tensor with shape of [N, T_k, C_k]
  Returns
    A 3d tensor with shape of (N, T_q, C)
  '''
  
  def feedforward(inputs, num_units=[2048, 512], scope="feedforward",
                  reuse=None):
    '''Point-wise feed forward net.
    
    inputs: A 3d tensor with shape of [N, T, C].
    
    Returns:
    A 3d tensor with the same shape and dtype as inputs
  '''
