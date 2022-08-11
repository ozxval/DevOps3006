from selenium import webdriver

my_driver = webdriver.Chrome(executable_path="D:/chromedriver_win32/chromedriver.exe")
my_driver.get("D:/Downloads/tip_calc/index.html")
billamt = my_driver.find_element(by="id", value="billamt")
billamt.send_keys("100")
my_driver.find_element(by="xpath", value='//*[@id="serviceQual"]/option[4]').click()
my_driver.find_element(by="id", value="peopleamt").send_keys("2")
my_driver.find_element(by="id", value="calculate").click()
expected = "7.50"
actual = my_driver.find_element(by="id", value="tip").text

assert actual != expected