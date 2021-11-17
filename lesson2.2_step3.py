from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import Select
try:

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_elem=browser.find_element_by_id("num1")
    x=x_elem.text
    y_elem=browser.find_element_by_id("num2")
    y=y_elem.text
    x=int(x)+int(y)
    x=str(x)
    print(x)
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value=x]").click()
    browser.find_element_by_class_name("btn").click()

finally:
    sleep(5)
    browser.quit()
