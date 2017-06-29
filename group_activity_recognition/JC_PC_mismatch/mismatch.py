import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np
from glob import glob
import re
from datetime import datetime
from collections import defaultdict
import csv
import os


    
    
    
J= []
P = [] 
mismatch = 0
nofiles = 0
files_list = glob(os.path.join('JC', '*.txt'))
for a_file in (files_list):
    #print(a_file)
    nofiles += 1
    filename = a_file
    
    # finding all such files
    
    fil = open(filename, 'r')
    fl  = a_file.split("_")
    lines = []
    lines.append(fil.readlines())   # Reading from file

    fil.close()
    textlines = []
    for i in range(len(lines[0])):
        textlines.append( lines[0][i].split(","))

    time  = []
    JC = []
    Pearson_coefficient  = []

    for j in range(len(textlines)):
        time.append(textlines[j][0])
        JC.append(textlines[j][1])
        Pearson_coefficient.append(textlines[j][2])


    for k in range(len(time)):
        time[k] = int(time[k])

    for k in range(len(JC)):
        JC[k] = float(JC[k])     # We store the JaccardIndex, pearson coefficent value and the time index as previously done

    for k in range(len(Pearson_coefficient)):
        Pearson_coefficient[k] = float(Pearson_coefficient[k])
    
    
    ft = open('LocationData\\'+ 'wifiLoc_' + fl[4],'r')

    li= []
    
    li.append(ft.readlines())    
    
    ft.close()
    for r in range(len(li[0])):
        li[0][r] = re.split('[ , :]',li[0][r])
    
        
    
    ik =1    
    while(ik < len(li[0]) - 5):    
        t = ik    
        Jac = []   # we take 5 mins of data, check if two users are in same location and same time , and then append the Jaccard Coefficient and Pearson Coefficient
        Pac = []
        jacsu = 0
        while(t < (5 + ik )):
            if fl[2] in (li[0][t]) and fl[3] in (li[0][t]):
                for h in range(len(li[0][t])):
                    if(fl[2] == li[0][t][h]):
                        loc2 =  li[0][t][h+1]
                for h in range(len(li[0][t])):
                    if(fl[3] == li[0][t][h]):
                        loc3 =  li[0][t][h+1]
                   
                if(loc2 == loc3):
                       # if two locations are equal
                    Jac.append(JC[t])
                    Pac.append(Pearson_coefficient[t])
                    
                    if((Jac) == [0.0, 0.0, 0.0, 0.0, 0.0]):
                        # if Jac coefficient is 0 for consecutive 5 minutes
                        mismatch += 1
                        
            t += 1
            
        ik +=1       

# iter the loop

