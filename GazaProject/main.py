from scraper import GazaScraper
from save_data import save_csv

print("Welcome to Gaza News!")
print("---------------------")

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
    print("Choose Language / اختر اللغة:")
    print("1. English")
    print("2. اللغة العربية")

    choice = input("Enter choice: ")

    if choice == "1":
        language = "en"
    elif choice == "2":
        language = "ar"
    else:
        print("Invalid Choice! Defaulting to English.")
        language = "en"

    while True:
        display_menu(language)
        option = input("Enter option: ")

        if option == "1":
            if language == "en":
                print("Showing latest news...")
            else:
                print("عرض آخر الأخبار...")
        elif option == "2":
            if language == "en":
                print("Searching News by Keyword...")
            else:
                print("جاري البحث عن الأخبار بالكلمة المفتاحية...")
        elif option == "3":
            if language == "en":
                print("Filtering News by Date...")
            else:
                print("تصفية الأخبار حسب التاريخ...")
        elif option == "4":
            if language == "en":
                language = "ar"
                print("Language switched to Arabic.")
            else:
                language = "en"
                print("تم تغيير اللغة إلى الإنجليزية.")
        elif option == "5":
            if language == "en":
                print("Good Bye!")
            else:
                print("إلى اللقاء!")
            break
        else:
            if language == "en":
                print("Invalid Choice, please try again.")
            else:
                print("اختيار غير صالح، حاول مرة أخرى.")

if __name__ == "__main__":
    main()
    scraper = GazaScraper()
