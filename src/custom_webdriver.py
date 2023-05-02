
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()

test_ua = "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"

options = webdriver.ChromeOptions()

options.add_argument("--window-size=1920,1080")

options.add_argument(f"--user-agent={test_ua}")
options.add_argument("--incognito")

options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
HEADLESS = os.getenv("HEADLESS")
if HEADLESS is True:
    options.add_argument('--headless')

CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")
test_driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)

