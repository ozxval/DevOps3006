# import requests
# import names
# # response = requests.get("https://api.github.com/users/avielb/repos")
# # # for repo in response.json()
# #
# # if len(response.json()) >= 5:
# #     print("there is more than 5 repositories")
# # else:
# #     print("thee is less than 5 repositories")
# # response.close()
# # for i in range(3):
# #     temp = requests.get(f"https://api.agify.io/?name={names.get_first_name()}").json()
# #     if 0 <= temp["age"] <= 120:
# #         print("age is right")
# #     else:
# #         print("age is not right")
# temp_link = requests.get("http://universities.hipolabs.com/search")
# print(len(temp_link.json()))
import requests
from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument('headless')
yco = webdriver.Chrome("D:/chromedriver_win32/chromedriver.exe", options=option)
yco.get("https://www.ycombinator.com/")
print(yco.title)