from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.target.com/')

driver.find_element(By.ID, 'search').send_keys('coffe')

driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

sleep(5)

actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
assert 'coffe' in actual_text
print('Test case passed')

sleep(10)
