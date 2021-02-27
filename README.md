# LinkedList
This is a module I've written to simulate a Python list that's truly a linked list internally. I've written it mainly as a learning experience.
It's my first time writing test cases at all and I got no influence from online resources with the exception of the `reverse` method. I've tried
to make some performance optimizations despite the module being written in Python. Suggestions are welcome!

## Usage
You can expect the list to mainly behave like a Python list:
```py
from linkedlist import LinkedList

# Passing iterables on initiation creates a list with the values inside
my_list = LinkedList([1,2,3,4])
my_list.extend(range(3))

for val in my_list:
  print(val)
  
 list_copy = my_list.copy()
 
if my_list[2] == 3:
  print("Values are equivalent!")
```

Every list method [here](https://www.w3schools.com/python/python_ref_list.asp) is supported (please report any bugs!)
