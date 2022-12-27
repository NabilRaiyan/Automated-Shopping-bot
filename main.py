from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

driver_path = "F:\Software\chromedriver_win32.exe"

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=option)

driver.get("https://nabatechshop.com/")

search = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div/div/div[2]/div/form/input[1]')
search.send_keys("arduino")
search.send_keys(Keys.ENTER)

time.sleep(2)

item1 = driver.find_element(By.LINK_TEXT, "L293D Motor Driver Shield For Arduino")
item1.click()

time.sleep(1)

item1_add_to_cart = driver.find_element(By.NAME, 'add-to-cart')
item1_add_to_cart.send_keys(Keys.ENTER)
time.sleep(3)

show_cart = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div/div/div[3]/div[3]/a')
show_cart.send_keys(Keys.ENTER)

time.sleep(3)

home = driver.find_element(By.XPATH, '//*[@id="menu-item-11577"]/a')
home.send_keys(Keys.ENTER)

time.sleep(3)

driver.quit()