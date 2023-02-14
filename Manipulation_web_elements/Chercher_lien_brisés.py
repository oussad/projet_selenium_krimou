import time  #import selenium <<permet
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
list_link=driver.find_elements(By.TAG_NAME,'a')
compteur=0
for lien in list_link:
    URL=lien.get_attribute('href')
    try:
        reponse = requests.head(URL)
    except:
        None
    if reponse.status_code>=400:
        print(URL,' est un lien brisé')
        compteur=compteur+1
        nom_lien=lien.get_attribute('href')
    else:
        print(URL,'le lien valide')

print("le nombres de lien brisé est =",compteur,nom_lien)
driver.close()
