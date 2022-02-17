# Life-Is-Short-Use-More-Python
Some interesting things about Python! 

## Python

- Python is by default CPython, there are also Jython...
- Same as Java, when executing Python, it first translate Python code into **Python ByteCode**, then **Python Virtual Machine** will translate ByteCode to machine code(0101001). So Python can run across different platform(OS).. 
- **Jython** is implemented with Java on low level. So you can **import Java code into Jython**, because those code will end up being translated to **Java ByteCode**, then **JVM** translates ByteCode to machine code..
- **Dynamic type** language similiar to JavaScript and Ruby
- **Integer** in Python is **Immutable**
- **list** in Python is **mutable**
- Everything in Python is **Object**.

### Variable:

```Python
# All lower case naming

students_count = 1000
rating = 4.99
is_published = False
course_name = """
Multiple
Lines
"""

x, y = 1, 2
x = y = 1
```

Mutable and Immutable Types:

- `id()` - this function can give you the memory ID of this variable
- Integer/String - immutable
- List - mutable

### String:

- `len()` - give you the length of string/list
- Python allows use **negative index**
- Use index to slice string [0:3] - return string from index 0 to 2, excluding the index 3

```Python
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-2])
print(course[0:3])
print(course[:3])
print(course[0:])

# Output
'''
18
P
n
Pyt
Pyt
Python Programming
'''
```

### Escape Sequences:

- 转义符

```python
# \" ----- "
# \' ----- '
# \\ ----- \
# \n ----- 回车

message = "Python \"Programming"
print(message)

# Python "Programming
```

### Formatted string

- Add `f` before the string to format it.

```Python
formatted_string = f"{len(a)} {2 + 2}"

year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
# 'Results of the 2016 Referendum'
```

### Useful String Methods:

- `upper()`
- `lower()`
- `title()`
- `strip()`
- `find()`
- `replace()`
- `print("Programming" in course)`
- `print("Programming" not in course)`

###  Number:

```Python
x = 10

x = 0b10
print(bin(x)) # 按照二进制print

x = 0x12c
print(hex(x)) # 按照16进制print

# a + bi
x = 1 + 2j
print(x)

###########
0b10
0x12c
(1+2j)
```

### Arithmetic Operators:

- There is no `++` or `--` in Python

```python
x = 10 + 3
x = 10 - 3
x = 10 * 3
x = 10 / 3 # 得到floating number
x = 10 // 3 # 得到Integer number
x = 10 % 3 
x = 10 ** 3 # 10 的 三次方

x = x + 1
x += 1

print(x)
```

### Types:

- Python has no **constant** 
- Mark variable as capital letters to make it a constant
- `import math` Many useful modules in `math`

```python
import math

PI = 3.14
print(round(PI))
print(abs(PI))
print(math.floor(PI)) 
```

- Python is a strong-typed language, so it doesn't implicitly decide type for user
- However, JavaScript is a weak-typed language, so it can implicitly decide types

Example below:

```Python
x = input("x: ")
y = x + 1
```

In this case, when user input` 1`, Python will give an error since it doesn't know `x + 1` should be a string `"11"` or a number `2`.

- Built-in type function:

  ```Python
  int()
  float()
  bool()
  str()
  ```

- Python has a concept like JavaScript, it has Truly and Falsy values

- Falsy: `""` `0` `[]` `None`, when you convert them to `bool()`it will become `false`

- Trusy: Anything else exclude the above ones

### Conditional Statements

- **Indentation** to specify a code block.
- **Do NOT** mix 4 spaces with Tab, this is **NOT** allowed in Python3

```Python
age = 22
if age >= 18:
  	print("Adult")
elif age >= 13:
  	print("Teens")
else:
  	pass

print("Done")
```

- Can use `pass` keyword to imply this is an empty block.

### Logical Operators

- `not` 

- ```Python
  name = ""
  if not name:
    print("bla")
  ```

- `and` 

- ```Python
  age = 22
  if age >= 18 and age < 65:
    print("bla")
    
  # age >= 18 and age < 65 equal to below
  18 <= age < 65
  ```

- `18 <= age < 65` is called **chaining comparsion operators**

### Ternary Operator

- In Java/JavaScript/C/C#, `message = age >= 18 ? "Good" : "Bad"`

- In Python: 

- ```python
  message = "Good" if age >= 18 else "Bad"
  ```

### For Loops

- Python only has two type of loops: `for` and `while`

- `for` and loop any object that is iterable. 

- ```python
  for x in "Python":
    print(x)
  
  for x in ['a', 'b', 'c']:
    print(x)
  
  # 从 0 开始走到 9 ，一次走两步
  # 0 2 4 6 8
  for x in range(0, 10, 2):
    print(x)
  ```

