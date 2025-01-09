#!/usr/bin/env python
# coding: utf-8
def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter +1
        sum += x
    mean = sum /counter
    return mean
# In[13]:


# Find the product of given numbers
def product(*n): 
    result = 1
    for i  in range(len(n)): 
        result *= n[i]
    return result

