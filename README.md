# Life-Is-Short-Use-More-Python
Some interesting things about Python! 

## Python

- Python is by default CPython, there are also Jython...
- Same as Java, when executing Python, it first translate Python code into **Python ByteCode**, then **Python Virtual Machine** will translate ByteCode to machine code(0101001). So Python can run across different platform(OS).. 
- **Jython** is implemented with Java on low level. So you can **import Java code into Jython**, because those code will end up being translated to **Java ByteCode**, then **JVM** translates ByteCode to machine code..
- **Dynamic type** language similiar to JavaScript and Ruby
- **Integer** in Python is **Immutable**
- **list** in Python is **mutable**

Variable:

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

String:

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

Escape Sequences:

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

Formatted string

- Add `f` before the string to format it.

```Python
formatted_string = f"{len(a)} {2 + 2}"
```

Useful String Methods:

- `upper()`
- `lower()`
- `title()`
- `strip()`
- `find()`
- `replace()`
- `print("Programming" in course)`
- `print("Programming" not in course)`

 Number:

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

Arithmetic Operators:

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

Type Conversion:

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

 
