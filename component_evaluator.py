from beautiful_soup_cleaner import relevant_components
"""
"""
def price_total(component_dict):
    total_sum = 0
    for key in component_dict:
        total_sum += component_dict[key]
    total_sum = round(total_sum, 2)
    return total_sum

budget = 0

def is_all_components_present(component_dict):
    relevant_clone = relevant_components.copy()
    del relevant_clone[relevant_clone == "External Storage"]
    for key in component_dict:
        if key in relevant_components:
            del relevant_clone[relevant_clone == key]
    if relevant_clone:
        return False
    return True

#def component_evaluator(component_dict):