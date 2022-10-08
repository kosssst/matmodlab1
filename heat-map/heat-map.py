import seaborn as sns
import pandas as pd
import csv
import matplotlib.pyplot as plt
import math

def get_koef_kor(file_name):
    x = []
    y = []
    sum_x = 0.0
    sum_y = 0.0
    num_rows = 0
    file = "../data/" + str(file_name)
    with open(file,'r',encoding="UTF-8") as f:
        reader = csv.reader(f)
        for row in reader:
            xi = float(row[0])
            yi = float(row[1])
            sum_x = sum_x + xi
            sum_y = sum_y + yi
            x.append(xi)
            y.append(yi)
            num_rows = num_rows + 1
    x_ser = sum_x/num_rows
    y_ser = sum_y/num_rows
    p_xy_sum = 0.0
    p_x_sum = 0.0
    p_y_sum = 0.0
    for i in range(num_rows):
        p_xy_sum = p_xy_sum + ((x[i] - x_ser)*(y[i] - y_ser))
        p_x_sum = p_x_sum + ((x[i] - x_ser)*(x[i] - x_ser))
        p_y_sum = p_y_sum + ((y[i] - y_ser)*(y[i] - y_ser))
    
    return p_xy_sum/((math.sqrt(p_x_sum))*(math.sqrt(p_y_sum)))

if __name__ == "__main__":
    files = [["1", "temperature-humidity.csv", "temperature-pressure_pa.csv", "temperature-pm1.csv", "temperature-pm25.csv", "temperature-pm10.csv", "temperature-no2_ug.csv", "temperature-so2_ug.csv", "temperature-co_mg.csv", "temperature-no2_ppb.csv", "temperature-so2_ppb.csv", "temperature-co_ppm.csv"],
             ["temperature-humidity.csv", "1", "humidity-pressure_pa.csv", "humidity-pm1.csv", "humidity-pm25.csv", "humidity-pm10.csv", "humidity-no2_ug.csv", "humidity-so2_ug.csv", "humidity-co_mg.csv", "humidity-no2_ppb.csv", "humidity-so2_ppb.csv", "humidity-co_ppm.csv"],
             ["temperature-pressure_pa.csv", "humidity-pressure_pa.csv", "1", "pressure_pa-pm1.csv", "pressure_pa-pm25.csv", "pressure_pa-pm10.csv", "pressure_pa-no2_ug.csv", "pressure_pa-so2_ug.csv", "pressure_pa-co_mg.csv", "pressure_pa-no2_ppb.csv", "pressure_pa-so2_ppb.csv", "pressure_pa-co_ppm.csv"],
             ["temperature-pm1.csv", "humidity-pm1.csv", "pressure_pa-pm1.csv", "1", "pm1-pm25.csv", "pm1-pm10.csv", "pm1-no2_ug.csv", "pm1-so2_ug.csv", "pm1-co_mg.csv", "pm1-no2_ppb.csv", "pm1-so2_ppb.csv", "pm1-co_ppm.csv"],
             ["temperature-pm25.csv", "humidity-pm25.csv", "pressure_pa-pm25.csv", "pm1-pm25.csv", "1", "pm25-pm10.csv", "pm25-no2_ug.csv", "pm25-so2_ug.csv", "pm25-co_mg.csv", "pm25-no2_ppb.csv", "pm25-so2_ppb.csv", "pm25-co_ppm.csv"],
             ["temperature-pm10.csv", "humidity-pm10.csv", "pressure_pa-pm10.csv", "pm1-pm10.csv", "pm25-pm10.csv", "1", "pm10-no2_ug.csv", "pm10-so2_ug.csv", "pm10-co_mg.csv", "pm10-no2_ppb.csv", "pm10-so2_ppb.csv", "pm10-co_ppm.csv"],
             ["temperature-no2_ug.csv", "humidity-no2_ug.csv", "pressure_pa-no2_ug.csv", "pm1-no2_ug.csv", "pm25-no2_ug.csv", "pm10-no2_ug.csv", "1", "no2_ug-so2_ug.csv", "no2_ug-co_mg.csv", "no2_ug-no2_ppb.csv", "no2_ug-so2_ppb.csv", "no2_ug-co_ppm.csv"],
             ["temperature-so2_ug.csv", "humidity-so2_ug.csv", "pressure_pa-so2_ug.csv", "pm1-so2_ug.csv", "pm25-so2_ug.csv", "pm10-so2_ug.csv", "no2_ug-so2_ug.csv", "1", "so2_ug-co_mg.csv", "so2_ug-no2_ppb.csv", "so2_ug-so2_ppb.csv", "so2_ug-co_ppm.csv"],
             ["temperature-co_mg.csv", "humidity-co_mg.csv", "pressure_pa-co_mg.csv", "pm1-co_mg.csv", "pm25-co_mg.csv", "pm10-co_mg.csv", "no2_ug-co_mg.csv", "so2_ug-co_mg.csv", "1", "co_mg-no2_ppb.csv", "co_mg-so2_ppb.csv", "co_mg-co_ppm.csv"],
             ["temperature-no2_ppb.csv", "humidity-no2_ppb.csv", "pressure_pa-no2_ppb.csv", "pm1-no2_ppb.csv", "pm25-no2_ppb.csv", "pm10-no2_ppb.csv", "no2_ug-no2_ppb.csv", "so2_ug-no2_ppb.csv", "co_mg-no2_ppb.csv", "1", "no2_ppb-so2_ppb.csv", "no2_ppb-co_ppm.csv"],
             ["temperature-so2_ppb.csv", "humidity-so2_ppb.csv", "pressure_pa-so2_ppb.csv", "pm1-so2_ppb.csv", "pm25-so2_ppb.csv", "pm10-so2_ppb.csv", "no2_ug-so2_ppb.csv", "so2_ug-so2_ppb.csv", "co_mg-so2_ppb.csv", "no2_ppb-so2_ppb.csv", "1", "so2_ppb-co_ppm.csv"],
             ["temperature-co_ppm.csv", "humidity-co_ppm.csv", "pressure_pa-co_ppm.csv", "pm1-co_ppm.csv", "pm25-co_ppm.csv", "pm10-co_ppm.csv", "no2_ug-co_ppm.csv", "so2_ug-co_ppm.csv", "co_mg-co_ppm.csv", "no2_ppb-co_ppm.csv", "so2_ppb-co_ppm.csv", "1"]]
    koefs = []
    for row in files:
        newrow = []
        for cell in row:
            if(cell == "1"):
                newrow.append(1)
                continue
            else:
                newrow.append(get_koef_kor(cell))
        koefs.append(newrow)

    df = pd.DataFrame(koefs, columns=["temperature","humidity","pressure_pa","pm1","pm25","pm10","no2_ug","so2_ug","co_mg","no2_ppb","so2_ppb","co_ppm"])
    p1 = sns.heatmap(df, annot=True, annot_kws={"size": 7})
    plt.show()