from selenium import webdriver
import time
from selenium.webdriver.common.by import By



from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

websiteURL = 'https://x.com/home'

driver.get(websiteURL)
time.sleep(5)

clickableElement = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]/div/div/svg/g/path')
clickableElement(0).click()

time.sleep(5)
driver.back()
time.sleep(1)
driver.forward()
