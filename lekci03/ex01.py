def f(x):
    return x**2


g = f

print(type(f))
print(type(g))
print(f(2))
print(g(4))


def f(x):
    return x ** 3


list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
list = []
for i in range(1, 21):
    if i % 2 == 0:
        list.append(i)
        print(i, '=', f(i), end=', ')
print(list)

with open('file3.txt', 'w') as data:
    data.write('1 2 3 5 8 15 23 38')
data.close()
path = 'file3.txt'  # путь к файлу пишется "путь"
data = open(path, 'r')

for line in data:
    print(line)

list = [(i, f(i)) for i in map(int, line) if not i % 2]
print(line)

print(list)

data.close()

with open('file3.txt', 'r') as f:
    list = [(i, i**2) for i in map(int, f.read().split()) if not i % 2]
    print(list)
f.close()

with open('file3.txt', 'r') as f:
    res = list(filter(lambda x: not x % 2, map(int, f.read().split())))
    print(res)
f.close()

data = '1 2 3 5 8 15 25 38'.split()
with open('file3.txt', 'r') as f:
    res = map(int, f.read().split())
    res = filter(lambda x: not x % 2, res)
    res = list(map(lambda x: (x, x**2), res))
    print(res)
f.close()
