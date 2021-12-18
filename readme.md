## Super High Level Intro to Python as my tutorial guideline. 
If you like it, feel free to use.

`NoCoding is good code.`


### plz be noted, I recommend you install python version newer than 3.6 

Core advantage of python is how simple it is, how easy the syntax is to read, and just how fast the development is with it.

## Data Type

* int
* float
* string
    * 'hello'
    * "hello"
    * it does not matter it is single or double quotation mark 
* bool


## Output && Printing 
* `print("hello world")`
* `print("hello", "world", "how", end=" | | ")`
* by default, the end is `\n`

## Variable Naming convention
* camel style `thisMyVariable`
* snake style `this_my_variable`, python prefers this one


## User Input
* `input('name :' )`
* use a variable to store this info `name = input('name: ')`

## Arithmetic operator
* typically, you need same data type for arithmetic operation
* but, a special case: `string * int` will repeat this string
* `/` will always return a float number
* type casting. `a = int(b / c)`
* exponent `result = x ** y`, x power y
* ` result = x // y` simply remove all decimals and returns an int

## String method
* `print(type(hello))`
* 
    ```python
    hello = "hello".upper() 
    print(hello)
    ```
* `string.count()`, e.g. `hello.count('o')` this is case sensitive
* string concatenation `print(hello + world)`

* convert a char to int `ord('a')`
* convert an int to char `chr('15')`
* string.join(collection). here string is used as the separator. `','.join(list)`
* capitalize the first letter of a string
```python
def fixMessage(message):
    return message.capitalize()
```

* split a string into list
```python
s = "welcome to the jungle"
x = s.split()
print(x)

# you could specify the separator
txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)
```

* replace a letter in the string with another letter
```python
string.replace("letter", "b")
```

## if/elif/else 

```python
if x == 'hello' : 
    print("this is hello")
```


``` python
if x == 'hello' : 
    print("this is hello")
elif x == "world" :
    print("this is world")
else :
    print("no idea what it is")
```

## List && Tuples
* list, length is dynamic



```python
one_list = list('abc', 'efg') 
# list() is a list constructor

this_list = [1,2,3]
this_list.append(4)
print(this_list)
this_list.extent([4,5,6])
print(this_list)
x = this_list.pop() # remove and return the last element by default
print(x)

y= this_list.pop(2)
print(y)

print(this_list[0])

this_list[0]  = 67
print(this_list) # list is mutable 

# just copy the reference
second_list = this_list

# copy a list, rather than a reference
third_list = this_list
```

* tuple is immutable 
 ```python
 # in list or tuple, the elements do not need to be the same type, which ic required im some other language like java
first_tuple = (1,2,4, "hello", [1,2,3]) 
first_tuple[0] = 3 # error occurs
first_tuple.append(5) # error corrus

 ```


## for && while loop
* for loop

```python
for i in range(10)
    print(i)
    # range(start, stop, step)
    # start, step is optional
```
```python
for i in [1,2,3,4]
    print(i)
```
```python
x = [1,2,4,4,5]
for i, element in enumerate(x)
    print(i, element)
```
```python
x = [1,2,4,4,5]
for i in range(len(x))
    print(i)
```

* while loop
```python
while condition == true :
    execution 
    break # optional
```

## Slice Operator 

```python
x = [0,1,2,43,4,45]
y= "superWill"

sliced = x[:3]
sliced2 = x[1:]
sliced3 = x[::-1] # reverse a list
sliced4 = x[::2]

sliced = y[:3]
sliced2 = y[1:]
sliced3 = y[::-1] # reverse a list
sliced4 = y[::2]

# it works with tuple as well
sliced6 =  (1,2,4,4,5,6)[::-1]

# this slice operator can work with any collection basically
```

## Set && Dict
```python
# set is unsorted, containing unique elements
x = set() # this is an empty set

y = {}
print(type(y)) # you find this is a dict, rather than a set

# but you could create a set with this
s =  {2,3,4,4,4}

print(s)

# thus, if you want to craate an empty set, you need the set constructor set()
s.remove(4)
print(s)
print(4 in s) # running time of this is constant, compared with a list

s2 = {4,5,6,6,6,7}

print(s.union(s2))
print(s.difference(s2))
print(s.intersection(s2))

```

