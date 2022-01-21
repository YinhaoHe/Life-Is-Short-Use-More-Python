# Life-Is-Short-Use-More-Python
Some interesting things about Python! 

## Python

- Python is by default CPython, there are also Jython...
- Same as Java, when executing Python, it first translate Python code into **Python ByteCode**, then **Python Virtual Machine** will translate ByteCode to machine code(0101001). So Python can run across different platform(OS).. 
- **Jython** is implemented with Java on low level. So you can **import Java code into Jython**, because those code will end up being translated to **Java ByteCode**, then **JVM** translates ByteCode to machine code..
- **Dynamic type** language similiar to JavaScript and Ruby
- **Integer** in Python is **Immutable**
- **list** in Python is **mutable**

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
