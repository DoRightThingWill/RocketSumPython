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








