import time  #import selenium <<permet
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
time.sleep(2)
driver.switch_to.frame("packageListFrame")
time.sleep(2)
driver.find_element(By.LINK_TEXT,'org.openqa.selenium').click()
driver.switch_to.default_content()
#driver.switch_to.frame("packageFrame")
driver.switch_to.frame(1)
time.sleep(2)
driver.find_element(By.LINK_TEXT,"WebDriver").click()
time.sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_elements(By.TAG_NAME,'iframe')[2])
#driver.switch_to.frame(2)
#driver.switch_to.default_content()
time.sleep(2)
driver.find_element(By.XPATH,"//a[text()='Help']").click()
time.sleep(3)
driver.close()
