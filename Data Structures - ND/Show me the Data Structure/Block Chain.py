#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 02:16:12 2020

@author: anunay.aatipamula
"""

import hashlib
import datetime

class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = datetime.datetime.now()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
      self.next =  None

    def calc_hash(self,data):
      if data:
          sha = hashlib.sha256()
          hash_str = data.encode('utf-8')
          sha.update(hash_str)
          return sha.hexdigest()
      else:
          return None
        
    def __repr__(self):
        return 'Block Timestamp: {}\nData : {}\nHash :  {}\nPrevious Hash : {}'.format(self.timestamp,self.data,self.hash,self.previous_hash)
  

class BlockChain:
    
    def __init__(self,head = None):
        self.block_head = head   
        self.block_tail = head
        self.size = 0
        
    def add_block(self,data):
        if self.block_head is None:
            self.block_head = Block(data,None)
            self.block_tail = self.block_head
        else:
            self.block_tail.next = Block(data,self.block_tail.hash)
            self.block_tail = self.block_tail.next
        self.size+=1
    
    def get_block(self,data):
        pos_block = self.block_head
        while pos_block:
            if(data is pos_block.data):
                return  pos_block
            pos_block = pos_block.next
        return None
    
    
    
    def capacity(self):
        return self.size
    
    def to_list(self):
        pos_block = self.block_head
        blockchain = list()
        while pos_block:
            blockchain.append(pos_block.data)
            pos_block = pos_block.next
        return blockchain
    
    def print_blocks(self):
        pos_head = self.block_head
        while pos_head:
            print(pos_head)
            pos_head = pos_head.next

    def __repr__(self):
        return str(self.to_list())
            
#Test Cases       
chain = BlockChain()
chain.add_block('data for a')
chain.add_block('data for b')
chain.add_block('data for c')
chain.add_block(None)

#Test Case 1
print('Pass' if chain.block_head.data=='data for a' else 'Fail')
# data for a
b = chain.block_head.next
c = chain.block_head.next.next


#Test Case 2

print('Pass' if b.hash == c.previous_hash else 'Fail')# True
print('Pass' if c.data=='data for c' else 'Fail')
# data for c





#Test Case 3 - Edge Cases

blockchain = BlockChain()

print('Pass' if blockchain.capacity()==0 else 'Fail')
# 0
print('Pass' if blockchain.to_list()==[] else 'Fail')
# []
blockchain.add_block('data for 1')
print('Pass' if blockchain.capacity()==1 else 'Fail')

# 1
print('Pass' if blockchain.to_list()==['data for 1'] else 'Fail')
# [['my balance: 0 | cash flow: +10 | final balance: 10', 1564306421.0008988, '5e5a93abe59f9e92b38e00ebc7a50c50f902f5a8
# 210d327590a36ffb25a831d9']]

#Test cases 4
blockchain.add_block('data for 2')
blockchain.add_block('data for 3')
blockchain.add_block('data for 4')
blockchain.add_block('data for 5')
print('Pass' if blockchain.capacity()==5 else 'Fail')
# 5
print('Pass' if blockchain.to_list()==['data for 1', 'data for 2', 'data for 3', 'data for 4', 'data for 5'] else 'Fail')


# Testing the "search function"
print(blockchain.get_block('data for 3'))
#Block Timestamp: 2020-05-09 23:22:21.050451
#Data : data for 3
#Hash :  3320a650047255bc1ae895ee8fd0edac2b5c517d7adc6ca041fca119a95b1ba3
#Previous Hash : c4ef6d399171955f1e8392bcb412f0ef8fd0ae202cd3ab4ec32fc9839b6c5d90


# Test cases 5 Edge Cases:
print('Pass' if blockchain.get_block('data for 10')== None else 'Fail')
# None

