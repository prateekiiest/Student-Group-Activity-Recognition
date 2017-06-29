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


filname = 'uniqueGroup_04' + filid[n] + '2013_bin5.txt'

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
    for j in range(0,len(time[r]),2):
        t[r].append(time[r][j])   
    
    
duration = [[] for r in range(len(time))]
for r in range(len(time)):
    for j in range(1,len(time[r]),2):
        duration[r].append(time[r][j])   
    
    
    
usergrp = [[] for sd in range(len(usergroups))]        
for r in range(len(usergroups)):
    
    usergrp[r] = usergroups[r].split(",")
    
q = 'Day_04'+ filid[n]+ '2013'
os.mkdir(q)    

# This function checks which user was present with which group at what time during a particular day during month 04
def useracitvityfile(user_id):
    
    data = []    
    #user_id = 'u25'
    for out in range(len(usergrp)): 
    
        for c in usergrp[out]:
            if(user_id == c):
                #print('Group')
                #print(usergrp[out])
                #print('location') 
                for g in range(len(t[out])):
                    o = usergrp[out][0]
                    for f in range(1,len(usergrp[out])):
                        o = o + ' ' + usergrp[out][f]  

                    if(timefinder(user_id,int(t[out][g]),filid[n]) != []):
                        data.append(o +',' + timefinder(user_id,int(t[out][g]),filid[n])[0] + ',' + t[out][g] + ','+ str(int(duration[out][g])) + '\n')
                    else:
                        for h in range(len(usergrp[out])):
                            if(timefinder(usergrp[out][h],int(t[out][g]),filid[n]) != []):
                                data.append( o +',' + timefinder(usergrp[out][h],int(t[out][g]),filid[n])[0] + ',' + t[out][g] +',' + str(int(duration[out][g])) + '\n')

    if(data!= []):        
        fl = open( q + '\ ' + user_id + '.csv' ,'a' )
        sortedlist = sorted(data, key=lambda column: column[2], reverse=False)
        fl.write('User Group, Location, Time, Duration \n')
        for row in sortedlist:
            fl.writelines(row)
        
        fl.close()        
for jt in range(len(na)):
    useracitvityfile(na[jt])




# The function finds the location of an user at a particular time and at a particular date
def timefinder(user,tim,date): 
    filename = 'wifi_location\wifi_location_' + user + '.csv' 
    loclines = []
    with open(filename) as f:               ## Opening the CSV files
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            loclines.append(row)  
            
            
    f.close()             
    for j in range(len(loclines)):
        loclines[j] = loclines[j][0].split(",")
        
    timevalue  = []
    for j in range(1,len(loclines)):
        timevalue.append((loclines[j][0]))
        
    yeardate = []
    for k in range(len(timevalue)):
        yeardate.append(year(timevalue[k]))
    
    location = []
    for j in range(1,len(loclines)):
        location.append((loclines[j][1]))
    
    
    daytime = []
    for k in range(len(timevalue)):
        daytime.append(timeval(timevalue[k]))
    
    day = []
    for k in range(len(daytime)):
        day.append(int(daytime[k][0:2]) *60 + int(daytime[k][3:5]))
    
    loc = []
    #c = 0
    for k in range(len(yeardate)):
        if(yeardate[k] == '2013:04:' + str(date)):
            if(day[k] == tim):
                
                loc.append(location[k])
    #f.close()            
    return list(set(loc))    

       


# Create a file for location backer-berry for month 04 and store the groups formed at what time and what date
locationfil = open('in[backer-berry]04.csv','a')
locationfil.writelines('Group' + ',' +'Time' + ',' + 'Date' + '\n')

       
for ry in range(len(filid)):
    filname = 'uniqueGroup_04' + filid[ry] + '2013_bin5.txt'

    fil = open(filname,'r')
    
    lines = []
    lines.append(fil.readlines())
    
    for r in range(len(lines[0])):
        lines[0][r] = re.split('[ |]',lines[0][r])
        
        
        
    time = []
    
    for kd in range(len(lines[0])):         # appending time index
        
        p = re.split('[ , ;]',lines[0][kd][1])
        time.append((p))
        
    
    
    usergroups = []
    for kp in range(len(lines[0])):
        p = (lines[0][kp][0])
        p = p.split(";")        # the groups formed at that time
        usergroups.append(p[0])   
    
    
    t = [[] for r in range(len(time))]
    for r in range(len(time)):
        for j in range(0,len(time[r]),2):
            t[r].append(time[r][j])   
        
        
    duration = [[] for r in range(len(time))]
    for r in range(len(time)):                      # duration of the group
        for j in range(1,len(time[r]),2):
            duration[r].append(time[r][j])   
        
        
        
        
    usergrp = [[] for sd in range(len(usergroups))]        
    for r in range(len(usergroups)):
        
        usergrp[r] = usergroups[r].split(",")   
               
        

    for k in range(len(usergroups)):
    
        for v in range(len(t[k])):
            if(timefinder(usergrp[k][0], int(t[k][v]), int(filid[ry])) != []):
                if(timefinder(usergrp[k][0], int(t[k][v]), int(filid[ry]))[0] == 'in[backer-berry]'):
                    us = usergrp[k][0]
                    for l in range(1,len(usergrp[k])):    # if location is in backer-berry
                        us = us + ' ' + usergrp[k][l]
                    locationfil.writelines(us + ',' + t[k][v] + ',' + filid[ry] + '\n')
 
 
# Function for converting the year value in the csv files to Day-Month-Year format
def year(value):

    yeartime = datetime.fromtimestamp(int(value)).strftime('%Y:%m:%d')
    return yeartime


# Function for converting the time value in the csv files to Hours-Minutes-Seconds format
def timeval(value):

    time = datetime.fromtimestamp(int(value)).strftime('%H:%M:%S')
    return time
    

