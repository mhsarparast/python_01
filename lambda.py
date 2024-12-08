from functools import reduce

info_list = [
    {'unit name': 'math', 'unit_numbers': '2', 'teacher': 'arshadi'},
    {'unit name': 'arabi', 'unit_numbers': '14', 'teacher': 'bagheri'},
    {'unit name': 'andishe', 'unit_numbers': '10', 'teacher': 'solimani'},
    {'unit name': 'kamputer', 'unit_numbers': '9', 'teacher': 'mesbah'},
    {'unit name': 'raftar', 'unit_numbers': '7', 'teacher': 'alishiri'},
]
a = list(filter(lambda x: int(x['unit_numbers']) > 3, info_list))
print(a)

b = reduce(lambda x, y: int(x) + int(y), [int(item['unit_numbers']) for  item in info_list])
print(b)

expense=1000
c=list(map(lambda x: int(x['unit_numbers'])*expense, info_list))
print(c)
d=sum(c)
print(d)
