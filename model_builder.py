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
    x_build = []
    y_build = []
    x_test = []
    y_test = []
    n_build = 0
    n_test = 0
    for i in range(n):
        if i % 5 == 0:
            x_test.append(x_arr[i])
            y_test.append(y_arr[i])
            n_test = n_test + 1
        else:
            x_build.append(x_arr[i])
            y_build.append(y_arr[i])
            n_build = n_build + 1
    yt = []
    yt1 = []
    sum_x_build = 0.0
    sum_y_build = 0.0
    sum_x2_build = 0.0
    sum_xy_build = 0.0
    for i in range(n_build):
        sum_x_build = sum_x_build + x_build[i]
        sum_y_build = sum_y_build + y_build[i]
        sum_x2_build = sum_x2_build + math.pow(x_build[i], 2)
        sum_xy_build = sum_xy_build + (x_build[i]*y_build[i])
    x_ser_build = sum_x_build/n_build
    y_ser_build = sum_y_build/n_build
    p_xy_sum = 0.0
    p_x_sum = 0.0
    p_y_sum = 0.0
    for i in range(n_build):
        p_xy_sum = p_xy_sum + ((x_build[i] - x_ser_build)*(y_build[i] - y_ser_build))
        p_x_sum = p_x_sum + ((x_build[i] - x_ser_build)*(x_build[i] - x_ser_build))
        p_y_sum = p_y_sum + ((y_build[i] - y_ser_build)*(y_build[i] - y_ser_build))
    arr = [[n_build, sum_x_build, sum_y_build], [sum_x_build, sum_x2_build, sum_xy_build]]
    koefs = kramer(arr, 2)
    print(" => linear:")
    print("  a1 = " + str(koefs[0]))
    print("  a2 = " + str(koefs[1]))
    koef_kor = p_xy_sum/((math.sqrt(p_x_sum))*(math.sqrt(p_y_sum)))
    print("  koef kor = " + str(koef_kor))
    r2_yt_build = 0
    r2_y_build = 0
    
    for i in range(n_build):
        yti = koefs[0] + x_build[i] * koefs[1]
        r2_yt_build = r2_yt_build + math.pow(y_build[i] - yti, 2)
        r2_y_build = r2_y_build + math.pow(y_build[i] - y_ser_build, 2)
        yt.append(yti)
    r2 = 1 - (r2_yt_build/r2_y_build)
    print("  r^2 = " + str(r2))
    r2_yt_test = 0
    r2_y_test = 0
    sum_y_test = 0
    for i in range(n_test):
        sum_y_test = sum_y_test + y_test[i]
    y_ser_test = sum_y_test / n_test
    for i in range(n_test):
        yti = koefs[0] + x_test[i] * koefs[1]
        r2_yt_test = r2_yt_test + math.pow(y_test[i] - yti, 2)
        r2_y_test = r2_y_test + math.pow(y_test[i] - y_ser_test, 2)
    r2_test = 1 - (r2_yt_test/r2_y_test)
    print("  r^2 (test) = " + str(r2_test) + "\n")
    x_build = sorted(x_build)
    for i in range(n_build):
        yt1.append(koefs[0] + x_build[i] * koefs[1])
    plot.plot(x_build, yt1, label = "linear", color="red")

