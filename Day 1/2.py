import pprint
comp = ['spam', (1, 2, 3), ('ham', 'egg', ('ab', 'cd', ('abc', 'def')))]
comp *= 3
pprint.pprint(comp)
print(comp)