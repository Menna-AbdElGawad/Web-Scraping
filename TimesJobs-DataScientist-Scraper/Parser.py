from bs4 import BeautifulSoup

class Parsing:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'lxml')
        self.jobs = self.soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    def get_data(self):
        extracted_jobs = []

        for job in self.jobs:
            published_date = job.find('span', class_='sim-posted').span.text.strip()

            if 'few' in published_date:
                company_name = job.find('h3', class_='joblist-comp-name').text.strip()
                job_title = job.find('h2').text.strip()
                more_info = job.header.h2.a['href']

                experience_tag = job.find('ul', class_='top-jd-dtl mt-16 clearfix').li
                location_tags = experience_tag.find_all("li") if experience_tag else []
                location = location_tags[1].text.strip() if len(location_tags) > 1 else "Not Mentioned"

                extracted_jobs.append({
                    "Company Name": company_name,
                    "Job Title": job_title,
                    "Location": location,
                    "Published Date": published_date,
                    "More Info": more_info
                })

        return extracted_jobs
