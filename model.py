'''Transformer Network'''

import tensorflow as tf
from data_load import load_vocab
from modules import get_token_embeddings, ff, positional_encoding, multihead_attention,label_smoothing, noam_scheme
from utils import convert_idx_to_token_tensor
from tqdm import tqdm 
import  logging 

logging.basicConfig(level=logging.INFO)

class Transformer:
  def __init__(self, hp):
    self.hp = hp
    self.token2idx, self.idx2token = load_vocab(hp.vocab)
    self.embeddings= get_token_embeddings(self.hp.vocab_size, self.hp.d_model, zero_pad = True)
    
    '''
    xs: tuple of 
      x: int32 tensor (N, T1)
      x_seqlens: int32  tensor (N,)
      sents1: str tensor (N,)
      
      ys: tuple of 
        decoder_input: int32 tensor (N, T2)
        y: int32 tensor (N, T2)
        y_seqlen: int32  tensor (N,)
        sents2: str tensor (N,) 
    
  def encode(self, xs, training=True):
  '''returns  memory: encoder outputs. (N, T1, d_model)
      
  def decode(self, ys, memory, src_masks, training=True):
    '''
    memory: encoder outputs. (N, T1, d_model)
    src_masks: (N, T1)
    
    Returns
    logits: (N,T2, V). float32.
    y_hat:(N,T2). int32.
    y:(N,T2). int32.
    sents2:(N,).string.
    '''
    
  def train(self, xs, ys):
  def eval(self, xs, ys): 
