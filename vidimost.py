
global_var = 10

def fun_ex(local_var1, local_var2):
    print(local_var1, local_var2, global_var)
fun_ex(11, 12)


def fun_ex1(local_var1, local_var2):
    global global_var
    global_var = 20
    print(local_var1, local_var2, global_var, id(global_var))

fun_ex1(11, 12)
print(global_var, id(global_var))

# nonlocal

def counter():
    num = 0
    def plus_1():
        nonlocal num
        num+=1
        return num
    return plus_1

con = counter()
print(con())
print(con())




