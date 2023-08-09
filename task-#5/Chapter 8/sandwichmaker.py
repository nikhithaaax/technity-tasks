import pyinputplus as pyip


bread_prices = {
    'wheat': 40.0,
    'white': 20.0,
    'sourdough': 35.0
}

protein_prices = {
    'chicken': 75.0,
    'turkey': 89.0,
    'ham': 50.0,
    'tofu': 56.0,
}

cheese_prices = {
    'cheddar': 20.0,
    'Swiss': 15.0,
    'mozzarella': 45.0,
}

topping_prices = {
    'mayo': 11.0,
    'mustard': 7.0,
    'lettuce': 5.0,
    'tomato': 5.0,
}


bread_choice = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='Choose a type of bread:\n')

protein_choice = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt='Choose a protein type:\n')

cheese_choice = pyip.inputYesNo('Do you want cheese? (yes/no): ')
if cheese_choice == 'yes':
    cheese_choice = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt='Choose a cheese type:\n')
else:
    cheese_choice = None

toppings = []
for topping in ['mayo', 'mustard', 'lettuce', 'tomato']:
    if pyip.inputYesNo(f"Do you want {topping}? (yes/no): ") == 'yes':
        toppings.append(topping)

num_sandwiches = pyip.inputInt('How many sandwiches do you want? (Enter a number greater than 0): ', min=1)


total_cost = (
    bread_prices[bread_choice]
    + protein_prices[protein_choice]
    + (cheese_prices[cheese_choice] if cheese_choice else 0)
    + sum(topping_prices[topping] for topping in toppings)
) * num_sandwiches


print(f"Total cost for {num_sandwiches} sandwich(es): {total_cost:.2f}")
