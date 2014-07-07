'''
Created on Jul 7, 2014

@author: viejoemer

What is a frozenset data structure and how it works?

¿Qué es la estructura de datos frozenset y como funciona?

frozenset
Return a new set or frozenset object whose elements are taken from 
iterable. The elements of a set must be hashable. To represent sets 
of sets, the inner sets must be frozenset objects. If iterable is not
specified, a new empty set is returned.

hashable
An object is hashable if it has a hash value which never changes during
 its lifetime (it needs a __hash__() method), and can be compared to 
 other objects (it needs an __eq__() method). Hashable objects which 
 compare equal must have the same hash value.

Hashability makes an object usable as a dictionary key and a set member,
 because these data structures use the hash value internally.

All of Python’s immutable built-in objects are hashable, while no 
mutable containers (such as lists or dictionaries) are. Objects which
are instances of user-defined classes are hashable by default; they all
compare unequal (except with themselves), and their hash value is their id().
'''

#frozenset: To represent sets of sets, sets of dict etc

#Using frozenset with dict.
d = {'dict_key':'dict_value'}
f = frozenset(d)
print(f)
f_keys = frozenset(d.keys())
print(f_keys)
f_values = frozenset(d.values())
print(f_values)

#Using frozent with list.
l = [1,"string",1.1]
f = frozenset(l)
print(f)
