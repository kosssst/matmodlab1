import csv

if __name__ == "__main__":
    with open("data.csv", 'r', newline='', encoding='UTF-8') as f:
        with open("normal_data.csv", 'w',newline='', encoding='UTF-8') as fw:
            reader = csv.reader(f)
            writer = csv.writer(fw)
            for row in reader:
                if((row[1] == "0.0000") or (row[2] == "0.0000") or (row[3] == "0.0000") or (row[4] == "0.0000") or (row[5] == "0.0000") or (row[6] == "0.0000") or (row[7] == "0.0000") or (row[8] == "0.0000") or (row[9] == "0.0000") or (row[10] == "0.0000") or (row[11] == "0.0000") or (row[12] == "0.0000")):
                    continue
                else:
                    writer.writerow(row)