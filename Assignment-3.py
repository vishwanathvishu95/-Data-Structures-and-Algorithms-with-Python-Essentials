#!/usr/bin/env python
# coding: utf-8

# # Question 1
# # Write a Python program to add two numbers using class and object.
# # (Take both numbers as input from the user)

# In[1]:


class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def float_divide(self):
        return self.a / self.b

    def floor_divide(self):
        return self.a // self.b

    def display(self):
        print(f"a={self.a}, b={self.b}")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

ob = calculator(a, b)

ob.display()

print("Sum:", ob.add())
print("Difference:", ob.sub())
print("Product:", ob.multiply())
print("Float Division:", ob.float_divide())
print("Floor Division:", ob.floor_divide())


# # Question 2
# # Define a function swap that should swap two values and print the swapped variables outside the swap function.

# In[2]:


def swap():
    global a
    global b

    a, b = b, a
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Original values:")
print(f"a={a}, b={b}")

swap()

print("Swapped values:")
print(f"a={a}, b={b}")


# In[ ]:




