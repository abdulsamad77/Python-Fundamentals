#!/usr/bin/env python
# coding: utf-8

# In[ ]:


continuation with list datatype :


# In[ ]:


organising the list datatype :


# In[1]:


cars= ['suzuki','maruti','hyundai','benz','kia','audi','tata','bmw']
print(cars)


# In[ ]:


# req : i want to organise above list in alphabetical order :


# In[ ]:


Approach : 
    1 = temp approach ====> we will be able toget the original defined list order ==> sorted
    2 = permanent approach ===> changes will be applied permanently ==> sort


# In[2]:


print(sorted(cars))


# In[3]:


print(cars)


# In[5]:


cars.sort()


# In[6]:


print(cars)


# In[ ]:


# ques : what is the difference between sorted and sort method in list datatype ?


# In[ ]:


# req : i want to know no. of elemnt in the above list :


# In[7]:


len(cars)


# In[ ]:


# req : i want to reverse the order == Z to A


# In[8]:


print(cars)


# In[9]:


cars.reverse()


# In[10]:


print(cars)


# In[ ]:





# In[ ]:


introduction to slicing :


# In[11]:


students=['parvez','naveen','khadija','roja','kartik','joseph']
print(students)


# In[ ]:


# general syntax of slicing :
[start_value:stop_value:step_count]


# In[ ]:


Note : last value is always exclusive, to include it we have to increment the index by +1


# In[ ]:


# req : i want to get parvez and naveen in a slice


# In[12]:


print(students[0:1])


# In[13]:


print(students[0:2])


# In[ ]:


# req : i want to have khadija and roja in the slice


# In[14]:


print(students[2:4])


# In[ ]:


# req : i want to get kartik and joseph


# In[15]:


print(students[4:6])


# In[16]:


print(students[0:6:2])


# In[ ]:


# ==> it is use for commenting the code


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




