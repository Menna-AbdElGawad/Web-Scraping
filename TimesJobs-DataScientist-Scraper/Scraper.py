import requests
from Parser import Parsing
from Export_CSV import Export_csv
import os

class Scraping:
    def __init__(self, keyword, max_pages=10):
        self.keyword = keyword.replace(' ', '%20')
        self.max_pages = max_pages  

    def run(self):
        if os.path.exists("Jobs.csv"):
            os.remove("Jobs.csv")
            print("Old Jobs.csv removed. Starting fresh...")

        all_jobs = []
        page = 1

        while page <= self.max_pages:
            url = (
                f"https://www.timesjobs.com/candidate/job-search.html?"
                f"from=submit&luceneResultSize=25&txtKeywords={self.keyword}"
                f"&postWeek=60&searchType=personalizedSearch"
                f"&actualTxtKeywords={self.keyword}"
                f"&searchBy=0&rdoOperator=OR&pDate=I&sequence=6&startPage={page}"
            )

            print(f"Fetching the page {page}...")
            response = requests.get(url)

            if response.status_code != 200:
                print(f"Error fetching page {page}: {response.status_code}")
                break

            html_content = response.text
            parse = Parsing(html_content)
            page_jobs = parse.get_data()

            if not page_jobs:
                print("No more jobs found. Scraping finished.")
                break

            all_jobs.extend(page_jobs)
            page += 1

        if all_jobs:
            export = Export_csv()
            export.save_csv(all_jobs)
        else:
            print("No jobs found.")
