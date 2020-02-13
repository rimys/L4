
def ident(x):
    return x

print (ident(10))

print((lambda x: x)(10))

ident_lambda = lambda x: x

print(ident_lambda(11))

swift = lambda a , b , c: f'unit A: {a.title()}, unit B: {b}, unit C: {c}'

print(swift('Hello', 'Andreu', 1111))

