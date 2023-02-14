import time  #import selenium <<permet
from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#mecanisem d attente dynamique et globale
#driver.implicitly_wait(20)
#mecanisme d attente utiliser pour des condition il attent la presence d elenet si non il continue
#20c est le temp d attente et 2 le tempe d ayttent pour verifier si l element existe
#ignored_exceptions=[NoSuchElementException] pour eviter des exception
MyWait=WebDriverWait(driver,20,poll_frequency=2,ignored_exceptions=[Exception])
driver.get("https://www.google.ca")
#driver.find_element(By.XPATH,"//input[@name='q']").send_keys('selenium')
#driver.find_element(By.NAME,"q").send_keys('selenium')
#searhc_goole=driver.find_element(By.NAME,"q")
search_google=MyWait.until(EC.presence_of_element_located((By.NAME,"q")))
#search_google.submit()
#searhc_goole=driver.find_element(By.NAME,"q")
search_google.send_keys('selenium')
search_google.submit()
#result_link=driver.find_element(By.XPATH,"//h3[text()='Selenium']")
result_link=MyWait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
result_link.click()
driver.close()
