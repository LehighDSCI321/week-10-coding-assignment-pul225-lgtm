cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
car = 'audi'
print(car == 'bmw')

car = 'Audi'
print(car.lower() == 'audi')
print(car)

topping = 'mushrooms'
if topping != 'anchovies':
    print('It is not what I want')

age = 30
print(age < 20)

car = 'audi'
print(car in cars)
if 'bike' not in cars:
    print('please enter the correct information')

for car in cars:
    print(car == 'bmw')

age = 66
if age > 16:
    print('you are little')

if age < 4:
    price = 0
elif age < 18:
    price = 20
elif age < 65:
    price = 40
else:
    price = 40 * 0.3
print(price)

if 'audi' in cars:
    print('I am audi')
if 'bmw' in cars:
    print('I am bmw')
if 'subaru' in cars:
    print('I am subaru')

if 'audi' in cars:
    print('I am audi')
elif 'bmw' in cars:
    print('I am bmw')
elif 'subaru' in cars:
    print('I am subaru')

alien_color = 'yellow'
if alien_color == 'green':
    print('get 5 points')
elif alien_color == 'red':
    print('get 6 points')
else:
    print('no point')

age = 65
if age < 2:
    print('I am a babby')
if age < 4:
    print('I am a little child')
if age < 13:
    print('I am a child')
if age < 18:
    print('I am a boy')
if age >= 65:
    print('I am a old')

for car in cars:
    if car == 'toyota':
        print('This is awsome')
    else:
        print(f'I like this {car} brand')

vegeatbles = ['ca', 'ba', 'in', 'pu']
if vegeatbles:
    for vegetable in vegeatbles:
        print('qqq')
else:
    print('ppp')

ava_topp = ('mush', 'oliv', 'gree', 'pepp', 'pine', 'extr')
requ_top = ['mush', 'french', 'extr']
for requ in requ_top:
    if requ in ava_topp:
        print('This is what we have')
    else:
        print("we don't have this")

user_names = ['puyang', 'rsq', 'mi', 'nihao', 'admin']
if user_names:
    for user in user_names:
        if user == 'admin':
            print(f'welcome {user}')
        else:
            print(f'thank you for logging again, {user}')

current_users = ['Pu', 'yang', 'Is', 'Stupid', 'true']
current_users1 = current_users[:]
current_users1 = [user.lower() for user in current_users1]
print(current_users1)

new_users = ['pu', 'li', 'is', 'very', 'fool']
for user in new_users:
    if user in current_users:
        print('This name is invalid')
    else:
        print('This is a good name')

numbers = [1, 2, 3, 4, 5, 6, 7 ,8 ,9]
for i in numbers:
    if i == 1:
        print('1st')
    if i == 2:
        print('2nd')
    if i == 3:
        print('3rd')
    if i == 4:
        print('4th')
    if i == 5:
        print('5th')
    if i == 6:
        print('6th')
    if i == 7:
        print('7th')
    if i == 8:
        print('8th')
    if i == 9:
        print('9th')
