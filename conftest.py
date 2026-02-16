import time
import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# =====================================================
# DRIVER FIXTURE - Starts and stops the  browser
# =====================================================
@pytest.fixture
def driver():
    """
    Pytest fixture to provide a Selenium WebDriver instance to tests.
    """

    # -----------------------------
    # Step 1: Configure Chrome Options
    # -----------------------------
    options = webdriver.ChromeOptions()

    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--disable-notifications")

    options.add_experimental_option(
        "prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )

    # -----------------------------
    # Step 2: Create Chrome WebDriver
    # -----------------------------
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()

    # -----------------------------
    # Step 3: Provide driver to test
    # -----------------------------
    yield driver

    # -----------------------------
    # Step 4: Teardown
    # -----------------------------
    driver.close()
    driver.quit()


# =====================================================
# SCREENSHOT ON TEST FAILURE
# =====================================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    This hook runs after each test.
    If the test fails, it takes a screenshot.
    """

    # Execute the test and get the result
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot if the test itself failed
    if report.when == "call" and report.failed:

        # Get the driver used in the test (if any)
        driver = item.funcargs.get("driver", None)
        if driver is None:
            return

        # Create screenshots folder if it doesn't exist
        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        # Create screenshot file name
        test_name = item.name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = f"{screenshots_dir}/{test_name}_{timestamp}.png"

        # Take screenshot
        driver.save_screenshot(screenshot_path)

        print(f"\n📸 Screenshot saved: {screenshot_path}")
