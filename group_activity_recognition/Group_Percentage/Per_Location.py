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
        
filid = ['22','23','24','25','26','27','28','29']
filname = 'uniqueGroup_05' + filid[0] + '2013_bin5.txt'
fil = open(filname,'r')
lines = []
lines.append(fil.readlines())

for r in range(len(lines[0])):
    lines[0][r] = re.split('[ |]',lines[0][r])
    

    
time = []
for k in range(len(lines[0])):
    #p = (lines[0][k][1]).split(",")
    p = re.split('[ , ;]',lines[0][k][1])
    time.append((p))
    

usergroups = []
for k in range(len(lines[0])):
    p = (lines[0][k][0])
    p = p.split(";")
    usergroups.append(p[0])   


t = [[] for r in range(len(time))]
for r in range(len(time)):
    for j in range(0,len(time[r]),2):   # time index
        t[r].append(time[r][j])   
    
    
duration = [[] for r in range(len(time))]
for r in range(len(time)):
    for j in range(1,len(time[r]),2):
        duration[r].append(time[r][j])    # duration index
    

    
uniqgroup = list(set(usergroups))

for i in range(len(uniqgroup)):
    for j in range(len(usergroups)):
        if(uniqgroup[i] == usergroups[j]):
            print(usergroups[j])
            for c in usergroups[j].split(","):
                for h in range(len(t[j])):
                    (timefindr(c,int(t[j][h],filid[0])))
            print('\n')
    

    # We create a csv file, store the number of groups formed at different locations through out the day along with the duration of the group.
fg = open('GroupsLcationPercebntage22.csv','a')
    
for i in range(len(uniqgroup)):
    x = uniqgroup[i].split(",")
    us = x[0]
    for r in range(1,len(x)):
        us = us + ' ' + x[r]
    loco = []
    tim = []
    for j in range(len(usergroups)):
        if(uniqgroup[i] == usergroups[j]):
            
            for h in range(len(t[j])):
                v = usergroups[j].split(",")
                
                for c in range(len(v)):
                    
                    if((timefindr(v[c],int(t[j][h]),(filid[0]))) != []):
                        loco.append((timefindr(v[c],int(t[j][h]),(filid[0])))[0])
                tim.append(int(duration[j][h]))
    d = defaultdict(int)
    for p in loco:
        d[p] += 1
    result = max(d.iteritems(), key=lambda x: x[1])  # checking whether maximum of users in a group are in a particular location.
    loc = list(result)
    z = ((sum(tim)*100/(1440*1.0)))
    fg.writelines(us+','+str(z) + ',' +loc[0] + '\n')
fg.close()    
