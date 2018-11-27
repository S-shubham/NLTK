#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


from nltk.corpus import gutenberg


# In[3]:


# Lets print some texts contained in nltk form project gutenberg


# In[6]:


gutenberg.fileids()


# In[7]:


# Lets do some processing on each of the text files in nltk


# In[8]:


for fileid in gutenberg.fileids():
    num_chars=len(gutenberg.raw(fileid))
    num_words=len(gutenberg.words(fileid))
    num_sents=len(gutenberg.sents(fileid))
    num_vocab=len(set(w.lower() for w in gutenberg.words(fileid)))
    # Lets print the stats
    print("*****")
    print(fileid)
    print("Average no. of characters per word is : ",round(num_chars/num_words))
    print("Average no. of words per sentence is : ",round(num_words/num_sents))
    print("Average frequency of word in text is : ",round(num_words/num_vocab))
    print("______")


# In[9]:


# If observed closely a very surprising revealatioin occurs
# Notice the average word length is 4/5, which is a characteristics of english language
# Average sentence length is the characteristic of the author. 


# In[11]:


mb=gutenberg.sents('shakespeare-macbeth.txt')


# In[12]:


mb


# In[13]:


len(mb)


# In[14]:


# There are 1907 sentences


# In[16]:


# lets find the length of the longest sentence in the text
longest=(max(len(s) for s in mb))


# In[18]:


# lets print the sentence which has the maximum number of words in it
[s for s in mb if len(s)==longest]


# In[19]:


# lets work with some informal text


# In[20]:


from nltk.corpus import webtext


# In[ ]:




