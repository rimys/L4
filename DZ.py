import random
def spisok(kolvo, imena):
    result1 = []
    for i in range(0, kolvo):
        result1.append(random.choice(imena))
    return result1

def chasto(a):
    vsego = str(len(a))
    result2 = max(a, key=a.count)
    return result2, vsego

def bukva(a):
    new_res = []
    for i in range(len(a)):
        f = str(a[i])
        for j in range(len(f)):
            g = f[0]
            new_res.append(g)
    result3 = max(g, key=g.count)
    return result3

otdel = ['Вася', 'Петя', 'Маша', 'Вовочка', 'Антон', 'Андрей', 'Ирвин', 'Мезозой', 'Иврит', 'Александр', 'Вениамин', 'Геннадий', 'Чебурашкен', 'Анатолий', 'Вельзевул', 'Зверь', 'Иннокентий', 'Паладин', 'Оргструктура', 'Величие']
n = 25

s = spisok(n, otdel)

print(s)
print(chasto(s))
print(bukva(s))


