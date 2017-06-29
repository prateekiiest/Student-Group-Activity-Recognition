import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np
import os
from glob import glob

p = 'JCPearsonPlots2'
os.makedirs(p)
main_directory = 'JC'

files_list = glob(os.path.join('JC1\JC', '*.txt'))
for a_file in sorted(files_list):
    #print(a_file)
    filename = a_file
    fil = open(filename, 'r')
    lines = []
    lines.append(fil.readlines())
    textlines = []
    for i in range(len(lines[0])):
        textlines.append( lines[0][i].split(","))

    time  = []
    JC = []
    Pearson_coefficient  = []
    for j in range(len(textlines)):
        time.append(textlines[j][0])  # appending the time index
        JC.append(textlines[j][1])    # appending the Jaccard Index coefficient for that particular time
        Pearson_coefficient.append(textlines[j][2])  # appending the Pearson coefficient for that particular time

    for k in range(len(time)):
        time[k] = int(time[k])  # converting to int
    for k in range(len(JC)):
        JC[k] = float(JC[k])  # converting to float
    for k in range(len(Pearson_coefficient)):
        Pearson_coefficient[k] = float(Pearson_coefficient[k])
    # Plotting

    plot1, = plt.plot(time,JC, 'o', linewidth = '4',color = 'red' ,label = 'JC')
    plot2, = plt.plot(time,Pearson_coefficient,'o',color = 'green' ,label = 'PC' ,linewidth = '5')
    
    plt.legend([plot1,plot2],["JaccardIndex", "PearsoncCoeff."], loc='upper left')
    plt.xticks([0, 180,360,540,720,900,1080,1260,1440])
    plt.xlabel('Time')
    plt.ylabel('JaccardIndex  &  PearsonCoeff.')
    plt.grid(animated = True)
    
    # Saving the plots
    name = a_file
    afile = a_file.replace('.txt','.png')
    Afil = afile.replace('JC\\','')
    A_fil = Afil.replace('JC1\\','')
    fileplot = p + '\ ' + A_fil
    plt.savefig(fileplot, dpi = 150)
    plt.close()
