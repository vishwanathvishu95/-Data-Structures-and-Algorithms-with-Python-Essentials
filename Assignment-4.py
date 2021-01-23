#!/usr/bin/env python
# coding: utf-8

# # Question 1
# # Implement deletion operation from the end of the linked list and Insertion operation from the beginning of the linked list
# 

# In[1]:


class Node:

    def __init__(self, data=0):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        new = Node(data)
        
        if self.head == None:
            self.head = new
        else:

            current = self.head

            while current.next != None:
                current = current.next

            current.next = new

    def deleteEnd(self):
        current = self.head
        prev = self.head

        while current.next != None:
            prev = current
            current = current.next

        prev.next = None

    def display(self):
        current = self.head

        while current != None:
            print(current.data, end="=>")
            current = current.next

        print()

mylist = LinkedList()

mylist.insertEnd(10)
mylist.insertEnd(20)
mylist.insertEnd(30)
mylist.insertEnd(40)
mylist.insertEnd(50)

mylist.display()

mylist.deleteEnd()

mylist.display()


# # Question 2
# # Implement binary search using python language.
# # (Write a function which returns the index of x in given array arr if present, else returns -1)

# In[2]:


import random

def binarySearch(nums, key):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left+right) // 2

        if key == nums[mid]:
            return mid
        elif key > nums[mid]:
            left = mid + 1
        else: 
            right = mid - 1

    return -1

nums = [10,20,30,40,50,60,70,80,90,100]

key = int(input("Enter value to search: "))

result = binarySearch(nums, key)

if result == -1:
    print("Value not found")
else:
    print("Found at", result+1)


# In[3]:


import random

def binarySearch(nums, key):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left+right) // 2

        if key == nums[mid]:
            return mid
        elif key > nums[mid]:
            left = mid + 1
        else: 
            right = mid - 1

    return -1

nums = [10,20,30,40,50,60,70,80,90,100]

key = int(input("Enter value to search: "))

result = binarySearch(nums, key)

if result == -1:
    print("Value not found")
else:
    print("Found at", result+1)


# # Question 3
# # Write a Python program to find the middle of a linked list.

# In[4]:


class Node:

    def __init__(self, data=0):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        new = Node(data)
        
        if self.head == None:
            self.head = new
        else:

            current = self.head

            while current.next != None:
                current = current.next

            current.next = new

    def middleNode(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        print("Middle Node:", slow.data)

    def display(self):
        current = self.head

        while current != None:
            print(current.data, end="=>")
            current = current.next

        print()

mylist = LinkedList()

mylist.insertEnd(10)
mylist.insertEnd(20)
mylist.insertEnd(30)
mylist.insertEnd(40)
mylist.insertEnd(50)

mylist.display()

mylist.middleNode()


# In[ ]:




