def greet_user(username):
    "print hello"
    print(f"Hello, {username.title()}!")

greet_user('pu')

def display_message():
    print("this is a chapter")

def favorite_book(title):
    print(f"one of my favorite book is {title.title()}")

favorite_book('since')

def describe_pet(name = 'puyang', type = 'dog'):
    print(f"\nI have a {type}")
    print(f"my {type}'s name is {name.title()}")

describe_pet('harry', 'hamster')
describe_pet('dog', 'puyang')
describe_pet(name = 'puyang', type = 'dog')
describe_pet(name = 'willie')

def make_shirt(size, words = 'I love python'):
    print(f"\nthis shirt's size is {size}, and the words on it is {words}")

make_shirt(89)
make_shirt(47)
make_shirt(90, 'I love R')

def describe_city(name, country = 'iceland'):
    print(f"{name} is in the {country}")

describe_city('rey', 'iceland')
describe_city('pu')
describe_city(country = 'China', name = 'fujian')

def get_formatted_name(first_name, last_name):
    """return the formatted name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('gangtie', 'hongliu')
print(musician)

def get_formatted_name(first_name, last_name, middle_name = ''):
    """return the formatted name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
        return full_name.title()
    else:
        full_name = f"{first_name} {last_name}"
        return full_name.title()

musician = get_formatted_name('pu', 'li')
print(musician)

def build_person(first_name, last_name, age = None):
    person = {'first': first_name,
              'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('puyang', 'li', 89)
print(musician)

# while True:
#     print("\n please tell me your name: ")
#     print("(enter 'q' at anytime to quit)")
#     f_name = input("First name: ")
#     if f_name =='q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}")

def city_country(name, country):
    information = f"{name}, {country}"
    print(information.title())

city_country('san', 'chile')

def make_album(singer, album_name, song_number=None):
    information = {'singer': singer,
                   'album_name': album_name}
    if song_number:
        information['song_number'] = song_number
    return information

album1 = make_album('pu', 'ni')
album2 = make_album('yang', 'mi')
album3 = make_album('li', 'vi', 89)

print(album1)
print(album2)
print(album3)

# while True:
#     print("please enter the name of singer and name of the album: ")
#     print("please enter 'q' to quit")
#     singer_name = input("singer name: ")
#     if singer_name == 'q':
#         break
#     album_name = input("album name: ")
#     if album_name == 'q':
#         break
#     information = make_album(singer_name, album_name)
#     print(information)
