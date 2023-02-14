import time  #import selenium <<permet
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
driver.get("https://google.ca")
time.sleep(4)
driver.back()
time.sleep(4)
driver.forward()
time.sleep(4)
driver.refresh()
time.sleep(4)
driver.close()