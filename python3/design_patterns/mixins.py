# https://www.ianlewis.org/en/mixins-and-python

# Python supports a simple type of multiple inheritance which allows the creation of Mixins. Mixins are a sort of
# class that is used to "mix in" extra properties and methods into a class. This allows you to create classes in a
# compositional style.

# Mixins are a really great concept but I often find that people use them incorrectly which can lead to some bugs. I
# often see Mixins used like the following:


class BaseClass:
    def __init__(self):
        pass

    def test(self):
        print("Base Class")


class Mixin1(object):
    def test(self):
        print("Mixin1")


class Mixin2(object):
    def test(self):
        print("Mixin2")


class MyClass(BaseClass, Mixin1, Mixin2):
    pass


# However, in Python the class hierarchy is defined right to left, so in this case the Mixin2 class is the base
# class, extended by Mixin1 and finally by BaseClass. This is usually fine because many times the mixin classes don't
# override each other's, or the base class' methods. But if you do override methods or properties in your mixins this
# can lead to unexpected results because the priority of how methods are resolved is from left to right.

obj = MyClass()
obj.test()

# The correct way to use mixins is like in the reverse order:


class MyClass(Mixin2, Mixin1, BaseClass):
    pass


# This kind of looks counter-intuitive at first because most people would read a top-down class hierarchy from left
# to right but if you include the class you are defining, you can read correctly up the class hierarchy (MyClass =>
# Mixin2 => Mixin1 => BaseClass. If you define your classes this way you won't have to many conflicts and run into
# too many bugs.

obj = MyClass()
obj.test()
