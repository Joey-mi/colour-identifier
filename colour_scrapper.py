#import requests
# import cssutils
#from urllib.parse import urljoin
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome()

#from bs4 import BeautifulSoup

def extract_site(url):
    intermediate_colours = []
    colour = []

    print('Locating website...')
    driver.get(url)

    print(driver.page_source)
    all_elem = driver.find_elements(By.CSS_SELECTOR, '*')
    for elem in all_elem:
        intermediate_colours.append(elem.value_of_css_property('color'))
        intermediate_colours.append(elem.value_of_css_property('background'))
        intermediate_colours.append(elem.value_of_css_property('text-shadow'))
        intermediate_colours.append(elem.value_of_css_property('background-color'))
        intermediate_colours.append(elem.value_of_css_property('border'))
        intermediate_colours.append(elem.value_of_css_property('border-bottom-color'))
        intermediate_colours.append(elem.value_of_css_property('border-color'))
        intermediate_colours.append(elem.value_of_css_property('border-left-color'))
        intermediate_colours.append(elem.value_of_css_property('border-right-color'))
        intermediate_colours.append(elem.value_of_css_property('border-top-color'))
        intermediate_colours.append(elem.value_of_css_property('box-shadow'))
        intermediate_colours.append(elem.value_of_css_property('caret-color'))
        intermediate_colours.append(elem.value_of_css_property('column-rule'))
        intermediate_colours.append(elem.value_of_css_property('column-rule-color'))
        intermediate_colours.append(elem.value_of_css_property('filter'))
        intermediate_colours.append(elem.value_of_css_property('opacity'))
        intermediate_colours.append(elem.value_of_css_property('outline-color'))
        intermediate_colours.append(elem.value_of_css_property('outline'))
        intermediate_colours.append(elem.value_of_css_property('text-decoration'))
        intermediate_colours.append(elem.value_of_css_property('text-decoration-color'))

    print(' ')
    for all_text in intermediate_colours:
        just_colour = ''

        if type(all_text) is not tuple:
        
            split_by_parentheses = re.split('[)]', all_text)
            isolate_colour = []
            for splits in split_by_parentheses:
                isolate_colour = isolate_colour + re.split('rgb', splits)
            

            for elem in isolate_colour:
                
                elem = elem + ')'
                elem = 'rgb' + elem
                eliminate_space = re.split(' ', elem)
                complete = ''

                for items in eliminate_space:
                    complete = complete + items

                if re.search(pattern = "rgb\(\s*(?:(\d{1,3})\s*,?){3}\)", string = complete): 
                    just_colour = complete
                    colour.append(just_colour)
                elif re.search(pattern = "rgba\(\s*(?:(\d{1,3})\s*,?){4}\)", string = complete):
                    just_colour = complete
                    colour.append(just_colour)
    result = []
    [result.append(x) for x in colour if x not in result]
    return result

# def eliminate_duplicates(an_arr):
#     match len(an_arr):
#         case 0 | 1:
#             return an_arr
#         case _:
#             first = an_arr[:len(an_arr)//2]
#             second = an_arr[len(an_arr)//2:]

#             result = []
#             recurse_through = []

#             if len(first) > len(second):
#                 recurse_through = first
#             else:
#                 recurse_through = second
            
#             counter = 0
#             for elem in recurse_through:
#                 if 



    

cnt = extract_site('https://weirdorconfusing.com/')
print(cnt)


