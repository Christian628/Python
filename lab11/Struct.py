#!usr/bin/env python3
"""
The attributes listed in the class are the only ones that are permitted in the struct.
The values defined in the class declaration are defaults to be used if the value
of a respective attribute is not specified when creating an instance of the struct.
"""


class Meta(type):
    def __new__(cls, name, bases, namespace):
        if 'x' in namespace.keys():
            default_x = namespace.pop('x')
        else:
            default_x = None

        if 'y' in namespace.keys():
            default_y = namespace.pop('y')
        else:
            default_y = None

        namespace['__slots__'] = 'x', 'y'
        namespace['default_x'] = default_x
        namespace['default_y'] = default_y

        def init(self, x=None, y=None):
            cls = type(self)
            if x is not None:
                self.x = x
            else:
                self.x = cls.default_x

            if y is not None:
                self.y = y
            else:
                cls.default_y

        def repr(self):
            output = 'Point('

            if self.x != type(self).default_x:
                output += f'x={self.x}'

            if self.y != type(self).default_y:
                if self.x != type(self).default_x:
                    output += ', '
                output += f'y={self.y}'
            output += ')'

            return output

        namespace['__init__'] = init
        namespace['__repr__'] = repr

        return super().__new__(cls, name, bases, namespace)


class Struct(metaclass=Meta):
    pass


class Point(Struct):
    x = 3.5
    y = 4.5


p = Point(y=8)
print(p)    # prints Point(y=8)

p.y = 2
p.x = 3
print(p)    # prints Point(x=3, y=2)

#p.z = 3   # AttributeError: 'Point' object has no attribute 'z'
