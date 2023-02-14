import time  #import selenium <<permet
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")
time.sleep(4)
#permet de voir si le checkbos avtive ou non
check_box=driver.find_element(By.ID,'checkbox1').is_selected()
print(check_box)
check_box1=driver.find_element(By.ID,'checkbox2').is_selected()
print(check_box1)
#permet de voir si le element est visble ou non
check_enable=driver.find_element(By.ID,'but1').is_enabled()
print(check_enable)
#permet de voir si le bouton active ou non
check_displaye=driver.find_element(By.ID,'hbutton').is_displayed()
print(check_displaye)
driver.close()
