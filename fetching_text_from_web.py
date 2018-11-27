#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk,re,pprint


# In[2]:


from nltk import word_tokenize


# In[3]:


from urllib import request


# In[6]:


url="http://www.gutenberg.org/files/2554/2554-0.txt"


# In[7]:


response=request.urlopen(url)


# In[9]:


raw=response.read().decode('utf8')


# In[10]:


# now we have read the text file from the above link


# In[11]:


#lets check the type of raw
type(raw)


# In[12]:


len(raw)


# In[13]:


# this is the number of characters read from the link


# In[14]:


#lets print the first 100 characters
raw[:100]


# In[16]:


#  lets tokeninze all the characters into words
w_tokens=word_tokenize(raw)


# In[17]:


type(w_tokens)


# In[19]:


len(w_tokens)


# In[ ]:


# sometimes it is not possible to extract a specific section of text from a file 

