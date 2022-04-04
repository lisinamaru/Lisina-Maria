#!/usr/bin/env python
# coding: utf-8

# In[14]:


friends = [{'name': 'Маи', 'year': 1930, 'city': 'Москва'}]

def name():
    name = []
    for name_friend in friends:
        name.append(name_friend['name'])
    return name 

def year():
    age = []
    for age_friend in friends:
        age.append(age_friend['year'])
    return age

def city():
    city = []
    for city_friend in friends:
        city.append(city_friend['city'])
    return city

def print_friend(name, year, city):
    for i in range(len(name)):
        print(name[i], year[i], city[i])

print_friend(name(), year(), city())


# In[ ]:




