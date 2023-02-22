import sys
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scroll_down(driver):
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(0.1)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height

#Setup Chrome driver options
chrome_options = Options()
chrome_options.add_argument("--window-size=700,5080")

#Set argument variable as profile ID
profile_id = sys.argv[1]

profile_url = f"https://steamcommunity.com/profiles/{profile_id}/inventory/"

driver = webdriver.Chrome(chrome_options=chrome_options)

try:
    driver.get(profile_url)
    select = Select(driver.find_element(By.CSS_SELECTOR,"#responsive_inventory_select")) # Create Select instance to work with dropdown
    select.select_by_value('#730') # Choose CSGO 
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#acceptAllButton"))
    ).click()
    scroll_down(driver)
    time.sleep(3) # When we have number of items we can create wait conditions
    web_element_list = driver.find_elements(By.CSS_SELECTOR,".item.app730.context2")
except Exception as e:
    print(e)



""" for web_element in web_element_list:
    id_ = web_element.get_attribute('id')
    try:
        WebDriverWait(
            driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,f'[href="#{id_}"]'))
        ).click()
        desc = driver.find_element(By.CSS_SELECTOR,"#iteminfo1_item_name").text
        if desc == '':
            desc = driver.find_element(By.CSS_SELECTOR,"#iteminfo0_item_name").text
        items.append(desc)
        WebDriverWait(
            driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".economy_item_popup_dismiss"))
        ).click()
    except Exception as e:
        print(e)
        error_list.append(id_)
time.sleep(1)
try: 
    WebDriverWait(
            driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,f'[href="#{error_list[0]}"]'))
        ).click()
    desc = driver.find_element(By.CSS_SELECTOR,"#iteminfo1_item_name").text
    items.append(desc)
    WebDriverWait(
                driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".economy_item_popup_dismiss"))
            ).click()
except Exception as e:
    print(e) """

print("finish")
driver.quit()