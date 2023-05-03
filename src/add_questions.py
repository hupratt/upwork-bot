import re



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
        elif re.search("How many hours", question, re.IGNORECASE):
            target.send_keys(
                "It depends on how far you are willing to sacrifice quality over speed?"
            )
        elif re.search("What software and applications do you use to scrape data", question, re.IGNORECASE):
            target.send_keys(
                "Only open source tools"
            )
        elif re.search("What software do you use to scrape data", question, re.IGNORECASE):
            target.send_keys(
                "Only open source tools"
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
        elif re.search("What information do you need from me to complete the job", question, re.IGNORECASE):
            target.send_keys(
                "A quick call with your team would help a lot"
            )
        elif re.search("Do you have examples of scraping sites", question, re.IGNORECASE):
            target.send_keys(
                "Please find my youtube channel here: https://www.youtube.com/channel/UC1bbDpT18-hqtiOJ-BKLuYQ"
            )
        elif re.search("examples of scraping sites", question, re.IGNORECASE):
            target.send_keys(
                "Please find my youtube channel here: https://www.youtube.com/channel/UC1bbDpT18-hqtiOJ-BKLuYQ"
            )
        elif re.search("What office applications", question, re.IGNORECASE):
            target.send_keys(
                "Excel and word exclusively. I am not proficient with VBA but I can do lookups, index/matches and much more"
            )
        else:
            logger.error(
                f"No answers to the following question were found: {question}"
            )
