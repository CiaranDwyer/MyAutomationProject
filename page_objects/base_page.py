from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    BasePage is the parent class for all page objects.
    It provides common methods like click, get_title, and alert handling,
    and stores a WebDriver instance and explicit wait for reuse across pages.
    """

    def __init__(self, driver):
        """
        Constructor for BasePage.

        :param driver: Selenium WebDriver instance for controlling the browser
        """
        # Store the WebDriver instance for use in child pages
        self.driver = driver

        # Create a reusable explicit wait (default: 10 seconds)
        # This is used for waiting for elements or conditions to occur before interacting
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        """
        Waits for an element to be clickable, then clicks it.

        :param locator: Tuple to locate element, e.g., (By.ID, "element_id") or (By.CSS_SELECTOR, "css")

        ✅ When to use:
            - Clicking buttons or links
            - Submitting forms
            - When element timing/loading is unpredictable

        ❌ When NOT to use:
            - Checking text or presence of element
            - When you need the element to be visible but not necessarily clickable
        """
        # Wait until the element is clickable, then perform click
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_title(self):
        """
        Returns the title of the current page.

        Useful for verifying navigation or ensuring that the correct page is loaded.
        """
        return self.driver.title

    def accept_alert(self):
        """
        Waits for a JavaScript alert to appear and accepts it (clicks OK).

        ✅ Use this when handling JS popups like:
            - Alerts
            - Confirm dialogs
            - Prompt dialogs (accepts without entering text)
        """
        # Wait until an alert is present
        alert = self.wait.until(EC.alert_is_present())

        # Accept the alert (click "OK")
        alert.accept()
