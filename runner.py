from beautiful_soup_cleaner import *
from component_evaluator import *

html_file_raw = input("Enter a link:\n")
print("\n")

html_file = clean_html(html_file_raw)

prices_per_component = get_list(html_file)

print(prices_per_component)
total_price = price_total(prices_per_component)

# print("{:.2f}".format(total_price))

if is_all_components_present(prices_per_component):
    print("All of the necessary components have been accounted, " +
          "for a total of ")
    print("{:.2f}".format(total_price))
    budget_chosen = False
    budget_found = False
    print("Is that correct? Enter [y] for yes or [n] for no.", end = (''))
    while(not budget_chosen or not budget_found):
        is_budget = input().upper()
        if is_budget == "Y":
            budget_chosen = True
            budget = total_price
            budget_found = True
        elif is_budget == "N":
            budget_chosen = True
            print("No problem. Please type in your budget.", end = (''))
            while not budget_found:
                budget_input = input()
                try:
                    budget_input = round(float(budget_input), 2)
                    budget = budget_input
                    budget_found = True
                except (TypeError, ValueError):
                    print("Sorry, invalid input. Please enter a float.", end = (''))
        else:
            print("Sorry, invalid input. Select [y] or [n].", end = '')
            
print("{:.2f}".format(budget))