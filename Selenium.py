from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service() #Service class object
webdriver.Chrome()
driver=webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.find_element(By.NAME,"Email").clear()
driver.find_element(By.NAME,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
actual_title=driver.title
expected_title="Dashboard / nopCommerce administration"

if actual_title==expected_title:
    print("Login Test Passed")
else:
    print("Test Failed")
driver.close()







