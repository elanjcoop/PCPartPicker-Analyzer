from beautiful_soup_cleaner import relevant_components

component_percentages_humble = {"CPU": 0.27, "Memory": 0.07, "Motherboard": 0.14, "Storage": 0.09, "Video Card": 0.23, "Power Supply": 0.11, "Case": 0.09}
component_percentages_modest = {"CPU": 0.2, "Memory": 0.07, "Motherboard": 0.11, "Storage": 0.1, "Video Card": 0.35, "Power Supply": 0.09, "Case": 0.08}
component_percentages_enthusiast = {"CPU": 0.23, "Memory": 0.05, "Motherboard": 0.1, "Storage": 0.13, "Video Card": 0.37, "Power Supply": 0.06, "Case": 0.06}
component_percentages_pro = {"CPU": 0.19, "Memory": 0.06, "Motherboard": 0.13, "Storage": 0.11, "Video Card": 0.4, "Power Supply": 0.06, "Case": 0.05}
component_percentages_god = {"CPU": 0.16, "Memory": 0.06, "Motherboard": 0.07, "Storage": 0.09, "Video Card": 0.47, "Power Supply": 0.06, "Case": 0.09}


"""
Finds the price of the current build when all components are present.
:param component_dict: dict with all the prices and components
:return total_sum: total price
"""
def price_total(component_dict):
    total_sum = 0
    for key in component_dict:
        total_sum += component_dict[key]
    total_sum = round(total_sum, 2)
    return total_sum

"""
Receives dictionary of prices and components and determines if the
required 7 are present.
:param component_dict: prices and component dict
:return: boolean
"""
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
Crux of the program!
Checks each component according to the build type's dictionary.
If it's under 80% of the suggested allocation, you're overspending,
over 120%, you are overspending.
Feel free to reach out to me if you think these numbers can be refactored.
:param component_dict: dict of prices and components
:param in_budget: budget inputted into method
:return: void, but prints messages as it goes, this might change in later iterations of program
"""
def evaluate_price(component_dict, in_budget):
    component_percentages_current = find_build_type(in_budget)
    for component in component_dict:
        component_percentage = component_dict[component] / in_budget
        if component_percentage < (component_percentages_current[component] * 0.8):
            print("You are underspending on " + component + ".")
        elif component_percentage > (component_percentages_current[component] * 1.2):
            print("You are overspending on " + component + ".")
        else:
            print("You are correctly spending on " + component + ".")


    
"""
Finds the type of build and returns dict that shows how the components should be allocated
:param in_budget: budget of build
:return build_type: dictionary with percentages depending on build type
"""
def find_build_type(in_budget):
    if in_budget < 650:
        component_percentages_current = component_percentages_humble
    elif in_budget >= 650 and in_budget < 1300:
        component_percentages_current = component_percentages_modest
    elif in_budget >= 1300 and in_budget < 2200:
        component_percentages_current = component_percentages_enthusiast
    elif in_budget >= 2200 and in_budget < 3000:
        component_percentages_current = component_percentages_pro
    else:
        component_percentages_current = component_percentages_god
    return component_percentages_current

"""
Returns component dictionary as a list of percentages over total cost
:param component_dict: dict of prices and components
:param total_cost: total cost of build
:return: array of percentages
"""
def component_percentage_list(component_dict, total_cost):
    component_percentage_list = []
    for key in component_dict:
        component_percentage = round(component_dict[key] / total_cost, 2)
        component_percentage_list.append(component_percentage)
    return component_percentage_list