- ```python
  print(range(5))
  
  # range(0, 5)
  ```

- Above is because there is a **range** object.

- `type(range(5))` is `<class 'range'>` this is a instance of range class.

- range object is iterable, and only take a small portion of memory.

### For Else

- If for loop completes without hitting the `break`, Python will excute the `else` below the for loop.

```python
names = ["John", "Mary"]
for name in names:
  if name.startswith("J"):
    print("Found")
    break
else:
  	print("Not found")
```

### While Loops

```python
while answer != guess:
  	guess = int(input("Guess: "))
else:
  	pass
```

- Same as for loop, it while loop completes without hitting any `break`, `else` gets excicuted.

### Functions

- To call a function under definition, we should always leave two lines blank.
- We can return multiple values in Python `return (number, number + by)`
- Even if no code in `increment()`, when print, it will print `None`

```python
def increment(number, by):
  	return (number, number + by)
  
  
print(increment(2, 3))
```

- `return (number, number + by)` is a **Tuple**
- To make a list `[1, 2]`, to make a tuple `(1, 2)`
- Keyword argument: `print(increment(2, by = 3))`
- Function can set default value: `def increment(number, by=1)`, so you can call `increment(2)` with only one parameter.
- Type annotation: `def increment(number: int, by: int = 1) -> tuple`
- Type annotation can specify the type of every parameter, and the return value of the function

```python
def increment(number: int, by: int=1) -> tuple:
  	return (number, number + by)
  
  
print(increment(2))
```

### Arguments xargs asterisk - 星号`*`

- When add `*` before a parameter, Python will package the parameter into a Tuple.

```python
def multiply(*list):
  	# print(list)
    total = 1
    for number in list:
      	total *= number
    return total
    
multiply(2, 3, 4, 5)

# list will be auto packed into a Tuple
```

### Arguments xxargs asterisk - 两个星号`**`

- When add two `**` before a parameter, Python will package the **keyword arguments** into **Dictionary**

```python
def save_user(**user):
  	print(user)
    print(user["id"])
    print(user["name"])
    
    
save_user(id=1, name="admin")

# {'id': 1, 'name': 'admin'}
```

- It is similar to **Object** in JavaScript

### Scope

- Local variable: Python don't have block scope, if the variable is defined in this function, it can always be access within this function. 

- ```python
  def greet():
    	if True:
        	message = "a"
      print(message)
      
  # This is legal, since message is in function greet()
  ```

- Global variable: If global variable, it can be accessed anywhere in this **file.**

- ```python
  message = "a"
  
  def greet():
    	message = "b"
      print(message) # Get b, since this will create a local variable also called message, inside this function.
  
      
  greet()
  print(message) # Still print a, since global variable is not allowed to be changed inside of a function
  ```

- But if you add `global message` before `message = "b"`, it will allow you to change value for global variable.

- Make sure **NEVER DO THAT**. Global variables are EVIL.

### Debugging

- VS Code - Go to debug panel, create a launch.json
- F9 - Add break point
- F5 - Start debugging session
- F10 - Step over one line
- F11 - Step into a function
- Shift + F11 - Step out of a function

## Python Data Structures

### List

- List, can put any type into a list in Python, list of strings/lists anything
- `*` can be used to replicate the elements in the list
- `+` can be used to concat the lists
- `list()` is a function which takes a iterable as argument, so we can pass in a iterable to create list

Some examples:

```python
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World") # Since String in Python is also iterable
```

### Accessing Items

- `letters[0]` - access the first element counting from begin
- `letters[-1]` - access the first element counting from behind

Slice list will create a new list, will **NOT** make change to the original list

- `letters[0:3]` equals `letters[:3]` - slice first three elements
- `letters[0:]` - slice from index 0 to end of list
- `letters[:]` -  copy a new list, is **NOT** a reference to old list
- `letters[::2]` - copy list every two steps
  - Example: `letters = ["a", "b", "c", "d"]`
  - `new_letters = letter[::2]`
  - `print(new_letters)` - `["a", "c"]`

- `letters[::-1]` - create a reverse order list
  - Example: `numbers = [1, 2, 3]`
  - `new_numbers = numbers[::-1]`
  - `print(new_numbers)` - `[3, 2, 1]`

### List Unpacking

- To assign variables to every element in a list is called list unpacking
- To unpack the list, need to assign same amount of variables to the number of elements in the list

```python
numbers = [1, 2, 3]
first, second, third = numbers

# first = 1
# second = 2
# third = 3
```

