peoples = ['ni', 'hao', 'i', 'am', 'stupid']
for people in peoples:
    print(f"this {people.title()}'s work is awsome")
    print(people)
print('Thank you, everyone. That was a great job')

message = 'Hello Python World'
print(message)

for value in range(1, 5):
    print(value)

numbers = list(range(1, 11, 2))
print(numbers)

squres = []
for number in range(1, 11): 
    squres.append(number ** 2)
print(squres)

print(min(range(1, 100)))
print(max(range(1, 100)))
print(sum(range(1, 100)))

squares = [value ** 2 for value in range(1, 11)]
print(squares)

for number in range(1, 21, 2):
    print(number)

my_numbers = list(range(3, 31, 3))
for number in my_numbers:
    print(number)

cube = []
my_numbers = list(range(1, 11))
for number in my_numbers:
    cube.append(number ** 3)
print(cube)

cube = []
my_numbers = list(range(1, 11))
for number in my_numbers:
    cube.append(number ** 3)
print(cube)

cube = [number ** 3 for number in my_numbers]
print(cube)

print(my_numbers[:-4])

for number in my_numbers[:-4]:
    print(number ** 3)

print(my_numbers)
my_number = my_numbers[:]
print(my_number)

my_number = my_numbers
my_numbers.append(100)
my_number.append(99)
print(my_numbers)
print(my_number)

middle_number = int(len(my_number) / 2)
print('The first three items are:', my_numbers[0:3])
print('Three items from the middle of the list are:', my_numbers[middle_number - 1 : middle_number + 2])
print('The last three items are:', my_numbers[-3:])

my_pizza = ['hot', 'pot', 'grass', 'tree', 'build', 'today']
your_pizza = my_pizza[:]

my_pizza.append('yes')
print(my_pizza)
your_pizza.append('no')
print(your_pizza)

for pizza in my_pizza:
    print(pizza)
for pizza in your_pizza:
    print(pizza)
