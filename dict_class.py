Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d = {'a':1,'b':2,'c':3}
>>> d
{'a': 1, 'c': 3, 'b': 2}
>>> for x in d:
	print x,d[x]

	
a 1
c 3
b 2
>>> for x in d:
	print x,'=',d[x]

	
a = 1
c = 3
b = 2
>>> d.clear()
>>> d
{}
>>> 
>>> 
>>> d = {'a':1,'b':2,'c':3}
>>> d.copy()
{'a': 1, 'c': 3, 'b': 2}
>>> d.copy()
{'a': 1, 'c': 3, 'b': 2}
>>> import copy
>>> copy.deepcopy()

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    copy.deepcopy()
TypeError: deepcopy() takes at least 1 argument (0 given)
>>> copy.deepcopy(d)
{'a': 1, 'c': 3, 'b': 2}
>>> d.fromkeys('c')
{'c': None}
>>> d.get('b')
2
>>> d.has_key('c')
True
>>> d.items()
[('a', 1), ('c', 3), ('b', 2)]
>>> x={values:keys for (keys,values) in d.items()}
>>> x
{1: 'a', 2: 'b', 3: 'c'}
>>> d.iteritems()
<dictionary-itemiterator object at 0x0000000003D84548>
>>> d.iteritems('c')

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d.iteritems('c')
TypeError: iteritems() takes no arguments (1 given)
>>> d.keys()
['a', 'c', 'b']
>>> d.values()
[1, 3, 2]
>>> d.pop()

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> d.pop('c')
3
>>> d
{'a': 1, 'b': 2}
>>> d.popitem()
('a', 1)
>>> d
{'b': 2}
>>> d = {'a':1,'b';2,'c':3}
SyntaxError: invalid syntax
>>> d = {'a':1,'b':2,'c':3}
>>> d1 ={'v':4,'y':5}
>>> d+d1

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    d+d1
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> d.update(d1)
>>> d
{'a': 1, 'y': 5, 'c': 3, 'b': 2, 'v': 4}
>>> d.viewkeys()
dict_keys(['a', 'y', 'c', 'b', 'v'])
>>> d.viewvalues()
dict_values([1, 5, 3, 2, 4])
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x=10
>>> type(x)
<type 'int'>
>>> 
