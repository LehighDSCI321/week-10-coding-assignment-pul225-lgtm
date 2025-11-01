alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)
alien_1['color'] = 'yellow'
alien_1['speed'] = 'medium'
alien_1['position'] = 25
print(alien_1)

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_1['position'] = alien_1['position'] + x_increment
print(alien_1)

del alien_1['points']
print(alien_1)

favorite_dish  = {
    'li': 've',
    'puyang': 'ye',
    'ni': 'ti',
    'hao': 'mi',
    }

choice = favorite_dish['li'].title()
print(choice)

ponit_value = favorite_dish.get('point', 'error')
print(ponit_value)

puyang = {'first': 'puyang', 'last': 'li', 'age': 25, 'city': 'xian'}
print(puyang)

favorite_numbers = {'pu': 12, 'ni': 25, 'san': 20, 'mi': 90, 'di': 67}
print(favorite_numbers)

for k, v in favorite_numbers.items():
    print(f'\nthis is the {k}')
    print(f'this is the {v}')

languages = {'jen': 'python', 'sarah': 'c', 'edward': 'c++', 'phil': 'java', 'puyang': 'c'}
for name, language in languages.items():
    print(f"{name.title()}'s favorite language is {language}")

for name in languages.keys():
    print(name.title())

for name in languages:
    print(name.title())

friends = ['jen', 'edward']
for name, language in languages.items():
    print(f'hi this is {name}')
    if name in friends:
        print(f"    {name}'s favorite language is {language}")
    else:
        print(f'{name} please take our poll')

print(languages.keys())
print(languages.values())

for name in sorted(languages.keys()):
    print(name)

print('the follow language has been mentioned:')
for language in languages.values():
    print(language)

print('the follow language has been mentioned:')
for language in set(languages.values()):
    print(language.title())

language = {'ni', 'hao', 'pu', 'yang', 'ni', 'ni'}
print(language)

country_rivers = {'changjiang': 'China', 'yellowriver': 'China', 'nile': 'egypt'}
for river, country in country_rivers.items():
    print(f'The {river.title()} runs through {country.title()}')

for river in country_rivers.keys():
    print(f"The river's name is {river.title()}")

for country in country_rivers.values():
    print(f"The country's name is {country.title()}")
