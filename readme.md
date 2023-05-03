# Upwork Bot

Automate your job search and delegate the task to a bot that will apply for you.

## DISCLAIMER

This codebase is in beta release. You may get banned for using this so make sure to use it with a test account.

## Requirements

Docker

## Features
1. Configurable search parameters. You can include and exclude certain keywords as well as sort the results 
- Sort: "Most recent ads", "Most money spent" or "Client rating". The variable that controls for sorting is either: SORT_SEARCH_BY=client_total_charge,SORT_SEARCH_BY=client_rating, SORT_SEARCH_BY=recency or SORT_SEARCH_BY=relevance
- Include keywords: INCLUDE_KEYWORDS_IN_SEARCH=python django java C#
- Exclude keywords: EXCLUDE_KEYWORDS_IN_SEARCH=dart 3D
- Run chrome in the background with the following configuration HEADLESS=1 or run in the foreground HEADLESS=0

2. Run anywhere with docker
3. Output a .txt with a couple of statistic like: timestamps, the number of applications sent, the number of failed applications and the number of skipped applications
4. The program outputs an error log that gives insight as to why the job application failed. More often than not it's because the customer has very specific questions to which this program was not pre-configured to answer


## Run with docker-compose
`
cp .env.template .env
`
`docker-compose up`

In case you're allergic to docker here are the manual steps:

## Install manually on Linux

Install chrome or chromium as well as the chrome driver.

Run these commands: 

`
cp .env.template .env
`

`
virtualenv env -p python3.10
`

`
source env/bin/activate
`

`
pip install -r requirements.txt
`

## Run manually on Linux

python src/main.py