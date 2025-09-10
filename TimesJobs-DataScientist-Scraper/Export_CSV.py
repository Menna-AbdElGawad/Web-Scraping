import csv

class Export_csv:
    def __init__(self):
        self.filename = "Jobs.csv"
        self.columns = [
            'Company Name', 'Job Title', 'Location', 'Published Date', 'More Info'
        ]

    def save_csv(self, data):
        with open(self.filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.columns)
            writer.writeheader()
            writer.writerows(data)
        print(f"✅ Saved {len(data)} jobs into: {self.filename}")
        print("Good Bye:)")