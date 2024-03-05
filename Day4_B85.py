#!/usr/bin/env python
# coding: utf-8

# In[ ]:


introduction to list datatypes :


# In[ ]:


defination : a list is a collection of items in a particular order.
classification : it is classififed as mutable datatype ( which can be edited / modified)
>>> how to define the list datatype ? ===  []


# In[1]:


students = ['khadija','anitha','naveen','suresh','keerthi','david']
print(students)


# In[ ]:


understanding the concept of indexing :


# In[ ]:


# req : i want to access anitha name from the above


# In[2]:


print(students[1])


# In[ ]:


# i want to access suresh name from the above


# In[3]:


print(students[3])


# In[6]:


print(students[3].title())


# In[ ]:


1. how to add new elements in the ist
2. how to modify the elements in the list
3. how to delete the elements in the list


# In[ ]:


# i want to add satish name in the list


# In[8]:


students.append('satish')
print(students)


# In[ ]:


# i want to add shoaib name in the list


# In[11]:


students.append('shoaib')


# In[12]:


print(students)


# In[ ]:


# i want to add tanveer at 2nd index position


# In[13]:


students.insert(2,'tanveer')


# In[14]:


print(students)


# In[ ]:


what is the difference between append and insert in a list datatypes
ans : by using insert method we can add any element at our desired index but in append method we dont get the choice of it


# In[ ]:


# req : i want to modify khadija name to rubina


# In[16]:


students[0]='rubina'


# In[17]:


print(students)


# In[ ]:


# req : i want to delete anitha name form list


# In[18]:


del students[1]


# In[19]:


print(students)


# In[ ]:




