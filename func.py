# def greet(name, msg='Hello'):
#     """Function about how to be pleasent"""
#     hello = f"{msg}, {name}!"
#     return hello


# x = "human"
# y = "dick"
# print(greet(x))
# print(greet(name=x, msg="good morning"))
# print(greet(name=y, msg="big"))
# print(greet(y, msg="big"))
# print(greet(name="user", msg="hi"))


# def add(*args):
#     result = ""
#     for i in args:
#         result = result + str(i)
#     print(result)

# add("One","Two","Three")


# l = ["One","Two","Three"]
# add(l)
# add(*l)
# add(*"banana")
# add(*range(1, 6, 2))


# def add_2(**kwargs):
#     for k, v in kwargs.items():
#         print(f"{k}:{v}")

# add_2(name="user",second="good", item="thing")


# d = {"name":"user","second":"good", "item":"thing"}
# add_2(**d)
# add(*d)


# def add_3(*args, **kwargs):
#     result = ""
#     for i in args:
#         result = result + str(i)
#     print(result)
#     for k, v in kwargs.items():
#         print(f"{k}:{v}")

# add_3(*l, **d)


def add_num(n):
    return n + 1

def operator(fun, val):
    return fun(val)


def parent():
    print("Begining")

    def inside():
        print("Inside")

    def second():
        print("Second")

    inside()
    second()



parent()



def greet(age):
    def adult(name):
        print(f"Hello, {name}!")

    def young(name):
        print(f"Hi, {name}!")

    if age < 16:
        return young
    else:
        return adult

get_greet = greet(20)
get_greet_2 = greet(8)
get_greet("User")
get_greet_2("Child")