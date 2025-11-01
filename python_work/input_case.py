# message = input('Tell me smoething:')
# print(message)

# name = input('please enter your name: ')
# print(f'\nHello, {name}')

# prompt = 'If you share your name'
# prompt += 'we can personalize the message you see: '
# message = input(prompt)
# print(f'Hello, {message}')

# age = input('please enter your age: ')
# age = int(age)
# print(age)
# print(type(age))

# if age >= 10:
#     print('you are not a child anymore')
# else:
#     print('you are just a kid')

# print(90 % 4)
# print(4 % 90)

# number = input("please enter a number, then I will tell you something: ")
# number = int(number)
# if number % 2 == 0:
#     print("It is an even number")
# else:
#     print("It is an odd number")

# car = input("please tell me what car you want: ")
# print(f"The {car} is amazing")

# customer_number = input("please tell me how many people you are with: ")
# customer_number = int(customer_number)
# if customer_number > 8:
#     print("there is no place")
# else:
#     print("please come in")

# int_number = input('please enter a number and I will tell you if it can be divided by 10: ')
# int_number = int(int_number)
# if int_number % 10 == 0:
#     print("the number is multiples of ten")
# else:
#     print("this is a good number")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# prompt = "\nTell me something, and I will repeat it back to yoi: "
# prompt += "\nEnter 'quit' to end the program."

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# active = True
# while active:
#     message = input("please enter something: ")
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# active = True
# while active:
#     message = input("Please enter the ingredients: ")
#     if message == 'quit':
#         break
#     else:
#         print(message)

active = True
current_number = 10
while active:
    current_number += 1
    if current_number > 15:
        break
    else:
        print(current_number)
