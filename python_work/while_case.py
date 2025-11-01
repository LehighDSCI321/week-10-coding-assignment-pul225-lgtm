unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nthe following users have been confirmed: ")
for user in confirmed_users:
    print(user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# responses = {}
# active = True
# while active:
#     name = input("please enter your name: ")
#     response = input("which mountain would you like to climb: ")
#     responses[name] = response

#     repeat = input("would you like to let another person respond?")
#     if repeat == 'no':
#         active = False

# for name, response in responses.items():
#     print(f"{name} would like to climb {response}")

sandwich_orders = ['pastrami', 'lo', 'pastrami', 'ls', 'pastrami']
finished_sandwich = []
active = True
for sandwich in sandwich_orders:
    print(f"I made your {sandwich}")
    finished_sandwich.append(sandwich)

print("the pastrami is sold out")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

active = True
responses = {}
while active:
    people = input("pleasw enter your name: ")
    place = input("please enter a place you would like to go: ")
    repeat = input("finished?: ")

    responses[people] = place
    if repeat == "yes":
         active = False

for people, place in responses.items():
    print(f"{people} want to go to the {place}")
