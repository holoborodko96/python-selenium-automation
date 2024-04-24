# test case to verify that Users can navigate to SignIn page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()
driver.find_element(By.XPATH, "//span[@class='styles__ListItemText-sc-diphzn-1 jaMNVl']").click()
sleep(5)

actual_text = driver.find_element(By.XPATH, "//span").text
assert 'Sign into your Target account' in actual_text
print('Test case passed')

driver.find_element(By.ID, 'login')
