
def make_pizza(size, *toppings):
    """describe the pizza which will be made"""
    print(f"\nmaking a {size} pizza")
    for topping in toppings:
        print(f"- {topping}")
