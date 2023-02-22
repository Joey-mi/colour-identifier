import re
from pywinauto import Application

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ttps://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters
def colourProgressBar(iteration, total, prefix='', suffix='', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print newline on complete
    if iteration == total:
        print()

def extract_site(url):
    intermediate_colours = []
    colour = []

    driver_exe = 'chromedriver'
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(driver_exe, options=options)
    driver.get(url)
    #print('Locating website...')
    #driver.get(url)

    # print(driver.page_source)

    all_elem = driver.find_elements(By.CSS_SELECTOR, '*')
    total_selectors_with_colours = len(all_elem)
    i = 0

    print("Analyzing css properties: ")
    colourProgressBar(0, total_selectors_with_colours, prefix = 'Progress:', suffix = 'Complete', length = 50)
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
        colourProgressBar(i + 1, total_selectors_with_colours, prefix = 'Progress:', suffix = 'Complete', length = 50)
        i = i + 1

    print(' ')

    all_properties = len(intermediate_colours)

    print("Parsing colours: ")
    colourProgressBar(0, all_properties, prefix = 'Progress:', suffix = 'Complete', length = 50)
    i = 0
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
        colourProgressBar(i + 1, all_properties, prefix = 'Progress:', suffix = 'Complete', length = 50)
        i = i + 1
    result = []
    [result.append(x) for x in colour if x not in result]
    return result

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
app = Application(backend='uia')
app.connect(title_re=".*Chrome.*")
element_name="Address and search bar"
dlg = app.top_window()
url = dlg.child_window(title=element_name, control_type="Edit").get_value()

#cnt = extract_site('https://weirdorconfusing.com/')

cnt = extract_site(url)
print(cnt)


