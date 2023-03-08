class MyClass_new:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func_suck(self):

        pak_suck = self.name + " " + "suck"

        return pak_suck


# https://ru.hexlet.io/courses/python-oop-basics/lessons/inheritance/theory_unit
class My_son(MyClass_new):


    def func_2(self):
        self.name = 2
        print(self.name)
        return self.name