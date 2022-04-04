#!/usr/bin/env python
# coding: utf-8

# In[3]:


numbers = [1, 2, 3, 4, 5,6,7,8,9,10]
s = 0
for number in numbers:
    s += number
print(s)


# In[15]:


n = 5

for i in range(n):
    print(''.join(map(str, range(1, i+2))))


# In[1]:


num_zeroes = 0
for i in range(int(input())):
    if int(input()) == 0:
        num_zeroes += 1
print(num_zeroes)


# In[2]:


n = int(input()) + 1
for i in range(1, n + n + 2):
    if i <= n:
        print(' ' * (n - i), end='')
        print(*range(1, i), *range(1, i - 1)[::-1], sep='')
    else:
        print(' ' * (i - n), end='')
        print(*range(1, n + n - i), *range(1, n + n - i - 1)[::-1], sep='')


# In[ ]:





# In[ ]:




