# collections: counter, namedtuple, OrderedDict, defaultydict, deque

#from collections import Counter 
#a = "aaaabbbccc"
#my_counter = Counter(a)
#print(my_counter)
#print(list(my_counter.elements()))

#from collections import OrderedDict
#Point = namedtuple('Point', 'x,y')
#pt = Point(1, -4)
#print(pt.x, pt.y)

#from collections import OrderedDict
#ordered_dict = OrderedDict()
#ordered_dict['b'] = 2
#ordered_dict['c'] = 3
#ordered_dict['d'] = 4
#ordered_dict['a'] = 1 
#print(ordered_dict)

#from collections import defaultdict
#d = defaultdict(int)
#d['a'] = 1 
#d['b'] = 2
#print(d['b'])

from collections import deque 
d = deque()

d.append(1)
d.append(2)

d.appendleft([4,5,6])
print(d)
d.rotate(-1)
print(d)
