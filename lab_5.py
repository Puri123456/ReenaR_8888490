

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.in")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("smartphones")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(2)

# Verifying that the search results page has loaded
assert "smartphones" in driver.title

# Selecting smartphones from the search results
smartphones_link = driver.find_element("xpath","/html/body/div[4]/div[2]/div[3]/div[10]/div[3]/div[1]/div/div/div[2]/div[1]/div[1]/ul/li[1]/span/span/div/img")
# smartphones_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a"
smartphones_link.click()

# Waiting for the smartphones details page to load
time.sleep(2)

# Clicking on "checkout" button
checkout_button = driver.find_element("id","checkout-button")
checkout_button.click()

# Waiting for the checkout page to load
time.sleep(2)

# Entering a new shipping address
address_field = driver.find_element("id", "address-ui-widgets-enterEmailFullName")
address_field.send_keys("Your Name")

# Waiting for the returns page to load
time.sleep(1)

# Closing the webdriver
driver.close()
