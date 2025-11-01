def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

user_names = ['hannah', 'ty', 'margot']
greet_users(user_names)

def print_models(unprinted, completed):
    while unprinted:
        current = unprinted.pop()
        print(f"print model: {current}")
        completed.append(current)

def show_completed(completed):
    for model in completed:
        print(model)

unprinted = ['e', 'w', 'o', 's', 'f']
completed = []

print_models(unprinted[:], completed)
show_completed(completed)

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current = messages.pop()
        print(f"print message: {current}")
        sent_messages.append(current)
    print(messages)
    print(sent_messages)

messages = ['ni', 'hao', 'pu', 'yang']
sent_messages = []
send_messages(messages[:], sent_messages)
print(messages)

def make_pizza(*toppings):
    """print the topping the customer ordered"""
    for topping in toppings:
        print(topping)

make_pizza('wo', 'shi', 'yi', 'tou', 'zhu')

def build_profile(first, last, **user_info):
    """build a disct including user's information"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('pu', 'li', location = 'Bethlhem', field = 'data')
print(user_profile)

pu_profile = build_profile('pu', 'yang', location = 'Bethlhem', field = 'data', major = 'mathmatics')
print(pu_profile)

def sandwich(*foods):
    """show the ingredients of the foods"""
    for food in foods:
        print(f"This sandwich includes {food}")

sandwich('pu')
sandwich('li', 'pu')
sandwich('li', 'pu', 'yang')

def car_profile(manufacturer, model, **car_info):
    """build a dict including car's profile"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = car_profile('subaru', 'outback', color = 'blue', tow_package = True)
print(car)
