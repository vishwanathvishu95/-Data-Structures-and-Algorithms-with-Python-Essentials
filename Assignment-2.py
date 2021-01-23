#!/usr/bin/env python
# coding: utf-8

# # Question 1
# # Write a Python program to print even numbers in a list.
# # Sample:
# # Input: list1 = [12, 3, 55, 6, 144]
# # Output: [12, 6, 144]
# # Input: list2 = [2, 10, 9, 37]
# # Output: [2, 10]

# In[2]:


list1= [12, 3, 55, 6, 144]

print([i for i in list1 if i%2==0])


# In[3]:


list2= [2,10,9,37]

print([i for i in list2 if i%2==0])


# # Question 2
# # Write a program to print the following pattern
# #          1
# #        22
# #      333
# #    4444
# #  55555

# In[5]:


a= 5

for i in range(1,a+1):
    print((a-i) * " " , str(i) * i)


# In[ ]:




