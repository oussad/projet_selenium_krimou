import time  #import selenium <<permet
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
palceholder_text=driver.find_element(By.XPATH,'//input[@name="username"]').get_attribute('placeholder')
print(palceholder_text)
time.sleep(4)
list_lien=driver.find_elements(By.TAG_NAME,'a')
time.sleep(4)
print(len(list_lien))
for element in list_lien:
    print(element.get_attribute('href'))
time.sleep(4)
driver.close()