#!//home/lui/anaconda/bin/python
#-*- coding:utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt



def load_data(data_file):
    
    donnees=np.loadtxt(data_file)
        
    return(donnees[:,1],donnees[:,2]) 


def scatter(x,y):
    plt.scatter(x,y)
    plt.show()




def main():
   donee=load_data("LOG_2015-11-20_09-21-04mma8888_3-axis_Accelerometer.log")


if __name__ == '__main__':
    main()
