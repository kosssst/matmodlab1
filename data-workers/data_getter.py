import csv

if __name__ == "__main__":
    with open("normal_data_v2.csv", 'r', encoding="UTF-8") as f:
        with open("pm1-temperature.csv", 'w', newline='', encoding="UTF-8") as fw:
            reader = csv.reader(f)
            writer = csv.writer(fw)
            for row in reader:
                newrow = [row[4], row[1]]
                writer.writerow(newrow)