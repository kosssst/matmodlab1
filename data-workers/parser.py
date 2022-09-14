import csv



if __name__ == "__main__":
    with open("saveecobot_19719.csv", newline='', encoding='utf-8') as f:
        with open("data.csv", 'w',newline='', encoding='UTF-8') as fw:
            reader = csv.reader(f)
            writer = csv.writer(fw)
            last_date = 'logged_at'
            newrow = ["0","0","0","0","0","0","0","0","0","0","0","0","0"]
            for row in reader:
                date = row[3]
                if(date == last_date):
                    if(row[1] == "humidity"):
                        newrow[2] = row[2]
                    if(row[1] == "pressure_pa"):
                        newrow[3] = row[2]
                    if(row[1] == "pm1"):
                        newrow[4] = row[2]
                    if(row[1] == "pm25"):
                        newrow[5] = row[2]
                    if(row[1] == "pm10"):
                        newrow[6] = row[2]
                    if(row[1] == "no2_ug"):
                        newrow[7] = row[2]
                    if(row[1] == "so2_ug"):
                        newrow[8] = row[2]
                    if(row[1] == "co_mg"):
                        newrow[9] = row[2]
                    if(row[1] == "no2_ppb"):
                        newrow[10] = row[2]
                    if(row[1] == "so2_ppb"):
                        newrow[11] = row[2]
                    if(row[1] == "co_ppm"):
                        newrow[12] = row[2]
                else:
                    newrow[0] = last_date
                    last_date = date
                    writer.writerow(newrow)
                    newrow = ["0","0","0","0","0","0","0","0","0","0","0","0","0"]
                    if(row[1] == "temperature"):
                        newrow[1] = row[2]