def polinomial_model_2(x_arr, y_arr, n, plot):
    x_build = []
    y_build = []
    x_test = []
    y_test = []
    n_build = 0
    n_test = 0
    for i in range(n):
        if i % 5 == 0:
            x_test.append(x_arr[i])
            y_test.append(y_arr[i])
            n_test = n_test + 1
        else:
            x_build.append(x_arr[i])
            y_build.append(y_arr[i])
            n_build = n_build + 1
    yt = []
    yt2 = []
    sum_x_build = 0.0
    sum_y_build = 0.0
    sum_x2_build = 0.0
    sum_xy_build = 0.0
    sum_x3_build = 0.0
    sum_x2y_build = 0.0
    sum_x4_build = 0.0
    for i in range(n_build):
        sum_x_build = sum_x_build + x_build[i]
        sum_y_build = sum_y_build + y_build[i]
        sum_x2_build = sum_x2_build + math.pow(x_build[i], 2)
        sum_xy_build = sum_xy_build + (x_build[i] * y_build[i])
        sum_x3_build = sum_x3_build + math.pow(x_build[i], 3)
        sum_x2y_build = sum_x2y_build + (math.pow(x_build[i], 2) * y_build[i])
        sum_x4_build = sum_x4_build + math.pow(x_build[i], 4)
    x_ser_build = sum_x_build/n_build
    y_ser_build = sum_y_build/n_build
    p_xy_sum = 0.0
    p_x_sum = 0.0
    p_y_sum = 0.0
    for i in range(n_build):
        p_xy_sum = p_xy_sum + ((x_build[i] - x_ser_build)*(y_build[i] - y_ser_build))
        p_x_sum = p_x_sum + ((x_build[i] - x_ser_build)*(x_build[i] - x_ser_build))
        p_y_sum = p_y_sum + ((y_build[i] - y_ser_build)*(y_build[i] - y_ser_build))
    arr = [[n_build, sum_x_build, sum_x2_build, sum_y_build], [sum_x_build, sum_x2_build, sum_x3_build, sum_xy_build], [sum_x2_build, sum_x3_build, sum_x4_build, sum_x2y_build]]
    koefs = kramer(arr, 3)
    print(" => polinomial (n=2):")
    print("  a1 = " + str(koefs[0]))
    print("  a2 = " + str(koefs[1]))
    print("  a3 = " + str(koefs[2]))
    koef_kor = p_xy_sum/((math.sqrt(p_x_sum))*(math.sqrt(p_y_sum)))
    print("  koef kor = " + str(koef_kor))
    r2_yt = 0
    r2_y = 0
    for i in range(n_build):
        yti = koefs[0] + x_build[i] * koefs[1] + koefs[2] * math.pow(x_build[i], 2)
        r2_yt = r2_yt + math.pow(y_build[i] - yti, 2)
        r2_y = r2_y + math.pow(y_build[i] - y_ser_build, 2)
        yt.append(yti)
    r2 = 1 - (r2_yt/r2_y)
    print("  r^2 = " + str(r2))
    r2_yt_test = 0
    r2_y_test = 0
    sum_y_test = 0
    for i in range(n_test):
        sum_y_test = sum_y_test + y_test[i]
    y_ser_test = sum_y_test / n_test
    for i in range(n_test):
        yti = koefs[0] + x_test[i] * koefs[1] + koefs[2] * math.pow(x_test[i], 2)
        r2_yt_test = r2_yt_test + math.pow(y_test[i] - yti, 2)
        r2_y_test = r2_y_test + math.pow(y_test[i] - y_ser_test, 2)
    r2_test = 1 - (r2_yt_test/r2_y_test)
    print("  r^2 (test) = " + str(r2_test) + "\n")
    x_build = sorted(x_build)
    for i in range(n_build):
        yt2.append(koefs[0] + x_build[i] * koefs[1] + koefs[2] * math.pow(x_build[i], 2))
    plot.plot(x_build, yt2, label = "polinomial (n=2)", color="blue")

