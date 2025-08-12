import csv

def save_csv(data, filename) :
    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f :
        writer = csv.DictWriter(f, fieldnames=keys[data])
        writer.writeheader()
        writer.writerows(data)