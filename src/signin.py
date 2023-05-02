import os, time
from selenium.webdriver.common.by import By


def login(test_driver, logger):
    logger.debug(f"Logging in")
    UPWORK_LOGIN_URL = os.getenv("UPWORK_LOGIN_URL")
    test_driver.get(UPWORK_LOGIN_URL)

    time.sleep(2)
    username_box = test_driver.find_element(By.XPATH, '//*[@id="login_username"]')
    UPWORK_EMAIL = os.getenv("UPWORK_EMAIL")
    username_box.send_keys(UPWORK_EMAIL)
    time.sleep(2)

    continue_with_email_box = test_driver.find_element(
        By.XPATH, '//*[@id="login_password_continue"]'
    )
    continue_with_email_box.click()
    time.sleep(2)

    password_box = test_driver.find_element(By.XPATH, '//*[@id="login_password"]')
    UPWORK_PASSWORD = os.getenv("UPWORK_PASSWORD")
    password_box.send_keys(UPWORK_PASSWORD)
    time.sleep(2)

    submit_password_box = test_driver.find_element(
        By.XPATH, '//*[@id="login_control_continue"]'
    )
    submit_password_box.click()
    time.sleep(5)