- **Or**, you can assign any number of varibles and follow with a `*other`, the `*other` will pack anything else into a new list, example below

```python
many_numbers = [1, 2, 3, 4, 4, 4, 4, 4, 4]
first, second, *other = many_numbers

# first = 1
# second = 2
# other = [3, 4, 4, 4, 4, 4, 4]
```

- Same thing, if you want to get the **first and last** item, just do:

```python
many_numbers = [1, 2, 3, 4, 4, 4, 4, 4, 9]
first, *other, last = many_numbers

# first = 1
# other = [2, 3, 4, 4, 4, 4, 4,]
# last = 9
```

### Looping Over List

- Loop elements:

- ```python
  letters = ["a", "b", "c"]
  for letter in letters:
    	print(letter)
  ```

- Loop index plus elements:

- `enumerate()` - function will return a enumerate object, which is iterable - It is a Tuple

- ```python
  letters = ["a", "b", "c"]
  for index, letter in enumerate(letters):
    	print(index, letter)
  ```

- Can unpack the elements in the `enumerate` object (Tuple) to loop, example above

### Adding or Removing Items

- `append()` - add from behind
-  `insert(0, "-")` - insert at index 0
-  `pop()` - remove from behind
-  `pop(0)` - remove index 0 item
-  `remove("b")` - will **remove the first occurance** of letter "b"
  - If you want to remove all "b" in the list, have to loop through it, no better way
-  `del letters[0:3]`  - will remove first three items in the list
-  `clear()` method will remove all items in the list

### Finding Items

- `index("a")` - find index of item "a", if not exist, get an error
- `in` - determine if items in a list
  -  `if "d" in letters` - determine if "d" is in the list, to prevent errors
- `count("d")` - count number of "d" in list

### Sorting Lists

- `numbers.sort()` - sort original list, default ascending order
- `numbers.sort(reverse=True)` - sort descending order
- `sorted(numbers)` - sort and **return a new list**, will not affect original list

```python
numbers = [3, 51, 2, 8, 6]
numbers.sort()
numbers.sort(reverse=True)

new_numbers = sorted(numbers)
new_numbers_reverse = sorted(numbers, reverse=True)
```

- A more complex sorting, like sorting a complex object:

```python
items = [
  	("Product1", 10),
	  ("Product1", 9),
	  ("Product1", 12),
]

def sort_item(item):
  	return item[1]

items.sort(key= sort_item)
print(items)
```

### Lambda Functions

- A simple one line anonymous function that we can pass to other functions.
- **anonymous function**

```python
items = [
  	("Product1", 10),
	  ("Product1", 9),
	  ("Product1", 12),
]

items.sort(key=lambda item:item[1])
```

### Map Function

- Used for mapping elements into different shapes
- `map()` function returns a map object, which is iterable
- Can call `list(map(...))` to make it a list
- Often used for functional programming

```python
items = [
  	("Product1", 10),
	  ("Product1", 9),
	  ("Product1", 12),
]

price_list = list(map(lambda item : item[1], items))
print(price_list)
```

### Filter Function

- `filter()` filter out the values based on some criteria
- Often used for functional programming
- Only works with single list

```python
items = [
  	("Product1", 10),
	  ("Product1", 9),
	  ("Product1", 12),
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
```

### List Comprehensions

- `[expression for item in items]`
- A unique way of `map()` and `filter()` only works in Python
- Only works with single list

```python
items = [
  	("Product1", 10),
	  ("Product1", 9),
	  ("Product1", 12),
]

price_list = list(map(lambda item : item[1], items))
filtered = list(filter(lambda item: item[1] >= 10, items))
```

- Above equals below, and it is preferable to use below in Python

```python
price_list = [item[1] for item in items]
filtered = [item for item in items if item[1] >= 10]
```

### Zip Funtion

- `zip()` works with multiple lists
- `zip()` can take many iterables as perameter, you can even put a string into a `zip()` function
- `zip("abc", list1, list2)`

```python
list1 = [1 ,2, 3]
list2 = [10, 20, 30]

list(zip(list1, list2))

# [(1, 10), (2, 20), (3, 30)]
```

### Stacks

- `python_stack = []` nothing special, can use list to implement stack
- `python_stack.append()` - to add into stack
- `python_stack.pop()` - pop the top of stack
- `python_stack[-1]` - access the top of stack

### Queues

- Cannot use list to implement queues, since move from begining of a list will cause every element in the queue to move one postion forward, very expensive
- Use `deque`
- `queue.append(1)` - add to queue from back
- `queue.popleft()` - pop from beginning/left from the queue

