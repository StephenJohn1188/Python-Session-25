#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[4]:


a=np.array([24,33,52,45,68,78,96,54,12,52])


# In[5]:


a


# In[6]:


np.mean(a)


# In[8]:


np.median(a)


# In[9]:


b=([1,2,3,4,5,6])


# In[10]:


b


# In[11]:


np.mean(b)


# In[13]:


np.median(b)


# In[15]:


p=np.array([[23,45],[66,44]])
p


# In[17]:


np.mean(p,axis=0)


# In[18]:


np.mean(p,axis=1)


# In[19]:


j=np.array([[12,45,48],[89,56,23],[75,53,15]])
j


# In[20]:


np.mean(j)


# In[21]:


np.mean(j,axis=0)


# In[22]:


np.mean(j,axis=1)


# In[23]:


np.median(j)


# In[24]:


np.median(j,axis=0)


# In[25]:


np.median(j,axis=1)


# In[27]:


df=pd.read_csv("student_marks.csv")


# In[28]:


df


# In[29]:


df['Maths'].mean()


# In[32]:


df['Maths'].median()


# In[34]:


df['Maths'].mode()


# In[35]:


a.max()


# In[36]:


a.min()


# In[40]:


range_of_a=a.max()-a.min ()


# In[41]:


range_of_a


# In[42]:


np.var(a)


# In[43]:


np.std(a)

