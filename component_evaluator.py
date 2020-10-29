from beautiful_soup_cleaner import relevant_components

component_percentages_modest = {"CPU": 0.2, "Memory": 0.07, "Motherboard": 0.11, "Storage": 0.1, "Video Card": 0.35, "Power Supply": 0.09, "Case": 0.08}
budget = 0

"""
Finds the price of the current build when all components are present.
"""
def price_total(component_dict):
    total_sum = 0
    for key in component_dict:
        total_sum += component_dict[key]
    total_sum = round(total_sum, 2)
    return total_sum


def is_all_components_present(component_dict):
    relevant_clone = relevant_components.copy()
    del relevant_clone[relevant_clone == "External Storage"]
    for key in component_dict:
        if key in relevant_components:
            del relevant_clone[relevant_clone == key]
    if relevant_clone:
        return False
    return True

"""
Remember, ext storage is not required
"""
def evaluate_price(component_dict, in_budget):
    build_type = find_build_type(in_budget)
    
def evaluate_price_modest(component_dict, in_budget):
    for component in component_dict:
        component_percentage = component_dict[component] / in_budget
        if component_percentage < (component_percentages_modest[component] * 0.8):
            print ("You are underspending on " + component + ".")
        elif component_percentage > (component_percentages_modest[component] * 1.2):
            print("You are overspending on " + component + ".")
        else:
            print("You are correctly spending on " + component + ".")

    
"""
Finds the type of build to determine how the components should be allocated
:param in_budget: budget of build
:return build_type: level of build to be examined
"""
def find_build_type(in_budget):
    if in_budget < 650:
        build_type = "humble"
    elif in_budget >= 650 and in_budget < 1300:
        build_type = "modest"
    elif in_budget >= 1300 and in_budget < 2200:
        build_type = "enthusiast"
    else:
        build_type = "pro"
    return build_type