def polinomial_model_3(x_arr, y_arr, n, plot):
    x_build = []
    y_build = []
    x_test = []
    y_test = []
    n_build = 0
    n_test = 0
    for i in range(n):
        if i % 5 == 0:
            x_test.append(x_arr[i])
            y_test.append(y_arr[i])
            n_test = n_test + 1
        else:
            x_build.append(x_arr[i])
            y_build.append(y_arr[i])
            n_build = n_build + 1
    yt3 = []
    yt = []
    sum_x_build = 0.0
    sum_y_build = 0.0
    sum_x2_build = 0.0
    sum_xy_build = 0.0
    sum_x3_build = 0.0
    sum_x2y_build = 0.0
    sum_x4_build = 0.0
    sum_x5_build = 0.0
    sum_x3y_build = 0.0
    sum_x6_build = 0.0
    for i in range(n_build):
        sum_x_build = sum_x_build + x_build[i]
        sum_y_build = sum_y_build + y_build[i]
        sum_x2_build = sum_x2_build + math.pow(x_build[i], 2)
        sum_xy_build = sum_xy_build + (x_build[i] * y_build[i])
        sum_x3_build = sum_x3_build + math.pow(x_build[i], 3)
        sum_x2y_build = sum_x2y_build + (math.pow(x_build[i], 2) * y_build[i])
        sum_x4_build = sum_x4_build + math.pow(x_build[i], 4)
        sum_x5_build = sum_x5_build + (math.pow(x_build[i], 5))
        sum_x3y_build = sum_x3y_build + (math.pow(x_build[i], 3) * y_build[i])
        sum_x6_build = sum_x6_build + (math.pow(x_build[i], 6))
    x_ser_build = sum_x_build/n_build
    y_ser_build = sum_y_build/n_build
    p_xy_sum = 0.0
    p_x_sum = 0.0
    p_y_sum = 0.0
    for i in range(n_build):
        p_xy_sum = p_xy_sum + ((x_build[i] - x_ser_build)*(y_build[i] - y_ser_build))
        p_x_sum = p_x_sum + ((x_build[i] - x_ser_build)*(x_build[i] - x_ser_build))
        p_y_sum = p_y_sum + ((y_build[i] - y_ser_build)*(y_build[i] - y_ser_build))
    arr = [[n_build, sum_x_build, sum_x2_build, sum_x3_build, sum_y_build], [sum_x_build, sum_x2_build, sum_x3_build, sum_x4_build, sum_xy_build], [sum_x2_build, sum_x3_build, sum_x4_build, sum_x5_build, sum_x2y_build], [sum_x3_build, sum_x4_build, sum_x5_build, sum_x6_build, sum_x3y_build]]
    koefs = kramer(arr, 4)
    print(" => polinomial (n=3):")
    print("  a1 = " + str(koefs[0]))
    print("  a2 = " + str(koefs[1]))
    print("  a3 = " + str(koefs[2]))
    print("  a4 = " + str(koefs[3]))
    koef_kor = p_xy_sum/((math.sqrt(p_x_sum))*(math.sqrt(p_y_sum)))
    print("  koef kor = " + str(koef_kor))
    r2_yt = 0
    r2_y = 0
    for i in range(n_build):
        yti = koefs[0] + x_build[i] * koefs[1] + koefs[2] * math.pow(x_build[i], 2) + koefs[3] * math.pow(x_build[i], 3)
        r2_yt = r2_yt + math.pow(y_build[i] - yti, 2)
        r2_y = r2_y + math.pow(y_build[i] - y_ser_build, 2)
        yt.append(yti)
    r2 = 1 - (r2_yt/r2_y)
    print("  r^2 = " + str(r2))
    r2_yt_test = 0
    r2_y_test = 0
    sum_y_test = 0
    for i in range(n_test):
        sum_y_test = sum_y_test + y_test[i]
    y_ser_test = sum_y_test / n_test
    for i in range(n_test):
        yti = koefs[0] + x_test[i] * koefs[1] + koefs[2] * math.pow(x_test[i], 2) + koefs[3] * math.pow(x_test[i], 3)
        r2_yt_test = r2_yt_test + math.pow(y_test[i] - yti, 2)
        r2_y_test = r2_y_test + math.pow(y_test[i] - y_ser_test, 2)
    r2_test = 1 - (r2_yt_test/r2_y_test)
    print("  r^2 (test) = " + str(r2_test) + "\n")
    x_build = sorted(x_build)
    for i in range(n_build):
        yt3.append(koefs[0] + x_build[i] * koefs[1] + koefs[2] * math.pow(x_build[i], 2) + koefs[3] * math.pow(x_build[i], 3))
    plot.plot(x_build, yt3, label = "polinomial (n=3)", color="yellow")

