#  Created by Simone Margio
#  www.simonemargio.im

# Problem: sort a tuple of tuples by 2nd item
# Input: tuple = (('a', 32),('b', 2),('c', 48), ('d',22), ('e',12), ('f',0), ('g',-4), ('h',22))
# Output: (('g', -4), ('f', 0), ('b', 2), ('e', 12), ('d', 22), ('h', 22), ('a', 32), ('c', 48))

tuplesort = (('a', 32),('b', 2),('c', 48), ('d',22), ('e',12), ('f',0), ('g',-4), ('h',22))

# Sort tuple with using every second element of single tuple (key=lambda element: element[1])
tuplesort = tuple(sorted(list(tuplesort), key=lambda element: element[1]))

print(tuplesort)