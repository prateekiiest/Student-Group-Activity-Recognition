import re
from datetime import datetime
from collections import defaultdict
import csv
import os

na = [str(i) for i in range(60)]
for i in range(len(na)):
    if(len(str(na[i])) == 1):
        na[i] ='u'+ '0' + na[i]
    else:
        na[i] = 'u' + na[i]
        
filid = ['23','24','25','26','27','28']

# For Day 23
filname = 'uniqueGroup_05' + filid[0] + '2013_bin5.txt'

fil = open(filname,'r')

lines = []
lines.append(fil.readlines())

for r in range(len(lines[0])):
    lines[0][r] = re.split('[ |]',lines[0][r])
    
    
    
time = []

for k in range(len(lines[0])):
   
    p = re.split('[ , ;]',lines[0][k][1])
    time.append((p))
    


usergroups = []
for k in range(len(lines[0])):
    p = (lines[0][k][0])    # storing the groups formed in a list
    p = p.split(";")
    usergroups.append(p[0])   


t = [[] for r in range(len(time))]
for r in range(len(time)):            # storing the time index in a list
    for j in range(0,len(time[r]),2):
        t[r].append(time[r][j])   
    
    
duration = [[] for r in range(len(time))]
for r in range(len(time)):
    for j in range(1,len(time[r]),2):   # storing the duration of the group in a list
        duration[r].append(time[r][j])   
    
occurence = []    
for i in range(len(t)):              # how many times the group occured
    occurence.append(len(t[i]))
    
maxoccurgroup = []    
for jl in range(len(occurence)):
    if(occurence[jl] == max(occurence)):    # the group that occured for maximum time 
        print("Group that occurred most  frequently is {}".format(usergroups[jl]))
        maxoccurgroup.append(usergroups[jl])
    
## Checking the maximum times a group formed in a day


##checking  How the group evolved 

    
for i in range(len(usergroups)):
    for c in usergroups[i].split(","):
        if c not in maxoccurgroup[0].split(","):
            print(c)
            print('\n')
    
    
# For Day 24
filname = 'uniqueGroup_05' + filid[1] + '2013_bin5.txt'

fil = open(filname,'r')

lines24 = []
lines24.append(fil.readlines())

for r in range(len(lines24[0])):
    lines24[0][r] = re.split('[ |]',lines24[0][r])
    
    
time24 = []

for k in range(len(lines24[0])):
    #p = (lines[0][k][1]).split(",")
    p = re.split('[ , ;]',lines24[0][k][1])
    time24.append((p))
    


usergroups24 = []
for k in range(len(lines24[0])):
    p = (lines24[0][k][0])
    p = p.split(";")
    usergroups24.append(p[0])   


t24 = [[] for r in range(len(time24))]
for r in range(len(time24)):
    for j in range(0,len(time24[r]),2):
        t24[r].append(time24[r][j])   
    
    
duration24 = [[] for r in range(len(time24))]
for r in range(len(time24)):
    for j in range(1,len(time24[r]),2):
        duration24[r].append(time24[r][j])   
            
        
        
occurence24 = []    
for i in range(len(t24)):
    occurence24.append(len(t24[i]))
    
maxoccurgroup24 = []    
for jl in range(len(occurence24)):
    if(occurence24[jl] == max(occurence24)):
        print("Group that occurred most  frequently is {}".format(usergroups24[jl]))
        maxoccurgroup24.append(usergroups24[jl])
        
        
        
fl =  open('LargeGroup'+ filid[1],'a')
#associate = []
fl.writelines('Group Evolution, Time \n')
for g in range(len(usergroups24)):
    if(maxoccurgroup24[0] in usergroups24[g]):
        for b in range(len(t24[g])):
            ght = usergroups24[g].split(",")
            us = ght[0]
            for ji in range(1,len(ght)):
                us = us + ' ' + ght[ji]
                
            
            fl.writelines(us + ',' + t24[g][b] + '\n')    
        
          

# For Day 25            
filname = 'uniqueGroup_05' + filid[2] + '2013_bin5.txt'

fil = open(filname,'r')

lines25 = []
lines25.append(fil.readlines())

for r in range(len(lines25[0])):
    lines25[0][r] = re.split('[ |]',lines25[0][r])
    
    
time25 = []

for k in range(len(lines25[0])):
    
    p = re.split('[ , ;]',lines25[0][k][1])
    time25.append((p))
    


usergroups25 = []
for k in range(len(lines25[0])):
    p = (lines25[0][k][0])
    p = p.split(";")
    usergroups25.append(p[0])   


t25 = [[] for r in range(len(time25))]
for r in range(len(time25)):
    for j in range(0,len(time25[r]),2):
        t25[r].append(time25[r][j])   
    
    
duration25 = [[] for r in range(len(time25))]
for r in range(len(time25)):
    for j in range(1,len(time25[r]),2):
        duration25[r].append(time25[r][j])   
        
        
        
        
        
occurence25 = []    
for i in range(len(t25)):
    occurence25.append(len(t25[i]))
    
maxoccurgroup25 = []    
for jl in range(len(occurence25)):
    if(occurence25[jl] == max(occurence25)):
        print("Group that occurred most  frequently is {}".format(usergroups25[jl]))
        maxoccurgroup25.append(usergroups25[jl])
        

# For Day 26
filname = 'uniqueGroup_05' + filid[3] + '2013_bin5.txt'

fil = open(filname,'r')

lines26 = []
lines26.append(fil.readlines())

for r in range(len(lines26[0])):
    lines26[0][r] = re.split('[ |]',lines26[0][r])
    
  
    
time26 = []

for k in range(len(lines26[0])):
    #p = (lines[0][k][1]).split(",")
    p = re.split('[ , ;]',lines26[0][k][1])
    time26.append((p))
    

usergroups26 = []
for k in range(len(lines26[0])):
    p = (lines26[0][k][0])
    p = p.split(";")
    usergroups26.append(p[0])   


t26 = [[] for r in range(len(time26))]
for r in range(len(time26)):
    for j in range(0,len(time26[r]),2):
        t26[r].append(time26[r][j])   
    
    
duration26 = [[] for r in range(len(time26))]
for r in range(len(time26)):
    for j in range(1,len(time26[r]),2):
        duration26[r].append(time26[r][j])        
      
        
        
occurence26 = []    
for i in range(len(t26)):
    occurence26.append(len(t26[i]))
    
maxoccurgroup26 = []    
for jl in range(len(occurence26)):
    if(occurence26[jl] == max(occurence26)):
        print("Group that occurred most  frequently is {}".format(usergroups26[jl]))
        maxoccurgroup26.append(usergroups26[jl])
        
