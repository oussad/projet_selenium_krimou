import time  #import selenium <<permet


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(4)
#recupération le nombres de lignes et colonnes d une table
nombres_lignes=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print(len(nombres_lignes))
nombres_colonnes=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
print(len(nombres_colonnes))
#recpére la velus d une cellue de la table
valeur_celle=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[3]/td[1]")
print(valeur_celle.text)
#recupére toutes les données du tableau
nb_lignes=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
nb_colonnes=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
valeur_head=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
"""for i in range(1,len(valeur_head)+1):
    data_head=driver.find_element(By.XPATH,"//table[@name='BookTable']//th["+str(i)+"]").text
    print(data_head)"""
time.sleep(3)
#recupéré des valeurs recherche
for r in range(2,nb_lignes+1):
    auteur=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text

    if auteur=='Amit':
        prix = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[4]").text
        nom_livre = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[1]").text
        print(auteur,"**********",nom_livre,"*********",prix)


driver.close()