import csv

if __name__ == "__main__":
    with open("normal_data_v2.csv", 'r', encoding="UTF-8") as f:
        with open("time-temperature.csv", 'w', newline='', encoding="UTF-8") as fw:
            reader = csv.reader(f)
            writer = csv.writer(fw)
            i = 1
            for row in reader:
                newrow= []
                if "00:00:00" in row[0]:
                    newrow.append("0")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "01:00:00" in row[0]:
                    newrow.append("1")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "02:00:00" in row[0]:
                    newrow.append("2")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "03:00:00" in row[0]:
                    newrow.append("3")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "04:00:00" in row[0]:
                    newrow.append("4")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "05:00:00" in row[0]:
                    newrow.append("5")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "06:00:00" in row[0]:
                    newrow.append("6")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "07:00:00" in row[0]:
                    newrow.append("7")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "08:00:00" in row[0]:
                    newrow.append("8")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "09:00:00" in row[0]:
                    newrow.append("9")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "10:00:00" in row[0]:
                    newrow.append("10")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "11:00:00" in row[0]:
                    newrow.append("11")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "12:00:00" in row[0]:
                    newrow.append("12")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "13:00:00" in row[0]:
                    newrow.append("13")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "14:00:00" in row[0]:
                    newrow.append("14")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "15:00:00" in row[0]:
                    newrow.append("15")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "16:00:00" in row[0]:
                    newrow.append("16")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "17:00:00" in row[0]:
                    newrow.append("17")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "18:00:00" in row[0]:
                    newrow.append("18")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "19:00:00" in row[0]:
                    newrow.append("19")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "20:00:00" in row[0]:
                    newrow.append("20")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "21:00:00" in row[0]:
                    newrow.append("21")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "22:00:00" in row[0]:
                    newrow.append("22")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue
                if "23:00:00" in row[0]:
                    newrow.append("23")
                    newrow.append(row[i])
                    writer.writerow(newrow)
                    continue