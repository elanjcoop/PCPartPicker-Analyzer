from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re

relevant_components = ["CPU", "Memory", "Motherboard", "Storage", "Video Card", "Power Supply", "Case", "External Storage"]
page_not_found = "Page not found."
status_code_not_200 = "Page could not be received."
error_codes = {"/b/": "Please provide a link of a build.",
               "https://pcpartpicker.com/": "Please provide a PCPARTPICKER link."
               }


"""
Receives an link and turns into a searchable html address
Raises error code if link is missing key components
:param html_file_raw: inputted, raw link
:return html_file: corrected htmlk
"""
def clean_html(html_file_raw):
    https = "https://"
    if https not in html_file_raw:
        html_file = https + html_file_raw
    else:
        html_file = html_file_raw
    for key in error_codes:
        if key not in html_file:
            print(error_codes[key])
            raise SystemExit
    return html_file


"""
Deletes duplicate elements in the lists and adds together values as necessary
:param dirty_list: list with duplicate entries
:return clean_list: list without the 
"""
def delete_duplicates(dirty_list):
    clean_list = {i:0 for i, v in dirty_list}
    for key, value in dirty_list:
        clean_list[key] = round(clean_list[key] + value, 2)
    return clean_list


"""
Removes components which we will not factor in (e.g. CPU Cooler, Case Fans, Operating System, Software, Custom, etc.)
Removes components that have no cost entry
Turns external storage into regular storage
:param dirty_dict: our full dict with the components we should not have
:return clean_dict: list with irrelevant components removed
"""
def delete_irrelevant_components(dirty_dict):
    clean_dict = dict(dirty_dict)
    for key in dirty_dict:
        if key not in relevant_components or dirty_dict[key] == 0:
            del clean_dict[key]
        if key == "External Storage":
            print(clean_dict)
            value = dirty_dict[key]
            try:
                clean_dict["Storage"] += value
            except KeyError:
                clean_dict["Storage"] = 0
                clean_dict["Storage"] += value
            try:
                del clean_dict[key]
            except KeyError:
                pass
    return clean_dict

"""
Gets soup object from html_file
:param html_file: working html to get the soup from
:return soup: soup to be parsed
"""
def get_soup(html_file):
    source = requests.get(html_file)
    if not source.status_code == 200:
        print(status_code_not_200)
        return(status_code_not_200)
    soup = BeautifulSoup(source.text, 'lxml')
    if page_not_found in soup.title.string:
        return(page_not_found)
    return soup

"""
Get the list of all prices and components from the soup.
WARNING: if element_price is set to find a, it will not account for foreign currency
:param soup: soup to be parsed
:return prices_per_component_dirty: prices and component list with extraneous values
"""
def get_prices_per_component_dirty(soup):
    components = []
    prices = []
    for element in soup.find_all('td', class_ = 'td__component'):
        components.append(element.string)

    for element in soup.find_all('td', class_='td__name'):
        element_price = element.find('p', class_="td__price")
        if element_price == None:
            element_price = element.find('a', class_="td__price")
        
        if element_price == None or element_price.string == None:
            prices.append(0)
            continue
        
        numeric_string = re.sub("[^0-9, .]", "", element_price.string)
        numeric_string = re.sub("\s", "", numeric_string)
        if numeric_string != "":
            prices.append(float(numeric_string))
        else:
            prices.append(0)
    prices_per_component_dirty = list(zip(components, prices))
    return prices_per_component_dirty
    
"""
Main method for this class that stems from main and runs through the method to get the final dict
:param html_file: HTML file that is cleaned and ready to run through these methods
:return prices_per_component_clean: final dict with corrected values and relevabt components
"""
def get_list(soup):
    if soup == page_not_found or soup == status_code_not_200:
        return({})
    print(soup.title.string)
    prices_per_component_dirty = get_prices_per_component_dirty(soup)
    prices_per_component_clean = delete_duplicates(prices_per_component_dirty)
    prices_per_component_clean = delete_irrelevant_components(prices_per_component_clean)
    return prices_per_component_clean

def get_page_title(soup):
    try:
        return soup.title.string
    except AttributeError:
        return "Page Not Found"