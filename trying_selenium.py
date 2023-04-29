#import os
import time
#driver_service = Service(executable_path=r"C:\Users\papti\chromedriver_win32\chromedriver.exe")
#driver_service = Service(executable_path=ChromeDriverManager().install())
#driver = webdriver.Chrome(service=driver_service)

#os.environ["PATH"] += r"C:\Users\papti"
#driver = webdriver.Chrome(executable_path=r"C:\Users\papti\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Chrome()
#search = driver.find_element(by=By.CLASS_NAME, value="s")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://www.techwithtim.net/")
print(driver.title)

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/aside[1]/form/label/input").send_keys("test" + Keys.RETURN)

driver.quit()
