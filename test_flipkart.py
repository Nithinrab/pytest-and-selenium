import pytest

import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture
def setup():
    global product,driver
    product = input("enter product to be searched")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()
def test_searchproducts(setup):
    driver.get("https://www.flipkart.com/")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    driver.find_element_by_name(("q")).send_keys(product)
    driver.find_element_by_class_name("L0Z3Pu").click()
    time.sleep(5)
    action = ActionChains(driver)
    action.context_click(driver.find_element_by_name("q"))
    action.perform()

