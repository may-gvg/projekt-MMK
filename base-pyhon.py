# ASCI CODE

print(ord('a')) # 97

print(ord('z')) # 122



print('ab' < 'ad')


# Collections
# List 
x = [4, True, 'hi']
x.append('hello')
x.extend([1, 2, 3, 4])
x.pop()
x.pop(0)

# Topal / cannot be changed
x = (0, 0, 2, 4, 8)

# Dictionary
x = {'asd': 3, 'sdf': 4}


# Slice operator 
# x[start:stop:step]
x = [1, 2, 3, 4, 4]
print(x[0: :2])
# reverse a list
x[::-1]


# Comprehensions

x = [x for x in range(5)]
print(x)

x = [[0 for x in range(100)] for x in range(5)]
print(x)

x = [i for i in range(101) if i % 5 == 0]
print(x)

# Unpack operaator / *args and **kwargs

x = [1, 23, 456, 5678]
print(x) # print normal list x
print(*x) # unpack list x

# *args - list
# **kwargs - dictionary



# Scope and global and local

x  = 'Tim' # - global

def func(name): # - scope
    x = name # - local

# Exceptions
def error():
    raise Exception('Bad')

# Handling Exceptions
def exceptions():
    try: 
        x = 7 / 0 
    except Exception as e:
        print(e)
    finally:
        print('finally')


# Lambda

x = lambda x: x + 5 # take x and follow the function
print(x(2))

# Map and filter

x = [1, 2, 3, 4, 5, 5, 6, 7, 8]
mp = map(lambda i: i + 2, x)
print(list(mp))

mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))

















