import json
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from rich import print

# ================================
# Load test data from JSON file
# ================================
test_data_path = "test_data/test_data.json"
with open(test_data_path) as f:
    data = json.load(f)


# ================================
# Test: Verify all users can log in
# ================================
def test_user_can_login(driver):
    """
    This test verifies that users listed in the JSON file
    can log in to SauceDemo and are navigated to the HomePage successfully.

    Flow:
    1. Open SauceDemo login page
    2. Enter username and password
    3. Click login
    4. Verify login was successful
    5. Perform some actions on the HomePage
    """

    # ------------------------------
    # Loop through all users in the JSON file
    # ------------------------------
    for user in data["users"]:
        # 1. Quit and restart the browser for each user
        driver.delete_all_cookies()
        driver.refresh()  # optional, makes sure no session remains

        #Look inside the user dictionary
        # Get the value for "userName"
        # Store it in username
        username = user["userName"]
        password = user["password"]

        print(f"[blue]🔑 Logging in as: {username}[/blue]")

        # ------------------------------
        # Initialize a fresh LoginPage for each user
        # ------------------------------
        login_page = LoginPage(driver)
        login_page.open_url()

        # ------------------------------
        # Perform login
        # ------------------------------
        home_page = login_page.login(username, password)

        # ------------------------------
        # Verify login was successful
        # ------------------------------
        title = home_page.get_title()
        print(f"[green]🏠 Page title after login: {title}[/green]")

        assert title == "Swag Labs", (
            f"Login failed for user: {username}. "
            f"Expected page title 'Swag Labs', got '{title}'"
        )

        home_page.is_this_page_loaded()
        print(f"[cyan]🚀 User {username} navigated to the HomePage successfully[/cyan]")

        # ------------------------------
        # Perform some actions on HomePage
        # ------------------------------
        home_page.click_add_to_cart_button()

        # ------------------------------
        # Reset session for next user
        # ------------------------------
        driver.delete_all_cookies()
