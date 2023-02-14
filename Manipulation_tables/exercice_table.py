import time  #import selenium <<permet
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.NAME,'username').send_keys('Admin')
time.sleep(2)
driver.find_element(By.NAME,'password').send_keys('admin123')
time.sleep(2)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//span[text()="Admin"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//span[text()="User Management "]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//a[text()="Users"]').click()
time.sleep(4)
nombres_lignes=driver.find_elements(By.XPATH,'//div[@class="oxd-table-body"]/div')
for data in range(1,len(nombres_lignes)+1):
    data1=driver.find_element(By.XPATH,'//div[@class="oxd-table-body"]/div[" + str(data) + "]').text
    print(data1)
    data2=driver.find_element(By.XPATH,'//div[@class="oxd-table-body"]/div[" + str(data) + "]').text

print(len(nombres_lignes))
driver.close()