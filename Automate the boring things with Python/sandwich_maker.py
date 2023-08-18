import pyinputplus as pyip

cost_of_options = {
    "bread type": {
        "wheat" : 2.00,
        "white" : 1.50,
        "sourdough": 2.50
    },
    "protein type": {
        "chicken": 2.30,
        "turkey": 1.20,
        "ham": 1.40,
        "tofu": 2.30
    },
    "cheese type": {
        "cheddar": 2.00,
        "Swiss": 2.30,
        "mozzarella": 1.30
    }
}

bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt="Please Select your bread type \n", numbered=True)
protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt="Please Select your protein type \n", numbered=True)

cheese_choice = pyip.inputYesNo(prompt="Do you want to add cheese? \n")

if cheese_choice == 'Yes':
    
    cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt="Please Select your cheese type \n", numbered=True)
else:
    cheese_type = ""

cost_of_bread = cost_of_options["bread type"][bread_type]
cost_of_protein = cost_of_options["protein type"][protein_type]

if cheese_type != "":

    cost_of_cheese = cost_of_options["cheese type"][cheese_type]

else:
    cost_of_cheese = 0

total_cost = cost_of_cheese + cost_of_bread + cost_of_protein

print(f"cost of bread {cost_of_bread}")
print(f"cost of protein {cost_of_protein}")
print(f"cost of cheese {cost_of_cheese}")
print(f"total cost {total_cost}")

number = pyip.inputInt(prompt="How many sandwiches dyu want? \n",default=1)

total_cost = number * total_cost
print(f"order placed for {number} number of sandwich and total cost is ₵{total_cost} ")