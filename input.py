import numpy as np 

class DataInput: 
  def __init__(self, data, batch_size):
    self.batch_size =  batch_size
    self.data = data 
    self.epoch_size = len(self.data)//self.batch_size
                  
