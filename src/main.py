from selenium.webdriver.common.by import By
import time, os
from bs4 import BeautifulSoup
import urllib.request
import pickle
from custom_logging import logger
from custom_webdriver import test_driver
from apply_job import apply_to_job
from dotenv import load_dotenv
from selenium.common.exceptions import (
    NoSuchElementException,
)


class UpworkBot:
    def __init__(self, dry_run=True):
        self.dry_run = dry_run
        self.original_window = test_driver.current_window_handle
        self.login()
        self.go_to_search()
        self.pickle_search_results()
        self.links = self.parse_soup()
        self.apply_to_jobs()

    def login(self):
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

    def go_to_search(self):
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
        test_driver.get(UPWORK_SEARCH_URL)
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
            if window_handle != self.original_window:
                test_driver.switch_to.window(window_handle)

    def pickle_search_results(self):
        logger.debug(f"Pickle the results")
        html_page = test_driver.page_source
        RSS_url = test_driver.current_url

        with open("url_RSS.txt", "w", encoding="UTF-8") as f:
            f.write(RSS_url)

        soup = BeautifulSoup(urllib.request.urlopen(RSS_url))
        # Open a file and use dump()

        with open("file.pkl", "wb") as file:
            # A new file will be created
            pickle.dump(soup, file)

        with open("html_page.html", "w", encoding="UTF-8") as f:
            f.write(html_page)

    # save progress in a pickle
    def parse_soup(self):
        logger.debug(f"Parse the html")
        # Open the file in binary mode
        with open("file.pkl", "rb") as file:
            # Call load method to deserialze
            pickled_soup = pickle.load(file)
        links_found = []
        for lnk in pickled_soup.find_all("link"):
            a_tag = lnk.next
            if "https://www.upwork.com/jobs/" in a_tag:
                links_found.append(a_tag)
        logger.debug(f"Appending {len(links_found)} that I just found")
        return links_found

    def apply_to_jobs(self):
        logger.debug(f"Applying for the jobs")
        for link in self.links:
            apply_to_job(link, test_driver, logger, self.dry_run)
            logger.debug(f"Going to the next link")


if __name__ == "__main__":
    load_dotenv()
    UpworkBot()

# add parameter to sort by highest paying? or most spent? most recent?
# parse more urls
# put configuration in yaml
# list what i applied to into a new log file
# docker
# comment my code
