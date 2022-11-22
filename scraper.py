from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains, keys

# definition of the search
search = "esiea"

# create browser
browser = webdriver.Firefox()

# go to google search page
browser.get('https://www.google.com')

# wait for the "refuse" button to be available to select it, then click it
refuser = WebDriverWait(browser, 30).until(EC.presence_of_element_located(('id', 'W0wltc')))
refuser.send_keys(keys.Keys.ENTER)

# select the search bar
query_search = WebDriverWait(browser, 30).until(EC.presence_of_element_located(('name', 'q')))

# type the search in search bar 
query_search.send_keys(search)

# send the research
action = action_chains.ActionChains(browser)
action.send_keys(keys.Keys.ENTER)
action.perform()

# wait for the first result to be available
elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located(('xpath', '//h3')))

# select all results
elements = browser.find_elements(by='xpath', value='//h3')

# display results
for e in elements:
    print(e.text)