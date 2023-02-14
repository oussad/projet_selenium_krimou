import time  #import selenium <<permet
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#mecanisem d attente dynamique et globale
driver.implicitly_wait(20)
driver.get("https://www.google.ca")
#time.sleep(4)
#driver.find_element(By.XPATH,"//input[@name='q']").send_keys('selenium')
#driver.find_element(By.NAME,"q").send_keys('selenium')
#searhc_goole=driver.find_element(By.NAME,"q")
searhc_goole=driver.find_element(By.NAME,"q")
searhc_goole.send_keys('selenium')
searhc_goole.submit()

#time.sleep(3)
result_link=driver.find_element(By.XPATH,"//h3[text()='Selenium']")
result_link.click()
#time.sleep(2)
driver.close()