def log_model(x_arr, y_arr, n, plot):
    x_build = []
    y_build = []
    x_test = []
    y_test = []
    n_build = 0
    n_test = 0
    for i in range(n):
        if i % 5 == 0:
            x_test.append(x_arr[i])
            y_test.append(y_arr[i])
            n_test = n_test + 1
        else:
            x_build.append(x_arr[i])
            y_build.append(y_arr[i])
            n_build = n_build + 1
    yt = []
    ytl = []
    sum_x_build = 0.0
    sum_y_build = 0.0
    sum_ln_x_build = 0.0
    sum_ln2_x_build = 0.0
    sum_yln_x_build = 0.0
    for i in range(n_build):
        sum_x_build = sum_x_build + x_build[i]
        sum_y_build = sum_y_build + y_build[i]
        sum_ln_x_build = sum_ln_x_build + math.log(x_build[i])
        sum_ln2_x_build = sum_ln2_x_build + math.pow(math.log(x_build[i]), 2)
        sum_yln_x_build = sum_yln_x_build + (y_build[i]*math.log(x_build[i]))
    x_ser_build = sum_x_build/n_build
    y_ser_build = sum_y_build/n_build
    p_xy_sum = 0.0
    p_x_sum = 0.0
    p_y_sum = 0.0
    for i in range(n_build):
        p_xy_sum = p_xy_sum + ((x_build[i] - x_ser_build)*(y_build[i] - y_ser_build))
        p_x_sum = p_x_sum + ((x_build[i] - x_ser_build)*(x_build[i] - x_ser_build))
        p_y_sum = p_y_sum + ((y_build[i] - y_ser_build)*(y_build[i] - y_ser_build))
    arr = [[n_build, sum_ln_x_build, sum_y_build], [sum_ln_x_build, sum_ln2_x_build, sum_yln_x_build]]
    koefs = kramer(arr, 2)
    print(" => log:")
    print("  a1 = " + str(koefs[0]))
    print("  a2 = " + str(koefs[1]))
    koef_kor = p_xy_sum/((math.sqrt(p_x_sum))*(math.sqrt(p_y_sum)))
    print("  koef kor = " + str(koef_kor))
    r2_yt = 0
    r2_y = 0
    for i in range(n_build):
        yti = koefs[0] + math.log(x_build[i]) * koefs[1]
        r2_yt = r2_yt + math.pow(y_build[i] - yti, 2)
        r2_y = r2_y + math.pow(y_build[i] - y_ser_build, 2)
        yt.append(yti)
    r2 = 1 - (r2_yt/r2_y)
    print("  r^2 = " + str(r2))
    r2_yt_test = 0
    r2_y_test = 0
    sum_y_test = 0
    for i in range(n_test):
        sum_y_test = sum_y_test + y_test[i]
    y_ser_test = sum_y_test / n_test
    for i in range(n_test):
        yti = koefs[0] + math.log(x_test[i]) * koefs[1]
        r2_yt_test = r2_yt_test + math.pow(y_test[i] - yti, 2)
        r2_y_test = r2_y_test + math.pow(y_test[i] - y_ser_test, 2)
    r2_test = 1 - (r2_yt_test/r2_y_test)
    print("  r^2 (test) = " + str(r2_test) + "\n")
    x_build = sorted(x_build)
    for i in range(n_build):
        ytl.append(koefs[0] + math.log(x_build[i]) * koefs[1])
    plot.plot(x_build, ytl, label = "log", color="brown")

