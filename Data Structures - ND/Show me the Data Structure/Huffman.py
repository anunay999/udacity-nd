#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:10:26 2020

@author: anunay.aatipamula
"""

import sys

class Node:
    def __init__(self,char,frequency):
        self.char = char
        self.freq = frequency
        self.left = None
        self.right = None
        
    def isLeaf(self):
        return self.right == None and self.left == None
    
class HuffmanTree:
    def __init__(self,head=None):
        self.head = head
    
        
        

def huffman_encoding(data):
    if data is None:
        return data,None
    frequency = get_frequencies(data)
    huff_tree = construct_tree(frequency)
    code_map = get_huff_map(huff_tree)
    encoded_string = str()
    for char in data:
        encoded_string+=code_map[char]
    return encoded_string,huff_tree
    

def huffman_decoding(data,tree):
    if data is None:
        return data
    code_map = get_huff_map(tree)
    code_map = {value: key for key, value in code_map.items()}
    code = str()
    decoded_string = str()
    for bit in data:
        if code in code_map:
            decoded_string += code_map[code]
            code = str()
        code += bit
    if code in code_map:
            decoded_string += code_map[code]
    return decoded_string
        
    

def sort_frequency_nodes(frequency):
    frequency.sort(key=lambda x: x.freq, reverse=True)
    return frequency

def get_frequencies(string):
    characters = list(string)
    nodes = list()
    for char in set(characters):
        nodes.append(Node(char,characters.count(char)))
    return sort_frequency_nodes(nodes)

def construct_tree(nodes):
    if len(nodes) == 1:
        return nodes[0]
    else:
        left_node = nodes.pop()
        right_node = nodes.pop()
        cum_freq = left_node.freq+right_node.freq
        current_node = Node(None,cum_freq)
        current_node.left = left_node
        current_node.right = right_node
        nodes.append(current_node)
        sort_frequency_nodes(nodes)
        return construct_tree(nodes)
        
def get_huff_map(head,code = '',):
    code_map = {}
    if head is None:
        return code_map
    else:
        if(head.char is not None):
            code_map[head.char] = code
        code_map.update(get_huff_map(head.left,code+'0'))
        code_map.update(get_huff_map(head.right,code+'1'))
    return code_map
    
        

    
def test_output(text):
    
    encoded_data, tree = huffman_encoding(text)
    
    decoded_data = huffman_decoding(encoded_data, tree)
    
    return decoded_data == text

#Test Case 1
print(test_output("ABBBBABBABABBBAABABABAABABA"))
print(test_output("Test") )
#Test Case 2
print(test_output("The bird is the word") )
#Test Case 3
print(test_output("Androids dream of electric sheep.") )
print(test_output(None) )
