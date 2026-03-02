from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def run_test(username, password, expected_result, test_case_name):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # Enter credentials
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    if expected_result == "success":
        if "inventory" in driver.current_url:
            print(f"{test_case_name}: PASSED")
        else:
            print(f"{test_case_name}: FAILED")

    elif expected_result == "failure":
        try:
            error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
            if error_message.is_displayed():
                print(f"{test_case_name}: PASSED")
            else:
                print(f"{test_case_name}: FAILED")
        except:
            print(f"{test_case_name}: FAILED")

    driver.quit()


# --------- Test Cases ---------

# Positive Test Case
run_test("standard_user", "secret_sauce", "success", "Test Case 1 - Valid Login")

# Negative Test Cases
run_test("locked_out_user", "secret_sauce", "failure", "Test Case 2 - Locked Out User")
run_test("invalid_user", "secret_sauce", "failure", "Test Case 3 - Invalid Username")
run_test("standard_user", "wrong_password", "failure", "Test Case 4 - Invalid Password")
run_test("", "", "failure", "Test Case 5 - Empty Fields")