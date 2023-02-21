import sys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Setup Chrome driver options
chrome_options = Options()
chrome_options.add_argument("--window-size=700,5080")

#Set argument variable as profile ID
profile_id = sys.argv[1]

profile_url = f"https://steamcommunity.com/profiles/{profile_id}/inventory/"

driver = webdriver.Chrome(chrome_options=chrome_options)

try:
    driver.get(profile_url)
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#acceptAllButton"))
    ).click()
    select = Select(driver.find_element(By.CSS_SELECTOR,"#responsive_inventory_select")) # Create Select instance to work with dropdown
    select.select_by_value('#730') # Choose CSGO 
    web_element_list = driver.find_elements(By.CSS_SELECTOR,".item.app730.context2")
except Exception as e:
    print(e)

items = []
for web_element in web_element_list:
    id_ = web_element.get_attribute('id')
    WebDriverWait(
        driver,1).until(EC.element_to_be_clickable((By.CSS_SELECTOR,f'[href="#{id_}"]'))
    ).click()
    desc = driver.find_element(By.CSS_SELECTOR,"#iteminfo1_item_name").text
    items.append(desc)
    WebDriverWait(
        driver,1).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".economy_item_popup_dismiss"))
    ).click()

print(web_element_list)
print("finish")
driver.quit()