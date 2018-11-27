#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


from nltk.tokenize import sent_tokenize


# In[3]:


text="""Hello Mr. Smith how are you doing and this is a fantastic news. I am really happy to hear that you are doing greate in your personal life.
I think now is the time to get started with it. you have been really helpful in achieving the goals for today."""


# In[8]:


# Now we are going to tokenize the text into sentence
t_text=sent_tokenize(text)


# In[9]:


print(t_text)


# In[10]:


# now we intend to tokenize the sentence into words
from nltk.tokenize import word_tokenize


# In[11]:


t_word=word_tokenize(text)


# In[12]:


# Print the tokenized word
print(t_word)


# In[13]:


# Now we are interested in finding the frequency distribution of the words in the text
from nltk.probability import FreqDist


# In[14]:


f_dist=FreqDist(t_word)


# In[15]:


# Now we want to print the top 5 most common words in our text
f_dist.most_common(5)


# In[16]:


# Lets do frequency distribution plot


# In[17]:


import matplotlib.pyplot as plt


# In[18]:


f_dist.plot(30,cumulative=False)


# In[20]:


# Now we would like to remove stopwords from our text 
# stopwords can also be custom built
# We will use the nltk library list of stopwords
from nltk.corpus import stopwords


# In[24]:


stop_words=set(stopwords.words("english"))


# In[25]:


# lets print the stopwords
print(stop_words)


# In[26]:


len(stop_words)


# In[27]:


# Let's remove stopwords
filtered_words=[]


# In[28]:


for word in t_word:
    if word not in stop_words:
        filtered_words.append(word)


# In[32]:


# Now we have successfully removed the stopwords from the text


# In[33]:


# Let's print the filtered words
filtered_words


# In[ ]:




