

def add(x,y):
    '''
    :param x: vv
    :param y: vf
    :return: ss
    '''
    return x+y

help(add)

print(add(100,200))
print(add('привет ', 'Андрей'))

def f1(n):
    def f2(m):
        return n+m
    return f2
new_f = f1(100)
print(new_f(250))

def f():
    pass

print(f())

# Аргументы

def add(x,y,z = 10):

    return x + y + z

print(add(1,2))
print(add(1,2,3))

def func(*args):
    print(type(args), args)
    return args

func (1,2,3,'привет')


