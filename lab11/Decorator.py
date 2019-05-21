#!usr/bin/env python3
"""
 The decorator converts a function to a descriptor. If executed on
 an instance, the descriptor returns the value of the function. If
 called on a class, the descriptor returns a sum of the original
 functions over all instances of the class. To retrieve all instances
 the descriptor uses the function provided as a parameter to the decorator.
"""



class Size:
    def __init__(self, original_function, all_instances):
        self.original_function = original_function
        self.all_instances = all_instances

    def __get__(self, instance, owner):
        if instance is None:
            return sum([self.original_function(i) for i in self.all_instances()])
        else:
            return self.original_function(instance)

def size(all_instances):
    def wrapper_function(original_function):
        return Size(original_function, all_instances)
    return wrapper_function

class Cache:
    def __init__(self):
        Cache._all_caches.append(self)
        self._storage = dict()

    _all_caches = []

    def set(self, key, value):
        self._storage[key] = value

    def get(self, key):
        self._storage[key]

    def _all_instances():
        return Cache._all_caches

    @Size(all_instances = _all_instances)
    def entries_count(self):
        return len(self._storage)


a = Cache()
b = Cache()

a.set('a', 1)
a.set('b', 2)
b.set('c', 3)

print(a.entries_count)      # prints 2
print(b.entries_count)      # prints 1
print(Cache.entries_count)  # prints 3
