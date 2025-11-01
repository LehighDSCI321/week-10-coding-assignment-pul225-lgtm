'''
bicycles = ['trek', 'cann', 'red', 'spe']
print(bicycles[-1])
print(bicycles[2].upper())
print(bicycles[-3])

message = f'my first bicycle is {bicycles[-1].title()}'
print(message)

names = ['puyang', 'ni', 'ha', 'ci']

print(names[3])

message = 'Hello my name is'
print(f'{message} {names[3]}')

bicycles[1] = 'giant'
print(bicycles)

bicycles.append('cann')
print(bicycles)

bicycles.insert(0, 'du')
print(bicycles)

my_popped = bicycles.pop(3)
print(my_popped)

bicycles.remove('giant')
print(bicycles)
'''

my_list = ['puyang', 'jiabao', 'jinping']
my_list[-1] = 'pupu'
my_list.insert(0, 'nihao')
my_list.insert(1, 'how')
my_list.append('professor')
print(my_list)

disappear_person1 = my_list.pop()
print(f'dear {disappear_person1}, I am so sorry to tell....')

disappear_person2 = my_list.pop()
print(f'dear {disappear_person2}, I am so sorry to tell....')

disappear_person3 = my_list.pop()
print(f'dear {disappear_person3}, I am so sorry to tell....')

disappear_person4 = my_list.pop()
print(f'dear {disappear_person4}, I am so sorry to tell....')

print(my_list)
print(f'dear {my_list[-1]} you can go to the....')
print(f'dear {my_list[-2]} you can go to the....')

del my_list
print(my_list)
