#!//home/lui/anaconda/bin/python
#-*- coding:utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def load_data(data_file):

    name = ["A", "time","B","x","y","z","C"]
    pandas_data=pd.read_table(data_file, sep=";", skiprows=1, names=name, decimal=",")
    print"\n", "pandas data",pandas_data

    scatter(pandas_data["x"],pandas_data["y"])

    return pandas_data

def scatter(x,y):
    plt.scatter(x,y)
    plt.show()




def main():
   donee=load_data("LOG_2015-11-20_09-21-04mma8888_3-axis_Accelerometer.log")


if __name__ == '__main__':
    main()
