my_dict = {'Ruslan': 1998, 'Adelina': 2003,'Darina': 2006}
print(my_dict)
print(my_dict['Ruslan'])
print(my_dict.get('Rezeda'))
my_dict.update({'Ainur': 2001,
                'Timur': 2002})
a=my_dict.pop('Ruslan')
print(a)
print(my_dict)

my_set={1,2,'aplle',4,5,6,1,5,3}
print(my_set)
my_set.add(9)
my_set.add(10)
my_set.remove(5)
print(my_set)