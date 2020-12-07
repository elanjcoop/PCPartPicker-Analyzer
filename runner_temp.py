from component_evaluator import *
from helpful_methods import *

print("Welcome to the PCPartPicker link analyzer!")
print("The link receiver is currently offline due to maintenance,")
print("so all values must be manually inputted:")
print_max_five(relevant_components)
print("This program analyzes your build and lets you know")
print("where you need to make changes.\n")


relevant_components = ["CPU", "Memory", "Motherboard", "Storage", "Video Card", "Power Supply", "Case"]

price_dict = {}
price_found = False

for component in relevant_components:
    price_found = False
    while price_found == False:
        try:
            print("Please enter price for " + component + ":", end = (''))
            component_cost = input()
            price_rounded = round(float(component_cost), 2)
            price_dict[component] = price_rounded
            price_found = True
        except (TypeError, ValueError):
             print("Sorry, invalid input. Please enter a float.")
         
print(price_dict)

total_price = price_total(price_dict)


print("Total price: ", end = '')
print("${:.2f}.".format(total_price))
evaluate_price(price_dict, total_price)