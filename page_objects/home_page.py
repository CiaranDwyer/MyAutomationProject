import time

from selenium.webdriver.common.alert import Alert

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

# 🏗️ Step 1: Return the HomePage Object
# 🏗️ Step 2: Create the HomePage Object Page
# 🧩 Step 3: Import HomePage into LoginPage
# 🧩 Step 4: Verify the HomePage is Loaded
# 🧩 Step 5: Add is_loaded() to every page

class HomePage(BasePage):

    HOMEPAGE_CONTAINER = (By.ID, 'inventory_container')
    ADD_TO_CART = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")

    def is_this_page_loaded(self):
        """Confirm that home page is loaded"""
        return self.wait.until(
            lambda driver: driver.find_element(*self.HOMEPAGE_CONTAINER)
        )

    def click_add_to_cart_button(self):
        self.click(self.ADD_TO_CART)
        time.sleep(2)

