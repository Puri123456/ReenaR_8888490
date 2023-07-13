from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Amazon website
driver.get('https://www.amazon.com/')

# Search for the shoe using a specific keyword
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')

search_box.send_keys('shoes')
search_button = driver.find_element(By.ID, 'nav-search-submit-button')
search_button.click()

# Wait for the search results to load
search_results = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')))

# Click on the first shoe in the search results
first_shoe = search_results[0]
first_shoe.click()

buy_now_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'buy-now-button')))
buy_now_button.click()

# Proceed to checkout
proceed_to_checkout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'hlb-ptc-btn-native')))
proceed_to_checkout_button.click()

# Fill in the sign-in details and complete the purchase process
# You will need to inspect the page elements and provide appropriate locators to interact with the sign-in and checkout forms

# Close the WebDriver
driver.quit()
