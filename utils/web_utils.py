from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def open_browser():
    driver = webdriver.Chrome()
    return driver

def find_element_by_id(driver, element_id):
    element = driver.find_element_by_id(element_id)
    return element

def fill_form(driver, form_id, data):
    form = driver.find_element_by_id(form_id)
    for key, value in data.items():
        input_element = form.find_element_by_name(key)
        input_element.clear()
        input_element.send_keys(value)

