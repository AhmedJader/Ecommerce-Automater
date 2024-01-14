from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://ahmedjader.github.io/Refined-Ecommerce-Web-App/")


input_element = driver.find_element(By.CLASS_NAME, "input")
link = driver.find_element(By.CLASS_NAME, "HOVER")

time.sleep(3)

counter = 1

while True:
    input_element.clear()
    input_element.send_keys(str(counter))

    link.click()

    time.sleep(2.5)  # You might want to adjust the sleep time based on your application's needs

    counter += 1

    if counter > 20:
        counter = 1
