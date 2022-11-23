from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains, keys

# definition of the search
search = "esiea"

# set options to not be detected as a bot
option = webdriver.FirefoxOptions()
option.add_argument("window-size=1920,1080")
option.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0") # Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0

# create browser
browser = webdriver.Firefox(options=option)
browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

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



# close browser window
browser.quit()

## to check bot detection
# browser.get("https://amiunique.org/fp")
# browser.get('https://antcpt.com/score_detector/')