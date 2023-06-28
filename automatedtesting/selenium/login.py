# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# Start the browser and login with standard_user
def login (driver, user, password):
    driver.get('https://www.saucedemo.com/')
    username = driver.find_element(by=By.XPATH, value='//*[@id="user-name"]')
    username.send_keys(user)
    passwordE = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
    passwordE.send_keys(password)
    button = driver.find_element(by=By.XPATH, value='//*[@id="login-button"]')
    button.click()


def add_items(driver):
    products = driver.find_element(by=By.CSS_SELECTOR, value='#inventory_container > div').find_elements(by=By.CLASS_NAME, value='inventory_item')
    for product in products:
        button_add = product.find_element(by=By.TAG_NAME, value='button')
        button_add.click()
        item_name = product.find_element(by=By.CLASS_NAME, value='inventory_item_name').text
        print(item_name, 'added to shopping cart.')
        time.sleep(1)


def remove_items(driver):
    products = driver.find_element(by=By.CSS_SELECTOR, value='#inventory_container > div').find_elements(by=By.CLASS_NAME, value='inventory_item')
    for product in products:
        button_add = product.find_element(by=By.TAG_NAME, value='button')
        button_add.click()
        item_name = product.find_element(by=By.CLASS_NAME, value='inventory_item_name').text
        print(item_name, 'removed to shopping cart.')
        time.sleep(1)


def get_number_items_in_cart(driver):
    cart = driver.find_element(by=By.ID, value='shopping_cart_container')
    number_items = int(cart.text) if cart.text != '' else 0
    print('Number of items in shopping cart is', number_items)
    return number_items


if __name__=="__main__":
    options = ChromeOptions()
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    # driver = webdriver.Chrome(service=service)
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

    # login
    login(driver, 'standard_user', 'secret_sauce')
    print("Logged in successful!")

    # add all items
    add_items(driver)
    number_items = get_number_items_in_cart(driver)
    if number_items == 6:
        print("We added all items into shopping cart successfully!")
    else:
        print("Failed to add all item into shopping cart!")

    # remove all item from cart
    remove_items(driver)
    number_items = get_number_items_in_cart(driver)
    if number_items == 0:
        print("We removed all items from shopping cart successfully!")
    else:
        print("Failed to remove all items from shopping cart!")



# login('standard_user', 'secret_sauce')