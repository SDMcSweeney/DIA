# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:14:04 2022

@author: elec_
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#read specified CSV's and call plot_results
def read_results(filename):
    
    string = "FILE LOCATION"
    string2 = ".csv"
    string+=filename
    string+=string2
    df = pd.read_csv(f'{string}', 
        sep=',', index_col=False)
    plot=df.set_index('Time').plot(ylim=(0,8),xlim=(0,2000),title=f"{filename}",)
    plot.set_xlabel("Time")
    plot.set_ylabel("Avg prey weightings")
    plot.set_title("TITLE")

    return 
    


if __name__ == '__main__':
    
    filename = 'FILE NAME'
    #value = read_results(filename)
    print(value)
