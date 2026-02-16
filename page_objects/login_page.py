import time
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.home_page import HomePage


class LoginPage(BasePage):
    """
    Represents the SauceDemo login page.

    Responsibilities:
    - Define element locators for the login page
    - Provide actions that can be performed on the login page
    - Provide a convenient login() method that performs the full login flow

    Notes:
    - Inherits from BasePage, which provides common functionality like click(), get_title(), wait, etc.
    """

    # ====================
    # LOCATORS
    # ====================
    # Locators define HOW Selenium finds elements on the page.
    # Tuples are used so we can unpack them with * when calling driver.find_element

    USERNAME_INPUT = (By.ID, "user-name")  # username input field
    PASSWORD_INPUT = (By.ID, "password")  # password input field
    LOGIN_BUTTON = (By.ID, "login-button")  # login button

    # ====================
    # CONSTRUCTOR
    # ====================
    def __init__(self, driver):
        """
        Initialize the LoginPage instance.

        :param driver: Selenium WebDriver instance
        """
        super().__init__(driver)  # Call BasePage constructor to initialize self.driver and self.wait

    # ====================
    # PAGE ACTIONS
    # ====================
    def open_url(self):
        """
        Navigate to the SauceDemo login page.

        Notes:
        - This is a simple helper method to open the URL
        - Added a short sleep to allow the page to load
        """
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(1)  # wait for page elements to appear (can be replaced by proper waits)

    def enter_username(self, username):
        """
        Enter text into the username field.

        :param username: string username to type
        """
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        """
        Enter text into the password field.

        :param password: string password to type
        """
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        """
        Click the login button.

        Notes:
        - Uses BasePage.click() which waits for the button to be clickable
        """
        self.click(self.LOGIN_BUTTON)

    # ====================
    # CONVENIENCE METHODS
    # ====================
    def login(self, username, password):
        """
        Perform the full login flow in one method call.

        Flow:
        1. Enter username
        2. Enter password
        3. Click login button
        4. Return HomePage object

        :param username: string username
        :param password: string password
        :return: HomePage instance (represents the page after successful login)
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        # After login, the browser navigates to the HomePage.
        # Return a HomePage object so the caller can continue interacting with the homepage.
        return HomePage(self.driver)
