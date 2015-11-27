#!//home/lui/anaconda/bin/python
#-*- coding:utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt



def load_data(data_file):
    
    file=open(data_file,"r")
    start=file.readline()
    data=file.read()
    print"start openning data : ",start,"\n",data
    file.close()
    dat_value=0
    return(data) 


def scatter(x,y):
    plt.scatter(x,y)
    plt.show()




def main():
   donee=load_data("LOG_2015-11-20_09-21-04mma8888_3-axis_Accelerometer.log")


if __name__ == '__main__':
    main()
