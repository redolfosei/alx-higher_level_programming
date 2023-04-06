#!/usr/bin/python3
"""LockedClass defind here which will use slot attribute"""
class LockedClass:
    """
    This prevents user from instantiating new LockedClass attributes
    for anything except the  attributes called 'first_name'.
    """
    __slots__ = ["first_name"]
