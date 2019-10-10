#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import random


# In[12]:


x = [35, 50, 65, 80]
a = random.randint(1,100)
y = [50, 70, 75, 80]


# In[13]:


def computeLoss(x,y,a):
    for i in range (1, 5):
        L = (x[i] * a - y[i])**2
    return Loss


# In[14]:


def computeGrad(x,y,a):
    grad = (2a * x**2[i] - 2x[i] * y[i])
return grad


# In[15]:


def main():
    epoch = 10
    lrate = 0.001
    for j in range (1,10):
        print(computeLoss)
        a = a - lrate * computeGrad

