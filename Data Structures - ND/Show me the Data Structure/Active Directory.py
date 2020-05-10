#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 02:49:49 2020

@author: anunay.aatipamula
"""

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    elif len(group.get_groups())==0:
        return False
    else:
        for grp in group.get_groups():
            is_found = is_user_in_group(user,grp)
            if is_found:
                return True
    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child_user = "child_user"
child.add_user(child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test Case 1
answer = is_user_in_group("sub_child_user", parent)
print(answer)
# True
# Test Case 2

answer = is_user_in_group("sub_child_user", child)
print(answer)
# True
# Test Case 3

answer = is_user_in_group("a_child", parent)
print(answer)
# False
# Test Case 4

answer = is_user_in_group("child_user", parent)
print(answer)
# True