```python
from collections import deque
queue = deque([])
queue.append(1)
queue.popleft()
```

### Tuples

- A read only list - **cannot** modify it at all
- `point = (1, 2)` or `point = 1, 2` both work
- `point = (1, 2) + (3, 4)` can add two tuples
- `point = (1, 2) * 3` can multiply tuples
- `point = tuple([1, 2])` can convert a list to a tuple 
- `tuple()` takes in a iterable
- `point[0:2]` can return first two as a NEW tuple
- `x, y, z = point` can unpack a tuple
- `if 10 in point` can use `in` operator to a tuple
- CANNOT `point[0] = 10` it is immutable
- Used for when you don't want to accidentally change or add a new value to a list, you can use tuple instead - like `const` in JavaScript

### Swapping Variables

- In Python, can use tuple and unpacking to swap it without defining a third variable

```python
x = 10
y = 11

x, y = y, x
# Successfully swap x and y
```

- Under the hood, `x, y = y, x` 
- Right side: `y, x ` is actually defining a tuple, so it equals `x, y = (y, x)`, but you can simplify that but removing the `()`
- Left side: `x, y` is actually unpacking the tuple on its right, so actually `x, y = (11, 10)` just unpack the tuple
- Both together, we can swap value without creating a third variable

### Arrays

- array is a little little little bit faster than list.
- `array()` - takes a Python **Typecode** and a list as parameters

```python
from array import array

numbers = array("i", [1, 2, 3])
numbers.append(4)
numbers.insert(0)
numbers.pop()
numbers.remove(2)
numbers[0]
```

- But unlike list, everything in the array is **typed**, so everything should be same type
- DO NOT USE THIS VERY OFTEN, if no performance issue, skip and only use list

### Sets

- Contains non-duplicate elements

```python
numbers = [1, 2, 3, 3, 3, 4]
first = set(numbers)
second = {1, 4} # Define a set
second.add(5)
second.remove(5)
len(second)

# Cool ones
first | second # get a union
first & second # get a intersaction
first - second # difference
first ^ second # Symetric difference
```

- Get a union `first | second`
- Get a intersaction `first & second` 
- Get a difference `first - second`
- Symetric difference `first ^ second` - either in first or second but not in both
- Unordered, cannot access using index
- `if 1 in first` - can use `in ` to check if exists in set

### Dictionaries

- Define `point = {"x": 1, "y": 2}`

- `dict(x=1, y=2)` parameters are called **keyword arguments**

- Key must be immutable type, like string or numbers

- Values can be any type

- `point["x"]` get the value of x

- `point["x"] = 10` change a value

- `point["z"] = 20` add a value

- Invalid key will get an error, `point["a"]` - get KeyError

- `if "a" in point` - check "a" in dict

- `point.get("a")` - get key "a" associated value, if not exists, return None

- Get or default `point.get("a", 0)` - if "a" exist, return value or return 0

- `del point["x"]` remove a key/value

- loop over dict

  - ```python
    for key in point:
    		print(key, point[key])
    ```

  - ```python
    for key, value in point.items():
    		print(key, value)
    ```

### Dictionary Comprehensions

- List comprehensions

```python
values = []
for x in range(5):
  	values.append(x * 2)
    
# Same as
a_list = [x * 2 for x in range(5)]
```

- Set comprehensions

```python
a_set = {x * 2 for x in range(5)}
```

- Dict comprehensions:

```python
a_dict = {x: x * 2 for x in range(5)}

# {0: 0, 1: 2, 2: 4}
```

- For tuple

```python
values = (x * 2 for x in range(5))

# get a generator object, not getting a tuple
```

### Generator Expressions

- A generator object do NOT store all values in the memory
- Good for dealing with large data or data stream

```python
values = (x * 2 for x in range(5))
for x in values:
  	print x

# It works
# But values is NOT a list
# It is a Generator Object
```

- generator object is **very small** - `from sys import getsizeof` - can check the memory size
- Cannot know how many items in the generator object, it has no `len()`

### Unpacking Operator

- `*` is the unpacking operator

- It can unpack any iterables `values = [*range(5), *"Hello"]`

- Only works in Python

- Can combine many lists

  - ```python
    first = [1, 2]
    second = [3, 4]
    values = [*first, "a", *second, *"Hello"]
    ```

- Unpack a Dict use `**` operator

  - ```python
    first = {"x": 1}
    second = {"x": 10, "y": 2}
    combined = {**first, **second, "z": 1}
    
    # {'x': 10, 'y': 2, 'z': 1}
    # When same key value, it will unpack and save as the last value
    ```

  - When key values same, will leave it as the last one
