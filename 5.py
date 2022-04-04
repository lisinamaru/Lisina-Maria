#!/usr/bin/env python
# coding: utf-8

# In[8]:


row = "1234"

print(row[::2])


# In[7]:


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
b = 1
while b != len(a):
    if a[b] > a[b - 1]:
        print(a[b], end=' ')
    b += 1


# In[13]:


s=[3,4, 5, 2, 1]

max_var=s.index(max(s))
min_var=s.index(min(s))

s[max_var],s[min_var]=s[min_var],s[max_var]

print (s)


# In[ ]:




