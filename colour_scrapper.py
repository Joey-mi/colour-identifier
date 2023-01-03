#import requests
import cssutils
#from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome()

#from bs4 import BeautifulSoup

content = ''
sheets = []

def extract_site(url):
    print('Locating website...')
    driver.get(url)

    print(driver.page_source)
    all_elem = driver.find_elements(By.CSS_SELECTOR, '*')
    for elem in all_elem:
        sheets.append(elem.value_of_css_property('color'))
    print(' ')
    print(sheets)
cnt = extract_site('https://weirdorconfusing.com/')
