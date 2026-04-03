# Project: Python - Mutable, Immutable objects

## Technical Blog Post

*The following content is the blog post written to explain the mechanics of Python objects.*

---

# Python Objects: The Hidden Logic of Mutability

![Python Programming](https://images.unsplash.com/photo-1515879218367-8466d910aaa4?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80)

### Introduction
In Python, the phrase "everything is an object" is a fundamental truth. From simple integers to complex data structures, Python treats every piece of data as an object. Understanding how these objects are identified, typed, and manipulated in memory is crucial for any developer aiming to write efficient and bug-free code. This post dives into the core mechanics of Python's object model, focusing on the pivotal distinction between mutable and immutable objects.

### ID and Type
Every object in Python is assigned a unique **ID** and a **Type** upon creation. The `id()` function returns the memory address of the object, acting as a unique identifier for its lifetime. The `type()` function reveals the class of the object. These two properties define "who" the object is and "what" it can do.

```python
a = "Holberton"
b = [1, 2, 3]

print(id(a))    # Output: 140523824563392 (Example address)
print(type(b))  # Output: <class 'list'>
