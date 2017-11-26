import os

from selenium import webdriver

drvier=webdriver.Chrome(executable_path="./chromedriver")

drvier.get ("https://www.baidu.com/")
baiduserach=drvier.find_element_by_id("kw")
baiduserach.send_keys("helloworld")