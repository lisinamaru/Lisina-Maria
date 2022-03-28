#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=True
b=False

R=(a*b)+(-1)*(a*b)

print(R)
0
a=True
b=False

R=(a*b)

print(R)
0
a=True
b=False

R=(a*b)+b

print(R)
0
a=True
b=False

R=a*b+(-1)*(a+b)+b

print(R)
-1
a=True
b=False

R=b*b+(-1)*a*(a+b+a)+(-1)*(a+b)

print(R)
-3
a=True
b=False

R=a<<b

print(R)
1
a=True
b=False

R=a&b|a>>a

print(R)
0
a=True
b=False

R=a&b | a >> b

print(R)
1
a=True
b=False

R=0b101 & 0b111 ^ 0b111 | 0b010

print(R)
2

