import time  #import selenium <<permet

from select import select
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.imdb.com/video/")
time.sleep(4)
driver.find_element(By.XPATH,"(//*[@id='iconContext-arrow-drop-down'])[1]").click()
time.sleep(3)
liste_li=driver.find_elements(By.TAG_NAME,'span')
print('la liste des li',len(liste_li))
for element in liste_li:
    #print(element.text)
    if (element.text=='Recherche avancée'):
        element.click()
        break
time.sleep(3)
driver.find_element(By.XPATH,"//a[text()='Advanced Title Search']").click()
driver.find_element(By.XPATH,"//input[@name='title']").send_keys('action')
"""list_TD=driver.find_elements(By.TAG_NAME,'td')
print(len(list_TD))
for element in list_TD:
    print(element.text)"""
check_box1=driver.find_element(By.XPATH,"(//input[@name='title_type'])[1]").click()
status_check_box1=driver.find_element(By.XPATH,"(//input[@name='title_type'])[1]").is_selected()
print(status_check_box1)
time.sleep(3)
check_box1=driver.find_element(By.XPATH,"(//input[@name='title_type'])[6]").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='release_date-min']").send_keys('1998-01-01')
driver.find_element(By.XPATH,"//input[@name='release_date-max']").send_keys('2023-01-01')
liste_déroulante1=driver.find_elements(By.NAME,"user_rating-min")
print(len(liste_déroulante1))
for element in liste_déroulante1:
    #print(element.text)
    if element.text == '1.0':
        element.click()
        break
liste_déroulante2=select(driver.find_elements(By.NAME,"user_rating-max"))
liste_déroulante2.
driver.close()