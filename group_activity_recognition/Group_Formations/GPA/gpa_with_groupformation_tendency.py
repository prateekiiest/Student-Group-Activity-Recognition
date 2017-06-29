
import csv 
from glob import glob

import os

filn = open('GradesRelation.csv','a')
f = open('grades.csv','r')

li = []
li.append(f.readlines())
f.close()

for i in range(1,len(li[0])):
    li[0][i] = li[0][i].split(",")
    
user = []       # storing the user id and their corresponding gpa
for i in range(1,len(li[0])):
    user.append(li[0][i][0])
    
gpa = []    
for i in range(1,len(li[0])):
    gpa.append(li[0][i][1])
    
    
filname = ['Day_04222013' ,'Day_04232013', 'Day_04242013' , 'Day_04252013' , 'Day_04262013' , 'Day_04272013' ,'Day_05222013' , 'Day_05232013', 'Day_05242013' , 'Day_05252013' , 'Day_05262013' , 'Day_05272013' , 'Day_05282013' , 'Day_05292013']    


# for the above filenames we create a file containing the user_ids, the number of groups that they formed and their gpa
for na in range(len(user)):
    su = 0
    for r in range(len(filname)):
        if(os.path.isfile( filname[r] + '\ ' + user[na] + '.csv') == True):
            fil = open( filname[r] + '\ ' + user[na] + '.csv' , 'r')
            line =[]
            line.append(fil.readlines())
            fil.close()
            z = len(line[0]) - 1
            su += z
            
    filn.writelines(user[na] + ',' + str(su) + ',' + gpa[na] + '\n ')
            
        
