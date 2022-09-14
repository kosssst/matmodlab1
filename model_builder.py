import matplotlib.pyplot as plt
import csv
import math
import sys

def det2(arr):
    return ((arr[0][0]*arr[1][1])-(arr[1][0]*arr[0][1]))

def det(arr, n):
    result = 0.0
    if(n > 2):
        for i in range(n):
            new_matrix = []
            for j in range(1,n):
                row = []
                for k in range(n):
                    if(k == i):
                        continue
                    else:
                        row.append(arr[j][k])
                new_matrix.append(row)
            result = result + (math.pow(-1, i) * arr[0][i] * det(new_matrix, n-1))
    else:
        result = det2(arr)
    return result

def kramer(arr, n):
    matrixs = []
    dets = []
    koefs = []
    for i in range(n+1):
        m = []
        if(i == n):
            for j in range(n):
                row = []
                for k in range(n):
                    row.append(arr[j][k])
                m.append(row)
        else:
            for j in range(n):
                row = []
                for k in range(n):
                    if(k == i):
                        row.append(arr[j][n])
                    else:
                        row.append(arr[j][k])
                m.append(row)
        matrixs.append(m)
    for i in range(n+1):
        dets.append(det(matrixs[i], n))
    for i in range(n):
        koefs.append((dets[i]/dets[n]))
    return koefs

def linear_model(x_arr, y_arr, n, plot):
    yt = []
    sum_x = 0.0
    sum_y = 0.0
    sum_x2 = 0.0
    sum_xy = 0.0
    for i in range(n):
        sum_x = sum_x + x_arr[i]
        sum_y = sum_y + y_arr[i]
        sum_x2 = sum_x2 + (x_arr[i]*x_arr[i])
        sum_xy = sum_xy + (x_arr[i]*y_arr[i])
    x_ser = sum_x/n
    y_ser = sum_y/n
    p_xy_sum = 0.0
    p_x_sum = 0.0
    p_y_sum = 0.0
    for i in range(n):
        p_xy_sum = p_xy_sum + ((x_arr[i] - x_ser)*(y_arr[i] - y_ser))
        p_x_sum = p_x_sum + ((x_arr[i] - x_ser)*(x_arr[i] - x_ser))
        p_y_sum = p_y_sum + ((y_arr[i] - y_ser)*(y_arr[i] - y_ser))
    arr = [[n, sum_x, sum_y], [sum_x, sum_x2, sum_xy]]
    koefs = kramer(arr, 2)
    print("linear:")
    print("a1 = " + str(koefs[0]))
    print("a2 = " + str(koefs[1]))
    koef_kor = p_xy_sum/((math.sqrt(p_x_sum))*(math.sqrt(p_y_sum)))
    print("koef kor = " + str(koef_kor))
    r2_yt = 0
    r2_y = 0
    for i in range(n):
        yti = koefs[0] + x[i]*koefs[1]
        r2_yt = r2_yt + ((y[i]-yti)*(y[i]-yti))
        r2_y = r2_y + ((y[i]-y_ser)*(y[i]-y_ser))
        yt.append(yti)
    r2 = 1 - (r2_yt/r2_y)
    print("r^2 = " + str(r2))
    plot.plot(x_arr, yt, label = "linear", color="red")

    



def polinomial_model_2(x_arr, y_arr, n, plot):
    yt = []
    sum_x = 0.0
    sum_y = 0.0
    sum_x2 = 0.0
    sum_xy = 0.0
    sum_x3 = 0.0
    sum_x2y = 0.0
    sum_x4 = 0.0
    for i in range(n):
        sum_x = sum_x + x_arr[i]
        sum_y = sum_y + y_arr[i]
        sum_x2 = sum_x2 + (x_arr[i]*x_arr[i])
        sum_xy = sum_xy + (x_arr[i]*y_arr[i])
        sum_x3 = sum_x3 + (x_arr[i]*x_arr[i]*x_arr[i])
        sum_x2y = sum_x2y + (x_arr[i]*x_arr[i]*y_arr[i])
        sum_x4 = sum_x4 + (math.pow(x_arr[i], 4))
    x_ser = sum_x/n
    y_ser = sum_y/n
    p_xy_sum = 0.0
    p_x_sum = 0.0
    p_y_sum = 0.0
    for i in range(n):
        p_xy_sum = p_xy_sum + ((x_arr[i] - x_ser)*(y_arr[i] - y_ser))
        p_x_sum = p_x_sum + ((x_arr[i] - x_ser)*(x_arr[i] - x_ser))
        p_y_sum = p_y_sum + ((y_arr[i] - y_ser)*(y_arr[i] - y_ser))
    arr = [[n, sum_x, sum_x2, sum_y], [sum_x, sum_x2, sum_x3, sum_xy], [sum_x2, sum_x3, sum_x4, sum_x2y]]
    koefs = kramer(arr, 3)
    print("polinomial (2):")
    print("a1 = " + str(koefs[0]))
    print("a2 = " + str(koefs[1]))
    print("a3 = " + str(koefs[2]))
    koef_kor = p_xy_sum/((math.sqrt(p_x_sum))*(math.sqrt(p_y_sum)))
    print("koef kor = " + str(koef_kor))
    r2_yt = 0
    r2_y = 0
    for i in range(n):
        yti = koefs[0] + x_arr[i]*koefs[1] + koefs[2]*x_arr[i]*x_arr[i]
        r2_yt = r2_yt + ((y[i]-yti)*(y[i]-yti))
        r2_y = r2_y + ((y[i]-y_ser)*(y[i]-y_ser))
        yt.append(yti)
    r2 = 1 - (r2_yt/r2_y)
    print("r^2 = " + str(r2))
    plot.plot(x_arr, yt, label = "polinomial (2)", color="blue")


if __name__ == "__main__":
    x = []
    y = []
    num_rows = 0
    name = sys.argv[1]
    data = sys.argv[2]
    xl = sys.argv[3]
    yl = sys.argv[4]
    with open(data,'r',encoding="UTF-8") as f:
        reader = csv.reader(f)
        for row in reader:
            xi = float(row[0])
            yi = float(row[1])
            x.append(xi)
            y.append(yi)
            num_rows = num_rows + 1
        plt.scatter(x, y, color= "green", marker= ".", s=1)
        print(name)
        linear_model(x, y, num_rows, plt)
        polinomial_model_2(x,y,num_rows,plt)
        plt.xlabel(xl)
        plt.ylabel(yl)
        plt.title(name)
        plt.legend()
        plt.show()
    