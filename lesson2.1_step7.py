from time import sleep

from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    elem=browser.find_element_by_id("treasure")
    x=elem.get_attribute("valuex")
    #x = x_element.text
    y = calc(x)
    elem=browser.find_element_by_tag_name("input")
    elem.send_keys(y)
    elem=browser.find_element_by_css_selector("input[type='checkbox']").click()
    elem=browser.find_element_by_id("robotsRule").click()
    elem=browser.find_element_by_class_name("btn").click()

finally:
    sleep(5)
    browser.quit()

