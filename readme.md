# Upwork Bot

Automate your job search and delegate the task to a bot that will apply for you.

## DISCLAIMER

This codebase is in beta release. You may get banned for using this. If you want to help out do not use this on your main account

## Requirements

Docker

## Features
1. Configurable search parameters. You can include and exclude certain keywords as well as sort the results 
- Sort: "Most recent ads", "Most money spent" or "Client rating". The variable that controls for sorting is either: SORT_SEARCH_BY=client_total_charge,SORT_SEARCH_BY=client_rating, SORT_SEARCH_BY=recency or SORT_SEARCH_BY=relevance
- Include keywords: INCLUDE_KEYWORDS_IN_SEARCH=python django java C#
- Exclude keywords: EXCLUDE_KEYWORDS_IN_SEARCH=dart 3D

2. Run anywhere with docker
3. Output a .txt with a couple of statistic like: timestamps, the number of applications sent, the number of failed applications and the number of skipped applications

## Run with docker-compose
`
cp .env.template .env
`
`docker-compose up`

In case you're allergic to docker here are the manual steps:

## Install manually on Linux
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