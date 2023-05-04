import pytest
import sys
from time import sleep
from selenium.webdriver.common.by import By
from main import UpworkBot


# @pytest.fixture
# def chrome_options(chrome_options):
#     chrome_options.driver = '/usr/lib/chromium-browser/chromedriver'
#     chrome_options.add_argument('--kiosk')
#     chrome_options.add_argument('--headless')
#     test_ua = "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"
#     chrome_options.add_argument("--window-size=1920,1080")

#     chrome_options.add_argument(f"--user-agent={test_ua}")
#     chrome_options.add_argument("--incognito")

#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-extensions")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     return chrome_options

@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium


# def test_nondestructive(selenium):
#     selenium.get("http://www.example.com")


# To avoid accidental changes being made to sensitive
# environments such as your production instances, all 
# tests are assumed to be destructive. Any destructive
# tests attempted to run against a sensitive 
# environment will be skipped.
@pytest.mark.nondestructive
def visit_pickled_links(selenium):
    bot = UpworkBot()
    for link in UpworkBot.parse_soup():
        bot.apply_to_job(link)
    selenium.get("html_page.html")

    # selenium.find_element(By.NAME, "li1").click()
    # selenium.find_element(By.NAME, "li2").click()

    # title = "Sample page - lambdatest.com"
    # assert title == selenium.title

    # sample_text = "Happy Testing at LambdaTest"
    # email_text_field = selenium.find_element(By.ID, "sampletodotext")
    # email_text_field.send_keys(sample_text)
    # sleep(5)

    # selenium.find_element(By.ID, "addbutton").click()
    # sleep(5)

    # output_str = selenium.find_element(By.NAME, "li6").text
    # sys.stderr.write(output_str)

    # sleep(2)
    selenium.close()