```python
x = {'key' : 4}
y = {'key' : [2,3,4]}
# for a dict, the value type is flexible
print(x['key'])
x['key2'] = 5
# the key type is flexible as well
x[2] = 8 # here 2 is not index, but a key
x[3] =  [4,5,6]

print(x)
# operations for a dict
print('key' in x)
print(x.values()) # fetch all values from a dict
print(list(x.values()))
print(list(x.keys()))
# to delete a key pair
del x[2]
print(x)
# iteration
for key, value in x.items() :
    print(key, value)

for key in x:
    print(x, x[key])

dict.get(key, value)
# if the key does not exist, then return this default value
# this is useful to initiate the first value
# e.g, track the frequency of letters in a string

x = 'abcdcefabcdabc'

letter_fre = {}

for letter in x:
    letter_fre[letter] = letter_free.get(letter, 0) + 1
    # if the letter does not exist in the dict, the get() return 0 and then plus one

```

## Comprehension
one line initiation of a list or a tuple, or a dict
```python
x = [x for x in range(5)]
# define a for loop in the list

x = [x+5 for x in range(5)]
x = [x %5 for x in range(5)]
x = [0 for x in range(5)]

y = [[1 for x in range(5)] for x in range(5)] 

m = [i for i range(100) if i % 5 ==0]
n = [i:1 for i range(100) if i % 5 ==0]
```

## function
```python
def func(x,y):
    print('go')
    return x+2, y+3

func(3,4)

m, n = func(4,5)
print(m, n)

# for a function in python, the execution block can not be empty, if for some reason, you are not sure what to put there, leave a 'pass' to avoid any error

def func2():
    pass
```

## *args && **kwargs
```python
# if you are not sure how many args you are going to have for a function, you could use *args a parameters. the function will fetch the element one by one accordingly

def func1(x, y):
    print(x, y)

test = [(1,2),(3,4)]

for pair in test:
    func1(*pair)


def func2(*args, **kwargs):
    print(args, kwargs)

func2(1,2,3,4,5, one=1, two=2)

```
## Exception

```python
raise Exception('test exception')

# this is a general exception
# you could specify one as you want

try:
    m = 7 / 0
except Exception as e:
    print(e)
finally:
    # will run eventually no matter what happen
    print('finally')
```
## Lambda function
one line anonymous function

```python
x = lambda x: x + 3
# this is not a suggested version to use it
print(x(2))
y = lambda x, y: x * y
print(x(2,3))

```
## Map && Filter
```python
x = [1,2,4,45,5,65,6,7,78,8]
mp = map(lambda i: i+2, x)
# this map() returns a map object
print(list(mp))

# map is used to change all elements
fl = filter(lambda i: i & 2 == 0, x)

print(list(fl))

def func(i):
    return i % 2 == 0
# filter is used to extract some elements meeting certain requirement
fl2 = filter(func, x)
print(fl2)

```

map(function, iterable) in python
a function could be a customized function or a built-in function
e.g.
```python
nums = [1,2,3,4,5,6,7]

nums_str = list(map(str, nums))

nums_len = list(map(len, nums_str))

# iterable, lets say, it could be a list, tuple, string, map, set..
# iterator, more like a pointer. the key feature is Moving and Fetching (NEXT) value
# map() return a map object, which is an iterator (a pointer representing a stream of data)

```


## F string

```python
# F or f is both ok
x = f'hello { 6+ 8}'
# f string support reference or functions, variables, via embedding them into {}
print(x)
```

## Class
```python
class node :
    def __init__(self, x, y):
        self.x = x
        self.y = y

# the init must be __init__, can not be _init_
def _private_metho (self, x):
    # a single leading underscore is generally used to mean "private method, please do not use"
    
```

## Tricky Points
* collection truth-ness
```python
xs = [()]
if xs:
    # check if the xs is empty
    print('a)
if xs[0]:
    print('b)
```

* comparison
```python
# check if x power (y) in the range of (L, R]
if L < x ** y <= R:

# get bit length of an int
a = 100
print(a.bit_length())

```
* Extended Iterable Unpacking
```python
a, *b, c = range(5)
print(a) # 0
print(b) #[1,2,3]
print(c) #4

# traditionally, in this way
first, rest = seq[0], seq[1:]
# now, in this way
first, *rest = seq

first, *rest, last = seq


```
