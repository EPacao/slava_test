
from my_class import MyClass_new

def my_void(a, b):

    for i in range(1, 50, 2):
        c = a*i*b
        print(c)

    return c

if __name__ == "__main__":
    print("Hello, World!")

    # c = my_void(2, 10)
    # print(c)

    person1 = MyClass_new("Pak", 24)

    print(person1.name)

    suck = person1.func_suck()
    print(suck)

