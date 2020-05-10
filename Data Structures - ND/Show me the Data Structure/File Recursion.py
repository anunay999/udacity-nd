#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 02:31:50 2020

@author: anunay.aatipamula
"""

## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os



def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    suffix_files = list()
    if os.path.isfile(path) and path.endswith(suffix):
        return [path]
    else:
        if os.path.isdir(path):
            for file in os.listdir(path):
                matching_suffix_path = find_files(suffix,os.path.join(path,file))
                if matching_suffix_path:
                    suffix_files.extend(matching_suffix_path)              
    return suffix_files

# Let us print the files in the directory in which you are running this script
print( find_files('.c', './testdir') )
#['./testdir/subdir3/d.c', './testdir/subdir2/c.c', './testdir/subdir2/subsubdirA/b.c', './testdir/e.c', './testdir/subdir.c/a.c']

print( find_files('.h', './testdir') )
#['./testdir/subdir2/subsubdirA/b.h', './testdir/subdir1/a.h']

print( find_files('.py', './testdir') )
#[]

#print( find_files('', './testdir') )
# AssertionError

#print( find_files(None, './testdir') )
# AssertionError