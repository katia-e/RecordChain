import pdb
from time import time
import nacl  
from nacl.public import PrivateKey, Box
import hashlib


class Record:
    """
    class Record describes an object of a record chain
    """
    def __init__(self, data, prev_hash='', prev_index=0):
        self.data = data
        self.prev_index = prev_index
        self.index =  self.prev_index+1
        self.prev_hash = prev_hash
        self.timestamp = time()
        self.hash = self.calc_hash()
    

    @ property
    def calc_hash(self):
        h = hashlib.new('ripemd160')
        h.update(self.data.encode()+self.prev_hash.encode())
        return h.hexdigest()

    def show(self):
        print("data: ", self.data)
        print("prev_hash: ", self.prev_hash)
        print("timestamp: ", self.timestamp)
        print("index: ", self.index)


class Chain:
    def __init__(self):
        self.record = Record('Genesis')
        self.chain = [self.record]
        self.hash = b''
        self.index = 0
    
    def add(self, data):
        self.index+=1
        new_record = Record(data, self.chain[-1].hash, self.index)
        self.chain.append(new_record)
    
    def broken(self):
        for i, record in enumerate(self.chain):        
            if i:
                if self.chain[i-1].calc_hash() != record.prev_hash:
                    return True
        return False

    def __getitem__(self, k):
        return self.chain[k]
    def __setitem__(self, k, v):
        return self.chain[k] = v

    def show(self):
        for record in self.chain:
            record.show()

            
        
           




    
