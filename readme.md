# Upwork Bot

Automate your job search and delegate the task to a bot that will apply for you.

## Features
- Configurable search parameters. You can include and exclude certain keywords as well as sort the results by either: "Most recent ads", "Most money spent" or "Client rating"
- Run anywhere


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