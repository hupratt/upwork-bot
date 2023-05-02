import pickle
from journal import logger
from chromewebdriver import test_driver
from signin import login
from search import go_to_search
from apply_job import apply_to_job
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import urllib.request

class UpworkBot:
    def __init__(self, dry_run=True):
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
# close other window
