import pickle
import time
import os
from journal import logger
from chromewebdriver import test_driver
from signin import login
from search import go_to_search
from add_questions import fill_out_text_boxes
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import urllib.request
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
)
from selenium.webdriver.common.by import By


class UpworkBot:
    def __init__(self, dry_run=True):
        self.successful_run = 0
        self.failed_run = 0
        self.skipped_run = 0
        self.dry_run = dry_run
        original_window = test_driver.current_window_handle
        login(test_driver, logger)
        
        go_to_search(test_driver, logger, original_window)
        self.pickle_search_results()
        self.links = self.parse_soup()

        self.apply_to_jobs()


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
            self.apply_to_job(link)
            logger.debug(f"{self.successful_run} successfully applied and failed to apply {self.failed_run} times and skipped {self.skipped_run}")
            logger.debug(f"Going to the next link")

    def apply_to_job(self, link):
        # go to URL
        skipping = False
        test_driver.get(link.replace("?source=rss", ""))
        logger.debug(f"Visiting {link}")
        time.sleep(2)
        apply_box = test_driver.find_element(
            By.XPATH,
            '//*[@id="main"]/div[2]/div[4]/div/div/div[1]/div/div[2]/aside/div[1]/div[1]/div[1]/div/span/button',
        )
        apply_box.click()
        time.sleep(5)
        try:
            annoying_box = test_driver.find_element(
                By.XPATH,
                '//*[@id="main"]/div/div[2]/div/div[3]/div[2]/div/div/div/div[1]/button',
            )
            annoying_box.click()
            time.sleep(5)
        except NoSuchElementException:
            pass

        except ElementClickInterceptedException as e:
            logger.debug(f"Radio button not clickable {link}")
            logger.debug(f"{e}")
            pass
        try:
            you_do_not_qualify_box = test_driver.find_element(
                By.CSS_SELECTOR, "div[class='up-alert-slot-container'] p:nth-child(1)"
            )
            if you_do_not_qualify_box.text == "You do not meet all the client's preferred qualifications":
                logger.debug(f"You do not qualify to this job, skipping {link}")
                self.skipped_run += 1
                skipping = not(skipping)
            time.sleep(1)
        except NoSuchElementException:
            logger.debug(f"Cant locate you_do_not_qualify_box inside of {link}")
            pass
        try:
            duration_dropdown_box = test_driver.find_element(
                By.XPATH, '//*[@id="dropdown-label-2"]'
            )
            duration_dropdown_box.click()
            time.sleep(1)
        except NoSuchElementException:
            logger.debug(f"Cant locate duration_dropdown_box inside of {link}")
            pass
        try:
            duration_dropdown_item_box = test_driver.find_element(
                By.XPATH, "(//span[@class='up-menu-item-text'])[4]"
            )
            duration_dropdown_item_box.click()
            time.sleep(1)
        except NoSuchElementException:
            logger.debug(
                f"Cant click on item inside duration_dropdown_box inside of {link}"
            )
            pass
        try:
            # github_box = test_driver.find_element(By.XPATH, "//label[contains(text(),'GitHub')]")
            cover_letter_box = test_driver.find_element(
                By.CSS_SELECTOR, '[aria-labelledby="cover_letter_label"]'
            )
            COVER_LETTER = os.getenv("COVER_LETTER")
            cover_letter_box.send_keys(COVER_LETTER)
            time.sleep(1)
            logger.debug(f"Found the cover letter box {link}")
        except NoSuchElementException:
            logger.warning(f"Cant locate cover_letter_box 3 inside of {link}")
            pass
        try:
            # q_and_a_interview_box = {"cause of this issue":"I would need to take a look at the code base"}
            questions_interview_box = test_driver.find_element(
                By.CLASS_NAME, "fe-proposal-job-questions"
            )
            labels_inside_questions_interview_box = questions_interview_box.find_elements(
                By.TAG_NAME, "label"
            )

            logger.debug(
                f"Found {len(labels_inside_questions_interview_box)} interview questions"
            )
            questions_interview_list = list(
                map(lambda number: number.text, labels_inside_questions_interview_box)
            )
            logger.debug(f"Found these interview questions: {questions_interview_list}")
            text_fields_inside_questions_interview_box = (
                questions_interview_box.find_elements(By.CLASS_NAME, "up-textarea")
            )
            zipped_lists_dictionary = {
                questions_interview_list[i]: text_fields_inside_questions_interview_box[i]
                for i in range(len(questions_interview_list))
            }

            fill_out_text_boxes(zipped_lists_dictionary, logger)

            # attrs = test_driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', questions_interview_box)
            # result = [key for (key, value) in attrs.items() if value == '']

        except NoSuchElementException as e:
            logger.error(f"Cant locate questions_interview_box inside of {link}")
            logger.error(f"{e}")
            pass
        try:
            submit_application_box = test_driver.find_element(
                By.CSS_SELECTOR,
                "button[class='up-btn up-btn-primary m-0']",
            )
            if self.dry_run is False and skipping is False:
                submit_application_box.click()
                time.sleep(5)
            logger.debug(f"Applied to job {link}")
            self.successful_run += 1
        except NoSuchElementException as e:
            logger.error(f"Cant locate submit_application_box inside of {link}")
            logger.error(f"{e}")
            self.failed_run += 1
            pass

if __name__ == "__main__":
    load_dotenv()
    UpworkBot()

# parse more urls
# put configuration in yaml
# list what i applied to into a new log file
# docker
# comment my code
# close other window
