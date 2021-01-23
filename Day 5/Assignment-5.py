#!/usr/bin/env python
# coding: utf-8

# # Question 2
# # Implement selection sort algorithm using Python.

# In[2]:


import random


def selectionSort(mylist):
    for i in range(len(mylist)-1):
        min_index = i

        for j in range(i+1, len(mylist)):
            if mylist[j] < mylist[min_index]:
                min_index = j

        mylist[i], mylist[min_index] = mylist[min_index], mylist[i]

mylist = [random.randint(1,100) for i in range(10)]

print("Original List:", mylist)

selectionSort(mylist)

print("Sorted List:", mylist)


# # Question 3
# # Implement pop operation of the stack

# In[3]:


def push(stack, data):
    stack.append(data)

def pop(stack):
    if stack == []:
        return "Underflow - Empty Stack"

    return stack.pop()

def display(stack):
    if stack == []:
        print("Underflow - Empty Stack")
        return

    for i in range(-1, -len(stack)-1, -1):
        print(stack[i])

    print()

stack = []

push(stack, 1)
push(stack, 10)
push(stack, 100)

display(stack)

print(pop(stack))
print(pop(stack))
print(pop(stack))
print(pop(stack))


# # Question 4
# # Implement dequeue operation of the queue

# In[4]:


def enqueue(queue, data):
    queue.append(data)

def dequeue(queue):
    if queue == []:
        return "Underflow - Empty Queue"

    return queue.pop(0)

def display(queue):
    if queue == []:
        print("Underflow - Empty Queue")
        return

    for i in queue:
        print(i, " => ", sep="", end="")

    print()

queue = []

enqueue(queue, 1)
enqueue(queue, 10)
enqueue(queue, 100)


display(queue)

print(dequeue(queue))
print(dequeue(queue))
print(dequeue(queue))
print(dequeue(queue))


# In[ ]:




