#!/usr/bin/env python
# coding: utf-8

# In[1]:


Задача про самолеты
def factorial(n):
    if n == 1: return 1
    else: return n * factorial(n-1)
factorial(5)/factorial(5-3)


# In[2]:


Задача про Пауля
import random
k=0
results=[2, 1, 1, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1]
#Результаты матчей по условию задачи величины реальные, так что считаю их заранее известными#
def prognoz(n):
    data = []
    while len(data) <n:
        data.append(random.randint(1,2))
    return data
prognoz_data=prognoz(16)
#Рандомно заполняет список 16-тью значениями-предсказаниями#
for j in range(0,100):
    for i in range(0,15):
        if results[i]==prognoz_data[i]:
            k+=1
    print(j,k)
    k=0
    prognoz_data=prognoz(16)


# In[4]:


1
2
3
5
6
7
8
9
10
2
3
4
5
6
7
8
9
8
7
6
5
4
3
8
10
9
8
7
6
4
3
6
5
8
8
6
6
8
9
9
9
8
7
6
5
4
3
8
10
9
8
7
6
4
3
6
5
8
8
6
6
8
9
9
10
9
8
7
6
4
3
6
5
8
8
6
6
8
9
9
8
9
6
5
6
7
8
5
6
6
7
7
8
7
6
2
10
1


# In[ ]:


"Нет соотсвествия с условиями задачи. Гипотеза не доказано"

