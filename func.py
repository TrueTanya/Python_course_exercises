def greet(name, msg='Hello'):
    """Function about how to be pleasent"""
    hello = f"{msg}, {name}!"
    return hello


x = "human"
y = "dick"
print(greet(x))
print(greet(name=x, msg="good morning"))
print(greet(name=y, msg="big"))
print(greet(y, msg="big"))
print(greet(name="user", msg="hi"))