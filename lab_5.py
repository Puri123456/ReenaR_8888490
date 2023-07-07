# Importing required libraries

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time


# Setting up the webdriver

driver = webdriver.Chrome()


# Navigating to the Amazon.ca homepage

driver.get("https://www.amazon.ca")

time.sleep(2)


# Finding the search bar and entering text

search_bar = driver.find_element("id", "twotabsearchtextbox")

search_bar.send_keys("air+conditioning")


# Submitting the search query

search_bar.send_keys(Keys.RETURN)


# Waiting for the search results page to load

time.sleep(3)


# Verifying that the search results page has loaded

assert "air+conditioning" in driver.title


# Selecting an air+conditioning from the search results

aircon_link = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/span/a/div/img")

aircon_link.click()



# Waiting for the air+conditioning details page to load

time.sleep(5)


# Clicking on the "Buy Now" button

buy_now_button = driver.find_element("id", "buy-now-button")

buy_now_button.click()


# Waiting for the checkout page to load

time.sleep(2)


# Entering a new shipping address

address_field = driver.find_element("id", "address-ui-widgets-enterEmailFullName")

address_field.send_keys("Your Name")


# Waiting for the returns page to load

time.sleep(1)

# Closing the webdriver

driver.close()
