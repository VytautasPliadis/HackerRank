'''
Counter: The Counter class is used to count the occurrences of elements in a collection (usually a list or a string)
 and store them in a dictionary-like object. It's particularly useful when you need to count the frequency of items in
 a collection.
'''
from collections import Counter

# Count the occurrences of elements in a list
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count = Counter(my_list)

# Access the counts
print(count[3])  # Prints 3

'''
defaultdict: The defaultdict class is a dictionary subclass that provides default values for missing keys. 
It's helpful when you want to avoid key errors when working with dictionaries.
'''
from collections import defaultdict

# Create a defaultdict with a default value of 0
my_dict = defaultdict(int)
my_dict['a'] += 1  # No KeyError, initializes to 0

print(my_dict)

'''
namedtuple: The namedtuple function creates a simple, memory-efficient class-like structure with named fields. 
It's useful for creating lightweight classes to represent data records.
'''
from collections import namedtuple

# Define a named tuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 22)

# Access fields by name
print(p.x, p.y)

'''
deque: The deque (short for "double-ended queue") is a double-ended queue data structure that allows efficient appending 
and popping elements from both ends. It's especially useful for implementing queues and stacks.
'''
from collections import deque

# Create a deque
my_deque = deque([1, 2, 3])

# Append and pop elements from both ends
my_deque.append(4)
my_deque.appendleft(0)
my_deque.pop()
my_deque.popleft()

print(my_deque)

'''
OrderedDict: The OrderedDict is a dictionary subclass that maintains the order of items based on their insertion order.
It's useful when you need to preserve the order of keys in your dictionary.
'''
from collections import OrderedDict

# Create an ordered dictionary
my_dict = OrderedDict()
my_dict['c'] = 4
my_dict['b'] = 2
my_dict['a'] = 1

# Dictionary maintains the order of insertion
for key, value in my_dict.items():
    print(key, value)