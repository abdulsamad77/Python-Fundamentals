#!/usr/bin/env python
# coding: utf-8

# In[ ]:


continuation with strings;


# In[1]:


fullname='abdul samad'
print(fullname)


# In[2]:


print(fullname.title())


# In[ ]:


To convert the entire name in capital letters :


# In[3]:


print(fullname.upper())


# In[ ]:


to comvert in small letters :


# In[4]:


print (fullname.lower())


# In[ ]:


Introduction to f Strings : **


# In[ ]:


=> general syntax of f strings :
    f"custom message {placeholder1},{placeholder2},....{placeholdern}"


# In[5]:


firstname='abdul'
lastname='samad'
fullname=f"{firstname} {lastname}"
print(fullname)


# In[6]:


print(fullname.title())


# In[9]:


message= f"keep up the good work {fullname.title()}"
print(message)


# In[ ]:





# In[ ]:


Adding white spaces to strings :


# In[10]:


print("fav_language:htmlcssjavascriptnode.js")


# In[11]:


print("fav_language:\nhtml\ncss\njavascript\nnode.js")


# In[12]:


print("fav_language:\n\thtml\n\tcss\n\tjavascript\n\tnode.js")


# In[ ]:





# In[ ]:


Removing white spaces from strings :


# In[13]:


name='python'
print(name)


# In[16]:


name1='python '
print(name1)


# In[17]:


name2=' python'
print(name2)


# In[19]:


name1.rstrip()


# In[20]:


name2.lstrip()


# In[ ]:




