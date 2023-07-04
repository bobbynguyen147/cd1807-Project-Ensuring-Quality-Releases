# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from datetime import datetime

def CustomPrint(message):
    print (datetime.now().strftime("%d/%m/%Y, %H:%M:%S")  + ' (INFO): ' + message)

# Start the browser and login with standard_user
def login (user, password):
     
    CustomPrint('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    # driver = webdriver.Chrome(options=options)
    chromedriver = "/usr/lib/chromium-browser/chromedriver"
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    CustomPrint('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element("id",'user-name').send_keys(user)
    driver.find_element("id",'password').send_keys(password)
    driver.find_element("id",'login-button').click()
    CustomPrint('Login successfully')

    CustomPrint('Choose all items')
    items = driver.find_elements("class name",'inventory_item')
    for item in items:
        name = item.find_element("class name",'inventory_item_name')
        CustomPrint('Add ' + name.text + ' to cart')
        item.find_element("class name",'btn_inventory').click()
    
    CustomPrint('Go to cart')
    driver.find_element("class name",'shopping_cart_link').click()
    removes = driver.find_elements("class name", "cart_item")
    for remove in removes:
        name = remove.find_element("class name",'inventory_item_name')
        CustomPrint('Remove ' + name.text + ' from cart')
        remove.find_element("class name",'cart_button').click()

    CustomPrint('Done')

login('standard_user', 'secret_sauce')

