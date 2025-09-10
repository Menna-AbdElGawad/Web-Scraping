from Scraper import Scraping

def main():
    print("\n===== Welcome to Job Scraping =====")
    print("===================================")

    keyword = input("\nPlease Enter the job title you want to search for: ")

    scrape = Scraping(keyword=keyword, max_pages=10)  
    scrape.run()

if __name__ == '__main__':
    main()
