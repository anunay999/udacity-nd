#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 02:05:36 2020

@author: anunay.aatipamula
"""
import re
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,route_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(route_handler)
        
    def insert(self,path,handler = None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_path = self.root
        for route in path:
            current_path = current_path.insert(route)
        current_path.handler = handler
            
            

    def find(self,path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_path = self.root
        for route in path:
            if route not in current_path.node:
                return None
            current_path = current_path.node[route]
        return current_path.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,handler=None):
        # Initialize the node with children as before, plus a handler
        self.node = dict()
        self.handler = handler
        
    def insert(self,key):
        # Insert the node as before
        if key in self.node:
            return self.node[key]
        else:
            self.node[key] = RouteTrieNode()
            return self.node[key]
        

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self,route_handler,not_found):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(route_handler)
        self.not_found = not_found

    def add_handler(self,path,handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        routes  = self.split_path(path)
        self.route_trie.insert(routes,handler)

    def lookup(self,path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        routes  = self.split_path(path)
        handler = self.route_trie.find(routes)
        if handler:
            return handler
        else:
            return self.not_found


    def split_path(self,path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if(len(path) < 1):
            return []
        routes = re.split('/',path)
        if(len(routes)>0 and routes[0] == ''):
            routes.pop(0)
            if(routes[len(routes)-1]==''):
                routes.pop(len(routes)-1)
        return routes


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route
# some lookups with the expected output
print ("Pass" if  ("root handler" == router.lookup("")) else "Fail")
print ("Pass" if  ("root handler" == router.lookup("/")) else "Fail")
print ("Pass" if  ("about handler" == router.lookup("/home/about")) else "Fail")

print ("Pass" if  ("not found handler" == router.lookup("/home")) else "Fail")
print ("Pass" if  ("about handler" == router.lookup("/home/about")) else "Fail")
print ("Pass" if  ("about handler" == router.lookup("/home/about/")) else "Fail")
print ("Pass" if  ("not found handler" == router.lookup("/home/about/me")) else "Fail")
print ("Pass" if  ("not found handler" == router.lookup(".")) else "Fail")


