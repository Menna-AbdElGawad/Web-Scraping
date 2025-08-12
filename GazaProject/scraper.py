import requests
from bs4 import BeautifulSoup
import datetime

class GazaScraper:
    def __init__(self):
        self.url = "https://www.aljazeera.net/search/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1%20%D8%BA%D8%B2%D8%A9"

    def get_latest_news(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")

        news_div = soup.find("div", {"class": "gc_content"})
        articles_html = news_div.find_all("article")

        news_list = []  # قائمة جديدة لتخزين الأخبار

        for article in articles_html:
            title_tag = article.find("h3") or article.find("h2")  # حسب هيكلة الموقع
            title = title_tag.get_text(strip=True) if title_tag else "No title"

            link_tag = article.find("a", href=True)
            link = link_tag["href"] if link_tag else "No link"

            date_tag = article.find("time")
            date = date_tag.get_text(strip=True) if date_tag else "No date"

            news_list.append({"title": title, "link": link, "date": date})

        return news_list

    def search_key(self, keyword):
        news = self.get_latest_news()
        return [n for n in news if keyword in n["title"]]

    def filter_date(self, target_date):
        news = self.get_latest_news()
        return [n for n in news if target_date in n["date"]]
