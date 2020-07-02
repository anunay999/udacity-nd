#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:03:35 2020

@author: anunay.aatipamula
"""

## Represents a single node in the Trie
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.nodes = dict()
        self.isWord = False
        
        ## Add a child node in this Trie
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self,root = TrieNode()):
        ## Initialize this Trie (add a root node)
        self.root = root
        
    def insert(self, word):
        ## Add a word to the Trie
        current_char = self.root
        for char in word:
            if char not in current_char.nodes:
                current_char.nodes[char]  = TrieNode()
            current_char = current_char.nodes[char]
        current_char.isWord = True
        
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_char = self.root
        word = str()
        for char in prefix:
            if char in current_char.nodes:
                word += char
                current_char = current_char.nodes[char]
            else:
                return None
        return Trie(current_char)
            
    def get_words(self,word,current_char,autocomplete):
        if current_char.isWord :
            autocomplete.append(word)
        for char in current_char.nodes.keys():
            self.get_words(word+char,current_char.nodes[char],autocomplete)
        return autocomplete
    
    def suffixes(self, prefix,suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        autocomplete = list()
        if prefix != '':
            prefixNode = self.find(prefix)
        else:
            #prefixNode = Trie(self.root)
            return ['please enter text']
            
        if prefixNode:
            words = self.get_words('',prefixNode.root,autocomplete)
            words = list(filter(lambda x : len(x)!=0,words))
            return words
        else:
            return ['not found']
        
            
        

        
            
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


print('Pass' if ['not found'] == MyTrie.suffixes("hello") else 'Fail')
print('Pass' if ['please enter text'] == MyTrie.suffixes("") else 'Fail')

print('Pass' if ['un', 'unction', 'actory'] == MyTrie.suffixes("f") else 'Fail')
print('Pass' if ['hology', 'agonist', 'onym'] == MyTrie.suffixes("ant") else 'Fail')
print('Pass' if ['rie', 'rigger', 'rigonometry', 'ripod'] == MyTrie.suffixes("t") else 'Fail')
print('Pass' if ['hology', 'agonist', 'onym'] == MyTrie.suffixes("ant") else 'Fail')
print('Pass' if ['ger', 'onometry'] == MyTrie.suffixes("trig") else 'Fail')
