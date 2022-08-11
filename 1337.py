from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys

s = Service("D:\chromedriver_win32\chromedriver.exe")
my_driver = webdriver.Chrome(service=s)
# my_driver = webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")
# for i in range(5):
#     my_driver.get("https://github.com/avielb")
#     sleep(5)
#     my_driver.refresh()
# my_driver.close()
my_driver.get(r"D:\Downloads\tip_calc\index.html")
my_driver.find_element(by="id", value="billamt").send_keys("100")
my_driver.find_element(by="xpath", value='//*[@id="serviceQual"]/option[2]').click()
my_driver.find_element(by="id", value="peopleamt").send_keys("3")
sleep(3)
my_driver.find_element(by="id", value="calculate").click()

temp = my_driver.find_element(by="id", value="billamt").text
my_driver.close()
print(temp)