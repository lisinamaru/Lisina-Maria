#!/usr/bin/env python
# coding: utf-8

# In[9]:


"решено так же понятно, как написана первая задача"

import itertools
from functools import reduce
 
p = [0.4, 1.0, 0.5]
 
q = [1 - i for i in p]
print(reduce(lambda a, b: a * b, q))
 
a = range(len(p))
 
for i in range(1, len(p)):
    c = list(itertools.combinations(a, i))
    s = []
    for j in c:
        t = p[:]
        for k in j:
            t[k] = 1 - t[k]
        t = [1 - i for i in t]
        s.append(reduce(lambda a, b: a * b, t))
    print(sum(s))
 
print(reduce(lambda a, b: a * b, p))


# In[ ]:




