import tensorflow as tf 

from data_load import load_vocab
from modules import get_token_embeddings, ff, positional_encoding, multihead_attention, label_smoothing, noam_scheme
from uitls import convert_idx_to_token_tensor
from tqdm import tqdm 
import logging 

class Transformer:

def encode(self, xs, training=True):
def decode(self, ys, memory, src_masks, training=True):
