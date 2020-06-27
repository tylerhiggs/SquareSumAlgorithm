#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:05:36 2020

@author: Tyler Higgs


Daily Coding Problem: Problem #156
"""

memo = {} # i->x(i)


def x(i):
    '''
    Given a positive integer i, find the smallest number of squared
    integers which sum to i
    
    For example, given i = 13, return 2 since 13 = 3^2 + 2^2
    
    Given i = 27, return 3 since 27 = 3^2 + 3^2 + 3^2
    
    Solved using dynamic programming in O(n^2) time
    '''
    if i in memo:
        return memo[i]
    elif i == 0:
        memo[i] = 0
        return 0
    else:
        smallest = float("inf")
        for j in range(1,i+1):
            if i - j**2 >= 0:
                attempt = x(i - j**2)
                if attempt + 1 < smallest:
                    smallest = attempt + 1
            else:
                break
        memo[i] = smallest
        return smallest
    
print(x(171))
                
                

