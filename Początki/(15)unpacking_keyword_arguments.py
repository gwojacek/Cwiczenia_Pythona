# args = positional arguments, kwargs = keyword arguments
# ważne są 2 gwiazdki
def named(**kwargs):
    print(kwargs)

named(name="Bob", age=23)
print("111111111111111111111111111111")
#wyciaga values z dictionary i nie trzeba robić name=, age= w princie funkcji
def named_2(name, age):
    print(name, age)

details = {"name": "Cezare", "age": 25}

named_2(**details)
print("222222222222222222222222222222")

def print_nicely(**kwargs):
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(**details)
print("333333333333333333333333333333333333")


def both(*args, **kwargs):

    for kwarg, value in kwargs.items():
        print(f"{kwarg}: {value}")

    print(args)
    print(kwargs)

both(1,2,name="Jacek",profession="placek robi")