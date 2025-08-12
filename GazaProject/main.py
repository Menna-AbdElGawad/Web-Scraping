from scraper import GazaScraper
from datetime import datetime

def display_menu(language="en"):
    if language == "en":
        print("=== Gaza News Portal ===")
        print("1. View Latest News")
        print("2. Search News by Keyword")
        print("3. Filter News by Date")
        print("4. Switch Language (English / Arabic)")
        print("5. Exit")
    elif language == "ar":
        print("=== بوابة أخبار غزة ===")
        print("1. عرض آخر الأخبار")
        print("2. البحث عن الأخبار بالكلمة المفتاحية")
        print("3. تصفية الأخبار حسب التاريخ")
        print("4. تغيير اللغة (عربي / إنجليزي)")
        print("5. خروج")

def main():
    scraper = GazaScraper()

    print("Choose Language / اختر اللغة:")
    print("1. English")
    print("2. اللغة العربية")

    choice = input("Enter choice: ")

    if choice == "1":
        language = "en"
    elif choice == "2":
        language = "ar"
    else:
        print("Invalid choice! Defaulting to English.")
        language = "en"

    while True:
        display_menu(language)
        option = input("Enter option: ")

        if option == "1":
            news = scraper.get_latest_news()
            scraper.save_to_csv(news)
            for n in news:
                if n['date']:
                    date_str = n['date'].strftime('%d/%m/%Y')
                else:
                    date_str = 'N/A'
                print(f"{date_str} - {n['title']} ({n['link']})")

        elif option == "2":
            keyword = input("Enter keyword: ")
            news = scraper.search_key(keyword)
            for n in news:
                if n['date']:
                    date_str = n['date'].strftime('%d/%m/%Y')
                else:
                    date_str = 'N/A'
                print(f"{date_str} - {n['title']}")

        elif option == "3":
            date_str = input("Enter date (DD/MM/YYYY): ")
            try:
                target_date = datetime.strptime(date_str, "%d/%m/%Y").date()
            except:
                print("Invalid date format.")
                continue

            news = scraper.filter_date(target_date)
            for n in news:
                if n['date']:
                    date_str = n['date'].strftime('%d/%m/%Y')
                else:
                    date_str = 'N/A'
                print(f"{date_str} - {n['title']}")

        elif option == "4":
            if language == "en":
                language = "ar"
                print("تم تغيير اللغة.")
            else:
                language = "en"
                print("Language switched.")

        elif option == "5":
            if language == "en":
                print("Good Bye!")
            else:
                print("إلى اللقاء!")
            break

        else:
            if language == "en":
                print("Invalid choice, please try again.")
            else:
                print("اختيار غير صالح، حاول مرة أخرى.")

if __name__ == "__main__":
    main()