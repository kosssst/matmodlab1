import csv

if __name__ == "__main__":
    with open("normal_data_v2.csv", 'r', encoding="UTF-8") as f:
        with open("pm25-co_ppm.csv", 'w', newline='', encoding="UTF-8") as fw:
            reader = csv.reader(f)
            writer = csv.writer(fw)
            for row in reader:
                newrow = [row[5], row[12]]
                writer.writerow(newrow)