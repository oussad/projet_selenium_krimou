import time  #import selenium <<permet
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
list_link=driver.find_elements(By.TAG_NAME,'a')
print("nombre de lien sur la page ",len(list_link))
for element in list_link:
    print(element.text)
    print(element.get_attribute('href'))
print(list_link[3].text)
driver.close()
