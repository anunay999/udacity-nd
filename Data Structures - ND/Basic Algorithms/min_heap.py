#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:48:19 2020

@author: anunay.aatipamula
"""

class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]        # initialize arrays
        self.next_index = 0                                   # denotes next index where new element should go
    
    def get_parent(self,ind):
        return int((ind-1)/2)
    
    def swap(self,ind1,ind2):
        if ind1<len(self.cbt) and ind2<len(self.cbt):
            temp = self.cbt[ind1]
            self.cbt[ind1] = self.cbt[ind2]
            self.cbt[ind2] = temp
            
    def heapify(self):
        current_ind = self.next_index
        ind = self.get_parent(current_ind)
        while(self.cbt[ind] > self.cbt[current_ind] and ind>=0 and ind < len(self.cbt)):
            self.swap(ind,current_ind)
            current_ind = ind
            ind = self.get_parent(current_ind)      
        self.next_index+=1
        
    def insert(self, data):
        if(self.next_index < len(self.cbt)):
            self.cbt[self.next_index] = data
            self.heapify()
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]
    def __repr__(self):
        return str(self.cbt)
    
            
        