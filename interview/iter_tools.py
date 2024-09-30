"""
    --- filter ---

nums = [1, 4, 5, 7, 16]


def my_func(x):
    if x % 2 == 0:
        return True
    else:
        return False


filtered_nums = filter(my_func, nums)

for num in filtered_nums:
    print(num)
"""

"""
    --- map ---

nums = [1, 2, 4, 6]
result = tuple(map(lambda x: x ** 2, nums))
print(result)
"""

"""
    --- reduce ---

from functools import reduce

nums = [1, 3, 5, 6, 2]
result = reduce(lambda x, y: x * y, nums)
print(result)  # output: 180
"""

"""
    -----------------
    --- itertools ---
    -----------------
    
from itertools import count

for i in count(10, 2):
    print(i)
    if i > 1000:
        break
# Output: 10, 12, 14, 16, 18, 20, ...

--------------------------------------------
from itertools import cycle

counter = 0
for item in cycle(['A', 'B', 'C']):
    print(item)
    counter += 1
    if counter == 6:
        break
# Output: A, B, C, A, B, C, ...
--------------------------------------------
from itertools import repeat

for item in repeat('Hello', 3):
    print(item)
# Output: Hello, Hello, Hello
--------------------------------------------
from itertools import product

print(list(product('AB', repeat=2)))
# Output: [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
--------------------------------------------
from itertools import permutations

print(list(permutations('ABC', 2)))
# Output: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
--------------------------------------------
from itertools import combinations

print(list(combinations('ABC', 2)))
# Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]
--------------------------------------------
from itertools import combinations_with_replacement

print(list(combinations_with_replacement('ABC', 2)))
# Output: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
--------------------------------------------
from itertools import accumulate
from operator import mul

print(list(accumulate([1, 2, 3, 4], mul)))
# Output: [1, 2, 6, 24] (1, 1*2, 1*2*3, 1*2*3*4)
--------------------------------------------
from itertools import chain

print(list(chain('ABC', 'DEF')))
# Output: ['A', 'B', 'C', 'D', 'E', 'F']
--------------------------------------------
from itertools import islice

print(list(islice(range(10), 1, 8, 2)))
# Output: [1, 3, 5, 7]
--------------------------------------------
from itertools import tee

iter1, iter2 = tee([1, 2, 3, 4], 2)
print(list(iter1))  # Output: [1, 2, 3, 4]
print(list(iter2))  # Output: [1, 2, 3, 4]
--------------------------------------------
from itertools import zip_longest

print(list(zip_longest('AB', '1234', fillvalue='-')))
# Output: [('A', '1'), ('B', '2'), ('-', '3'), ('-', '4')]
--------------------------------------------
"""

"""
    *** COLLECTIONS ***

------------------------------------------
from collections import namedtuple

point = namedtuple('Point', ['x', 'y'])
p = point(10, 20)
print(p.x, p.y)
------------------------------------------
from collections import deque

d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
print(d)

d.pop()
d.popleft()
print(d)
------------------------------------------
from collections import Counter

c = Counter('avada kedavra')
print(c)
print(c['a'])
c.update('aaaa')
print(c)
------------------------------------------
from collections import defaultdict

dd = defaultdict(set)
dd['a'].add(1)
dd['b'].add(2)
dd['a'].add(3)
print(dd)
------------------------------------------
from collections import OrderedDict

od = OrderedDict()
od['one'] = 1
od['two'] = 2
od['three'] = 3
print(od)
------------------------------------------
from collections import ChainMap

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
cm = ChainMap(dict1, dict2)
print(cm)
print(cm['three'])
cm = ChainMap(cm, {'twelve': 20})
------------------------------------------
from collections import UserDict

class MyDict(UserDict):
    def __missing__(self, key):
        return 'default'

md = MyDict({'a': 1, 'b': 2})
print(md['a'])   # Output: 1
print(md['c'])   # Output: default

------------------------------------------
"""

