from time import sleep

from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

  browser = webdriver.Chrome()
  link = "https://SunInJuly.github.io/execute_script.html"
  browser.get(link)
  elem=browser.find_element_by_id("input_value")
  x=elem.text
  elem=browser.find_element_by_id("answer")
  elem.send_keys(calc(x))
  elem=browser.find_element_by_css_selector("input[type='checkbox']").click()
  button = browser.find_element_by_class_name("btn")
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  elem=browser.find_element_by_id("robotsRule").click()
  button.click()

finally:
  sleep(5)
  browser.quit()