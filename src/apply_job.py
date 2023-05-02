import time
import re
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
)
from selenium.webdriver.common.by import By


def apply_to_job(link, test_driver, logger, dry_run):
    # go to URL
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
        cover_letter_box.send_keys(
            """Dear Sir, Madam, 

I feel confident I can help you on this project. I've maintained custom Django/React ecommerce shops and built web apps from scratch. In my latest project I handled the telegram API and was tasked to scrape the job postings from linkedin in order to post them to a telegram group. Please find attached the link to the video showcasing the software in action: https://www.youtube.com/watch?v=TE1I8zdv124.

I have also scraped android based native/hybrid/web apps on mobile.

My github profile: https://github.com/hupratt

I'm full time at home for the time being so I am available anytime for a chat 

Best Regards"""
        )
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
        if dry_run is False:
            submit_application_box.click()
            time.sleep(5)
        logger.debug(f"Applied to job {link}")
    except NoSuchElementException as e:
        logger.error(f"Cant locate submit_application_box inside of {link}")
        logger.error(f"{e}")
        pass
    


def fill_out_text_boxes(zipped_lists_dictionary, logger):
    for question, target in zipped_lists_dictionary.items():
        if re.search("cause of this issue", question, re.IGNORECASE):
            target.send_keys(
                "I can't tell what the cause could be. If you allowed me to call you regarding this topic maybe I could better assess the issue."
            )
        elif re.search("what do you have experience with", question, re.IGNORECASE):
            target.send_keys(
                "Maintaining, building web apps, websites, fat clients, web sockets for real time chat, webRTC for easy conferencing, streaming services, scraping services and much more. Please refer to my portfolio site or my github for more information. "
            )
        elif re.search("how long", question, re.IGNORECASE):
            target.send_keys(
                "It depends on how far you are willing to sacrifice quality over speed?"
            )
        elif re.search("Describe your recent experience", question, re.IGNORECASE):
            target.send_keys(
                "I've recently built a telegram group that gets updated from linkedin and monster databases based on specific job queries and filters. Users can then apply by clicking on the telegram link"
            )
        elif re.search("certifications", question, re.IGNORECASE):
            target.send_keys(
                "I have a masters degree in engineering from the ULB in Brussels, Belgium. I have attended some coursera certifications around front end development and SAS development. I am currently working on getting my RHCSA "
            )
        elif re.search(
            "Include a link to your GitHub profile", question, re.IGNORECASE
        ):
            target.send_keys(
                "I've recently built a telegram group that gets updated from linkedin and monster databases based on specific job queries and filters. Users can then apply by clicking on the telegram link"
            )
        elif re.search(
            "Are you open to have a PAID 1-2 hours take home project to test your skills and capabilities",
            question,
            re.IGNORECASE,
        ):
            target.send_keys("sure")
        elif re.search("AWS", question, re.IGNORECASE):
            target.send_keys(
                "I've used aws extensively to manage backups, create and maintain EC2 instance, create policies, S3 storage and ECS for docker images deployment"
            )
        elif re.search("react", question, re.IGNORECASE):
            target.send_keys(
                "I have built and maintained many react applications since 2015"
            )
        else:
            logger.debug(
                f"No answers to the following question were found: {question}"
            )
