# Project Title
Web Scraping Project

## Description
This project consists of multiple web scraping scripts designed to extract information from various websites. The scripts utilize Python and its libraries, such as `requests` and `BeautifulSoup`, to fetch and parse HTML content.

## Features
* Web scraping of job listings from [timesjobs.com](http://timesjobs.com)
* Web scraping of course information from static HTML files
* Web scraping of job postings from [TimesJobs](https://www.timesjobs.com)

## File Descriptions

### `Project(Web scrapping)\main.py`
This script scrapes job listings from [timesjobs.com](http://timesjobs.com) and saves them to text files. It continuously scrapes job listings, filtering out jobs that require a user-specified unfamiliar skill.

### `Webscrapping1\main.py`
This script performs web scraping on an HTML file to extract course information. It reads an HTML file, parses its content using BeautifulSoup, and extracts course cards.

### `Webscrapping2\main.py`
This script scrapes job postings from [TimesJobs](https://www.timesjobs.com). It fetches HTML content from a predefined URL, extracts relevant job details, and prints them to the console.


## Usage
To run the scripts, navigate to the respective directory and execute the `main.py` file.

```bash
# Run the script to scrape job listings from timesjobs.com
python Project(Web scrapping)\main.py

# Run the script to scrape course information from an HTML file
python Webscrapping1\main.py

# Run the script to scrape job postings from TimesJobs
python Webscrapping2\main.py
```

Note: Make sure to replace the placeholder URLs and file paths with actual values before running the scripts. Additionally, be respectful of website terms of service and robots.txt files when web scraping.
