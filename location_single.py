from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = 'laptop'
driver.get(f'https://www.amazon.in/s?k={query}&i=specialty-aps&srs=26966830031&crid=3LH7JI920TH09&sprefix=lapt%2Cspecialty-aps%2C243&ref=nb_sb_noss_2')
elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
print(elem.get_attribute('outerHTML'))


time.sleep(8)
driver.close()