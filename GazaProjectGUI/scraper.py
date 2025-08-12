from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from datetime import datetime
import time
import csv

class GazaScraper:
    def __init__(self):
        self.url = "https://www.aljazeera.net/search/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1%20%D8%BA%D8%B2%D8%A9"

    def get_latest_news(self):
        options = Options()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

        driver.get(self.url)
        time.sleep(3)

        while True:
            try:
                load_more_button = driver.find_element(By.CLASS_NAME, "show-more-button")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", load_more_button)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", load_more_button)
                time.sleep(3)  
            except NoSuchElementException:
                break

        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        news_list_div = soup.select_one("div.search-result__list")
        if not news_list_div:
            print("لم يتم العثور على قسم الأخبار")
            return []

        articles = news_list_div.find_all("article")
        news_data = []
        for article in articles:
            title_tag = article.find("h3")
            link_tag = article.find("a")
            date_tag = article.find(string=lambda text: "تحديث" in text)

            title = title_tag.get_text(strip=True) if title_tag else "No title"
            link = link_tag["href"] if link_tag else None
            date_str = date_tag.replace("آخر تحديث", "").strip() if date_tag else None

            try:
                date_obj = datetime.strptime(date_str, "%d/%m/%Y")
            except:
                date_obj = None

            news_data.append({
                "title": title,
                "link": link,
                "date": date_obj
            })

        news_data.sort(key=lambda x: x["date"] or datetime.min, reverse=True)
        return news_data


    def save_to_csv(self, news_data):
        if not news_data:
            print("There is no data to save.")
            return

        with open("GazaNews.csv", mode="w", newline="", encoding="utf-8-sig") as file:
            writer = csv.DictWriter(file, fieldnames=news_data[0].keys())
            writer.writeheader()
            writer.writerows(news_data)

            print("\n \n")
            print("You will find file in your directory named 'GazaNews.csv'")
            print("\n\n")

    def search_key(self, keyword):
        news = self.get_latest_news()
        return [n for n in news if keyword in n["title"]]

    def filter_date(self, target_date):
        news = self.get_latest_news()
        return [n for n in news if n["date"] and n["date"].date() == target_date]