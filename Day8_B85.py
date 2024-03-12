#!/usr/bin/env python
# coding: utf-8

# In[ ]:


introduction t dictionaries **


# In[ ]:


defination : a dict is a combination of key value pairs.
classification : it is classified as an mutable datatype.
how to define it ====> { }


# In[2]:


alien={'color':'green','points':5}  # key : value


# In[3]:


print(alien)


# In[4]:


type(alien)


# In[ ]:


# how to add new key value pairs to the dictionary


# In[ ]:


# req : i want to add the start_value at 0


# In[5]:


alien['start_value']=0


# In[6]:


print(alien)


# In[ ]:


# how to modify the value


# In[8]:


alien['color']= 'yellow'


# In[9]:


print(alien)


# In[ ]:


# how to delete the key value pairs


# In[10]:


del alien['points']


# In[11]:


print(alien)


# In[12]:


user_account={'user_name':'code_training_academy','first_name':'code','last_name':'training','password':54321}
print(user_account)


# In[ ]:


# for loop : ==========> general syntax

for tempvar in mainvar:
    print(tempvar)


# In[ ]:


# for dictionary


# In[ ]:


for k,v in mainvar.items():
    print(k,v)


# In[13]:


for a,b in user_account.items():
    print(a)
    print(b)


# In[ ]:


# enhancement of the code


# In[14]:


for a,b in user_account.items():
    print(f'key:{a}')
    print(f'key:{b}\n')


# In[ ]:


# if we want only the keys


# In[16]:


for a in user_account.keys():
    print(f'key:{a}')


# In[ ]:


# if we want values only


# In[21]:


for b in user_account.values():
    print(f'values:{b}\n')


# In[ ]:





# In[ ]:





# In[ ]:




