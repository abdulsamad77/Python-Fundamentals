#!/usr/bin/env python
# coding: utf-8

# In[ ]:


introduction to tuple datatype :


# In[ ]:


defination : an immidiate list is called as a tuple.
classification : it is classified as animmutable datatype ( fixed datatype ===> we will not be able to modify it)
how to define tuple datatype ==> ( )


# In[ ]:





# In[1]:


students=('sarika','keerthi','naveed','joseph')
print(students)


# In[2]:


type(students)


# In[3]:


print(students[0])


# In[ ]:


# req : i want to change sarika name to sangeeta


# In[4]:


students[0]='sangeeta'


# In[5]:


dimensions=(150,200)
print(dimensions)


# In[6]:


type(dimensions)


# In[7]:


dimensions[0]=100


# In[8]:


print(students)


# In[10]:


print(students[2])


# In[18]:


print(students[2].title())


# In[19]:


for a in students:
    print(a)


# In[ ]:


introduction to dictionaries **


# In[ ]:


defination : a dict is a combination of key value pairs.
classification : it is classified as a mutable dataype (we can edit / alter).
how to define it ==> { }


# In[20]:


alien={'color':'green','points':5}
print(alien)


# In[21]:


type(alien)


# In[ ]:


# create a facebook account


# In[22]:


user_name= {'first_name':'code',"last_name":'training','dob':1-1-20,'password':'12345'}
print(user_name)


# In[23]:


type(user_name)


# In[ ]:


# adding new key value pairs to dictionary :


# In[ ]:


"location":'autumn leaf'


# In[24]:


user_name['location']='autumn leaf'
print(user_name)


# In[ ]:


# req : how to access key value


# In[25]:


print(user_name['last_name'])


# In[26]:


print(user_name['code'])


# In[ ]:




