import time

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
product=input("enter product to be searched")
driver  = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
print("Test case started")
driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
driver.find_element_by_name(("q")).send_keys(product)
driver.find_element_by_class_name("L0Z3Pu").click()
time.sleep(25)
driver.close()
