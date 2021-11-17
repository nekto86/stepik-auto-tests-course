import os
from time import sleep

from selenium import webdriver

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir , file_name)

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    browser.find_element_by_css_selector("input[name='firstname']").send_keys("Dmitry")
    browser.find_element_by_css_selector("input[name='lastname']").send_keys("Goryainov")
    browser.find_element_by_css_selector("input[name='email']").send_keys("test@test.ru")
    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_class_name("btn").click()

finally:
    sleep(5)
    browser.quit()
