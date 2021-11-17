from time import sleep

from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.find_element_by_class_name("btn").click()
    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)
    x_element=browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    elem=browser.find_element_by_tag_name("input")
    elem.send_keys(y)
    elem=browser.find_element_by_class_name("btn").click()

finally:
    sleep(5)
    browser.quit()