def exp_model(x_arr, y_arr, n, plot):
    x_build = []
    y_build = []
    x_test = []
    y_test = []
    n_build = 0
    n_test = 0
    for i in range(n):
        if i % 5 == 0:
            x_test.append(x_arr[i])
            y_test.append(y_arr[i])
            n_test = n_test + 1
        else:
            x_build.append(x_arr[i])
            y_build.append(y_arr[i])
            n_build = n_build + 1
    yt = []
    yte = []
    sum_x_build = 0.0
    sum_y_build = 0.0
    sum_e_x_build = 0.0
    sum_e_2x_build = 0.0
    sum_ye_x_build = 0.0
    for i in range(n_build):
        sum_x_build = sum_x_build + x_build[i]
        sum_y_build = sum_y_build + y_build[i]
        sum_e_x_build = sum_e_x_build + math.exp(x_build[i])
        sum_e_2x_build = sum_e_2x_build + math.exp(x_build[i] * 2)
        sum_ye_x_build = sum_ye_x_build + (y_build[i] * math.exp(x_build[i]))
    x_ser_build = sum_x_build/n_build
    y_ser_build = sum_y_build/n_build
    p_xy_sum = 0.0
    p_x_sum = 0.0
    p_y_sum = 0.0
    for i in range(n_build):
        p_xy_sum = p_xy_sum + ((x_build[i] - x_ser_build)*(y_build[i] - y_ser_build))
        p_x_sum = p_x_sum + ((x_build[i] - x_ser_build)*(x_build[i] - x_ser_build))
        p_y_sum = p_y_sum + ((y_build[i] - y_ser_build)*(y_build[i] - y_ser_build))
    arr = [[n_build, sum_e_x_build, sum_y_build], [sum_e_x_build, sum_e_2x_build, sum_ye_x_build]]
    koefs = kramer(arr, 2)
    print(" => exp:")
    print("  a1 = " + str(koefs[0]))
    print("  a2 = " + str(koefs[1]))
    koef_kor = p_xy_sum/((math.sqrt(p_x_sum))*(math.sqrt(p_y_sum)))
    print("  koef kor = " + str(koef_kor))
    r2_yt = 0
    r2_y = 0
    for i in range(n_build):
        yti = koefs[0] + math.exp(x_build[i]) * koefs[1]
        r2_yt = r2_yt + math.pow(y_build[i] - yti, 2)
        r2_y = r2_y + math.pow(y_build[i] - y_ser_build, 2)
        yt.append(yti)
    r2 = 1 - (r2_yt/r2_y)
    print("  r^2 = " + str(r2))
    r2_yt_test = 0
    r2_y_test = 0
    sum_y_test = 0
    for i in range(n_test):
        sum_y_test = sum_y_test + y_test[i]
    y_ser_test = sum_y_test / n_test
    for i in range(n_test):
        yti = koefs[0] + math.exp(x_test[i]) * koefs[1]
        r2_yt_test = r2_yt_test + math.pow(y_test[i] - yti, 2)
        r2_y_test = r2_y_test + math.pow(y_test[i] - y_ser_test, 2)
    r2_test = 1 - (r2_yt_test/r2_y_test)
    print("  r^2 (test) = " + str(r2_test) + "\n")
    x_build = sorted(x_build)
    for i in range(n_build):
        yte.append(koefs[0] + math.exp(x_build[i]) * koefs[1])
    plot.plot(x_build, yte, label = "exp", color="lime")

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
        print("-----" + str(name) + "-----")
        linear_model(x, y, num_rows, plt)
        polinomial_model_2(x, y, num_rows, plt)
        polinomial_model_3(x, y, num_rows, plt)
        try:
            log_model(x, y, num_rows, plt)
        except:
            pass
        exp_model(x, y, num_rows, plt)
        plt.xlabel(xl)
        plt.ylabel(yl)
        plt.title(name)
        plt.legend()
        plt.show()
    