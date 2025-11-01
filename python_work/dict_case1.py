alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green',
                 'points': 5,
                 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[: 5]:
    print(alien)
print('...')
print(len(aliens))

for alien in aliens[: 3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[: 5]:
    print(alien)

for alien in aliens[: 3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

print(aliens[: 5])

pizza = {'crust': 'thick',
         'toppings': ['mushroom', 'extra cheese']}
for topping in pizza['toppings']:
    print(f'\n\t{topping}')

favorite_languages = {'jen': ['python', 'java'],
                       'sarah': ['c'],
                       'edward': ['c++', 'r'],
                       'phil': ['java']}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(language)
    elif len(languages) == 1:
        print(f"\n{name.title()}'s favorite languages is:")
        for language in languages:
            print(languages)

users = {'aeinstein': {'first': 'albert',
                       'last': 'einstein',
                       'location': 'princeton'},
         'mcurie': {'first': 'marie',
                    'last': 'curie',
                    'location': 'pairs'}
                    }

for user, user_info in users.items():
    print(f'\nUsername: {user}')
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

pet_1 = {'type': 'an', 'owner': 'pu'}
pet_2 = {'type': 'bi', 'owner': 'li'}
pet_3 = {'type': 'mi', 'owner': 'yang'}
pet_4 = {'type': 'li', 'owner': 'wi'}
pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    for type, owner in pet.items():
        print(f"{type}{owner}")

for pet in pets:
    print(f"This dog is {pet['type']}, its owner is {pet['owner']}")

favorite_places = {'pu': ['chang', 'jiang', 'yellow'],
                      'li': ['he', 'chang'],
                      'yang': ['huang', 'shan', 'zai']}

for name, places in favorite_places.items():
    print(f"my name is {name} and my favorite place are:")
    for place in places:
        print(f"\t{place}")

favorite_numbers = {'pu': [1, 2, 3], 'li': [5, 6], 'yang': [6, 8, 9]}
for name, numbers in  favorite_numbers.items():
    print(f"my name is {name}, and my favorite number are:")
    for number in numbers:
        print(f"\t{number}")

cities = {'beijing': {'country': 'China', 'population': 1000, 'facts': 'north'},
          'ny': {'country': 'US', 'population': 8000, 'facts': 'popular'},
          'shanxi': {'country': 'China', 'population': 2990, 'facts': 'landmarks'}}

for city, information in cities.items():
    print(f"this is {city}, it is located in {information['country']}"
          f"\twhose population is {information['population']}")
    if city == 'beijing':
        print(f"{information['facts']}")
    elif city == 'ny':
        print(f"{information['facts']}")
    elif city == 'shanxi':
        print(f"{information['facts']}")
