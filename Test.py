hello = 'tim'
world = 'world'
world = hello
hello = 'no'


# print(hello, world)

# s = {2,3,4,4,4,}

# print(s)

# y = {}

# print(type(y))

def func1 (*args):
    print(*args * 2)

func1(1,2,3,4,5)

x = (4,5,6,6,7)

func1(x)