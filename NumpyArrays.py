#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


x = np.array(["A",67,57,9.8])
print(x)
print(type(x))
print(x.dtype)


# In[4]:


a2 = np.array([[20,40],[30,60]])
print(a2)
print(type(a2))
print(a2.shape)


# In[6]:


# Reshaping an array
a = np.array([10,20,30,40])
b = a.reshape(2,2)
print(b)
print(b.shape)


# In[7]:


# Create an array with arange()
c = np.arange(3,20)
print(c)
type(c)


# In[8]:


# Use of around
d = np.array([1.3467, 3.10987, 4.91236])
np.around(d,2)


# In[9]:


# Use of np.sqrt
print(np.around(np.sqrt(d),2))


# In[12]:


# Use astype() to convert the data type
a1 = np.array([[3,4,5,8],[7,2,8,np.NaN]])
print(a1)
a1.dtype


# In[13]:


a1_copy1 = a1.astype(str)
print(a1_copy1)
a1_copy1.dtype


# In[14]:


a2 = np.array([[3,4,6],[7,9,10],[4,6,12]])
a2


# In[15]:


print(a2.sum(axis = 1))
print(a2.sum(axis=0))


# In[16]:


# Find the nean values along row and col
print(a2)
print(np.mean(a2, axis = 1))
print(np.mean(a2, axis = 0))


# In[17]:


# Matrix operations
a3 = np.array([[3,4,5],[7,2,8],[9,1,6]])
print(a3)
np.fill_diagonal(a3,0)
print(a3)


# In[19]:


# Define two matrices and multiply them
A = np.array([[1,2], [3,4]])
B = np.array([[5,6],[7,8]])

# Perform matrix multiplication
C = np.matmul(A,B)
print(c)


# In[20]:


# Transpose
print(A.T)
print(B.T)


# In[21]:


# Accessing the array elements 
a4 = np.array([[3,4,5],[7,2,8],[9,1,6],[10,9,18]])
a4


# In[29]:


# Slicing of array
a4[0:,2:]


# In[ ]:




