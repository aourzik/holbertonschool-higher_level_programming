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

print(id(a))
print(type(b))
```

### Mutable Objects
Mutable objects are those whose content can be changed after creation without changing their identity. Common examples include list, dict, and set. When you modify a list, you are changing the object in place, meaning the memory address remains the same despite the data inside being altered.

```python
my_list = [1, 2]
print(id(my_list))
my_list.append(3)
print(my_list)
print(id(my_list))
```

### Immutable Objects
Immutable objects cannot be modified once created. These include **int**, **float**, **string**, **tuple**, and **frozenset**. If you attempt to "change" an immutable object, Python does not modify the original; instead, it creates a brand-new object with a new identity (a different memory address).

```python
s = "Hello"
print(id(s))
s = s + " World"
print(id(s))
```

### Why it Matters: Python's Treatment of Objects
The distinction matters because of performance and memory management. Python optimizes memory by using a technique called "interning" for small integers and strings (pointing multiple variables to the same memory address). However, with mutable objects, Python must be careful; if two variables point to the same list, changing one affects the other, which can lead to unexpected side effects and logical bugs.

### Function Arguments: Pass-by-Assignment
Python uses a mechanism called "pass-by-assignment." When you pass an argument to a function, the function receives a reference to the object. For Immutable objects, since they can't change, the original value is safe; modifying it inside the function just reassigns a local name to a new object. For Mutable objects, the function can modify the object in place, and those changes will persist outside the function.

```python
def update_list(l):
    l.append(4)

my_list = [1, 2, 3]
update_list(my_list)
print(my_list)
```

### Advanced Insights (Integer Pre-allocation)
During my deep dive, I learned that CPython (the standard Python implementation) pre-allocates an array of integers from -5 to 256 at startup. This means that any variable assigned within this range actually points to the same pre-existing memory location. This optimization trick avoids the overhead of creating new objects for the most commonly used numbers in coding.