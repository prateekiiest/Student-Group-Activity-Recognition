
import os
from glob import glob

from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
import matplotlib.pyplot as plt

filename = []
files_list = glob(os.path.join('ProximityData', '*.txt'))
for a_file in sorted(files_list):
   
    filename.append(a_file)  # checking all the files in the give folder

for nk in range(len(filename)):
    for rt in range(len(filename)):
        if(filename[nk] != filename[rt]):
            
               
            f = open(filename[nk],'r')
            lines1 = []
            lines1.append(f.readlines())   # Reading
            textlines1 = []
            for i in range(len(lines1[0])): 
                textlines1.append( lines1[0][i].split("|"))
                
            
            # For first file
            time = []
            for i in range(len(textlines1)):
                time.append((int(textlines1[i][0])))    
            
            group = [[] for h in range(len(time))]
            for i in range(len(textlines1)):
                for p in range(1,len(textlines1[i])-1):
                    group[i].append((textlines1[i][p]))
                    
                    
            # For second file
            gf = open(filename[rt],'r')
            lines2 = []
            lines2.append(gf.readlines())
            textlines2 = []
            for i in range(len(lines2[0])): 
                textlines2.append( lines2[0][i].split("|"))
                
                        
            time2 = []
            for i in range(len(textlines2)):
                time2.append((int(textlines2[i][0])))    
            
            group2 = [[] for h in range(len(time2))]
            for i in range(len(textlines2)):
                for p in range(1,len(textlines2[i])-1):
                    group2[i].append((textlines2[i][p]))
                   
            
                   
            gr = group[0]
            for ip in range(1,len(group)):
                gr += group[ip]
                
            unique_group = list(set(gr))             #suffix 2 indicates attributes for second file, otherwise for first file
            
            gr = group2[0]
            for ip in range(1,len(group2)):
                gr += group2[ip]
                
            unique_group2 = list(set(gr))
            
            
            
            group = [[] for h in range(len(time))]
            for i in range(len(textlines1)):
                for p in range(1,len(textlines1[i])-1):
                    group[i].append((textlines1[i][p]))
            
            
            
            group2 = [[] for h in range(len(time2))]
            for i in range(len(textlines2)):
                for p in range(1,len(textlines2[i])-1):
                    group2[i].append((textlines2[i][p]))
                    
            common = []
            for gt in range(len(unique_group)):
                for bt in range(len(unique_group2)):
                    if(unique_group[gt] == unique_group2[bt]):
                        common.append(unique_group[gt])
                        
                        
            timeof1 = []
            timeof2 = []
            
            
            for gh in range(len(group)):
                for d in range(len(common)):
                    if(common[d] in group[gh]):
                        timeof1.append(time[gh])
                        
            for gh in range(len(group2)):
                for d in range(len(common)):
                    if(common[d] in group2[gh]):
                        timeof2.append(time2[gh])
            
            
            # Comparing two files
            bn = 0
            for k in range(len(timeof1)):
                for p in range(len(timeof2)):
                    if(timeof1[k] == timeof2[p]):
                        #print(timeof1[k])
                        bn +=1
            print("For filenames {} and {}".format(filename[nk],filename[rt]))            
            print("Number of same group occurences is {}".format(bn))
            print("\n")
            
                                                
            f.close()
            gf.close()
