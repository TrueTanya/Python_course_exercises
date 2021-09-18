def gen():
    num = 0
    while True:
        yield num
        num += 1
        if num > 100:
            return


print(type(gen))

# for i in gen():
#     print(i)

numbers = (line for line in open("million.txt", "rt"))
only_numbers = (line.strip() for line in numbers)

def pal(seq):
    for line in seq:
        if line == line[::-1]:
            yield line

for item in pal(only_numbers):
    print(item)

input()

def gen():
    num = 0
    while True:
        yield num
        num = num + 1 

g = gen()
print(next(g))

ge = (i for i in range(100))
ge.__next__()
next(ge)

def gen2():
    print("Start")
    n = 0
    while True:
        print(n)
        yield n
        n = n + 1

b = gen2()
next(b) 

