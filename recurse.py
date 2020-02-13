
# factorial

def fact(num):
    if num == 0:
        return 1
    else:
        return num*fact(num-1)

print(fact(10))


fact1 = 1
for i in range(1,11):
    fact1*=i
print(fact1)

# a^b

def degree(a,b):
    if b == 0:
        return 1
    else:
        return a*degree(a, b-1)
print(degree(2,10))

deg= 1
for i in range(1,11):
    deg*=2
    
print(deg)