#!//home/lui/anaconda/bin/python
#-*- coding:utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def load_data(data_file):

    name = ["A", "time","B","x","y","z","C"]
    pandas_data=pd.read_table(data_file, sep=";", skiprows=1, names=name, decimal=",")

    scatter(pandas_data["x"],pandas_data["z"])

    return pandas_data

def scatter(x,y):
    print x,y
    plt.scatter(np.array(x),np.array(y))
    plt.show()




def main():
   donee=load_data("o.log")


if __name__ == '__main__':
    main()
