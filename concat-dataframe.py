#!/usr/bin/env python
# coding: utf-8

# ### Bibliotecas 

# In[1]:


import pandas as pd


# ### Criando DataFrames

# In[3]:


df1 = pd.DataFrame({"nome": ["Caio", "Rodrigo", "Evandro", "Rafael"], "idade": [28,45,27,16]})


# In[11]:


df1


# In[12]:


df2 = pd.DataFrame({"nome": ["Caio", "Mariane", "Maria"], "idade": [28,29,59]})


# In[13]:


df2


# ### CONCAT simulando SQL UNION ALL

# In[14]:


df = pd.concat([df1,df2])


# In[15]:


df


# In[17]:


df.reset_index(drop=True, inplace=True) # ou usar ignore_index=True dentro do CONCAT


# In[18]:


df


# ### CONCAT simulando SQL UNION

# In[19]:


DF = pd.concat([df1,df2]).drop_duplicates().reset_index(drop=True)


# In[20]:


DF


# In[ ]:




