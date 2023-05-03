import os, time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
)

def go_to_search(test_driver, logger, original_window):
    logger.debug(f"Start searching")
    try:
        close_annoying_window_box = test_driver.find_element(
            By.XPATH,
            '//*[@id="main"]/div[2]/div[4]/aside/div/div[1]/div/section/div[2]/div[2]/div/div/div/div[2]/button',
        )
        close_annoying_window_box.click()
        time.sleep(2)
    except NoSuchElementException:
        logger.debug(f"Could not find the close_annoying_window_box")

    UPWORK_SEARCH_URL = os.getenv("UPWORK_SEARCH_URL")
    SORT_SEARCH_BY = os.getenv("SORT_SEARCH_BY")
    INCLUDE_KEYWORDS_IN_SEARCH = os.getenv("INCLUDE_KEYWORDS_IN_SEARCH")
    EXCLUDE_KEYWORDS_IN_SEARCH = os.getenv("EXCLUDE_KEYWORDS_IN_SEARCH")
    GO_TO_URL = f"{UPWORK_SEARCH_URL}?sort={SORT_SEARCH_BY}&or_terms={INCLUDE_KEYWORDS_IN_SEARCH}&exclude_terms={EXCLUDE_KEYWORDS_IN_SEARCH}"
    # test_driver.get(UPWORK_SEARCH_URL)
    test_driver.get(GO_TO_URL)
    time.sleep(4)
    try:
        click_rss_icon_box = test_driver.find_element(
            By.XPATH, '//*[@id="dropdown-secondary-label-1"]'
        )
        click_rss_icon_box.click()
        time.sleep(2)
    except NoSuchElementException as e:
        logger.error(f"Cant locate click_rss_icon_box")
        logger.error(f"{e}")
        raise
    try:
        click_rss_icon_again_box = test_driver.find_element(
            By.XPATH,
            '//*[@id="popper_1"]/div/div/div/div[1]/div/div/div/div/div/div/ul/li[1]',
        )
        click_rss_icon_again_box.click()
        time.sleep(2)
    except NoSuchElementException:
        logger.debug(f"Could not find the click_rss_icon_again_box")

    for window_handle in test_driver.window_handles:
        if window_handle != original_window:
            test_driver.switch_to.window(window_handle)