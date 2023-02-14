import time  #import selenium <<permet
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
driver.find_element(By.NAME,'username').send_keys('Admin')
time.sleep(4)
driver.find_element(By.NAME,'password').send_keys('admin123')
time.sleep(4)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(4)
#find_elements pluseur elements
list_lien=driver.find_elements(By.TAG_NAME,'a')
print(len(list_lien))
time.sleep(4)
for lien in list_lien:
    print(lien.text)
driver.close()