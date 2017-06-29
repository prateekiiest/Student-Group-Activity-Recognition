f = open('ProximityData\groups_05292013.txt','r')
lines = []
lines.append(f.readlines())
textlines = []
for i in range(len(lines[0])): 
    textlines.append( lines[0][i].split("|"))
    


time = []
for i in range(len(textlines)):
    time.append((int(textlines[i][0])))    

group = [[] for h in range(len(time))]
for i in range(len(textlines)):
    for p in range(1,len(textlines[i])-1):
        group[i].append((textlines[i][p]))    
    
           
gr = group[0]
for ip in range(1,len(group)):
    gr += group[ip]
                
unique_group = list(set(gr))

stable_group = []
for g in range(len(unique_group)):

    t =  (cummulative_diff(group_time(unique_group[g])))
    if(t.count(1) > 5):
        #print t
        stable_group.append(unique_group[g])
        
        
        
def group_time(uniquegroup):          
    uniqtime = [] 
    for gr in range(len(group)): 
        for br in range(len(group[gr])):
            
            if(group[gr][br] == uniquegroup):
                uniqtime.append(time[gr])
    return uniqtime
    

    
stablegroup = []    
for r in range(len(stable_group)):

    stablegroup.append(stable_group[r].split(",")) 

stableuniqgroup = []    
for r in range(len(unique_group)):
   
    stableuniqgroup.append(unique_group[r].split(","))    
   
# Function checks the audio level of a particular group
def check_audio_level_uniqgroup(usergroup):
    for k in range(len(stableuniqgroup)):
        if(usergroup == stableuniqgroup[k]):
            p = group_time(unique_group[k])
        
    re = p   
    
    audiolevel = [[] for il in range(len(usergroup))]    
    for gt in range(len(usergroup)):    
    
        #audiolevel = [] 
            
        filn = 'audio\\'+ usergroup[gt].replace(" ","") + '\\audio_' + usergroup[gt].replace(" ","") + '_' + '04132013.txt'
        iof = open(filn,'r')
        linesaudio = []
        linesaudio.append(iof.readlines())
        timeli = []                          # checking the audio levels of the user
        for ku in range(len(linesaudio[0])):
            linesaudio[0][ku] = linesaudio[0][ku].split(",")
        for ki in range(len(linesaudio[0])):    
            timeli.append(linesaudio[0][ki][0])
        
        co = timeli
        for y in range(len(p)):
            for x in range(len(timeli)): 
                if(re[y] == int(co[x]) ):
                    audiolevel[gt].append(linesaudio[0][x][1].replace("\n",""))
                    

        pu = audiolevel

        c = 0
        
        for lu in range(len(pu)):
            for ky in range(len(pu)):
                if(lu != ky):
                    for s in range(len(pu[lu])):
                        for t in range(len(pu[ky])):
                            if(s == t):
                                if(pu[lu][s] == pu[ky][t]):
                                    c += 1     
        psame = (c/2)
        su = []       
        for kg in range(len(pu)):
            su.append(len(pu[kg]))
        
    sumof = min(su)           
    if(sumof == 0):
        #print("Not Same")   
        percent = 0
    else:         
        percent = (psame/(sumof * 1.0))        
    
    if(percent>0.8):  # if 80% of the audio level of the users in close proximity match then we conclude that it forms a real group
        return 1
    else:
        return 0

# Same group = 1
# Not same = 0    

%matplotlib inline

import matplotlib.pyplot as plt
userno = [i for i in range(121)]
gry = [2 for i in range(121)]
value = [check_audio_level_uniqgroup(stableuniqgroup[i]) for i in range(121)]

plt.plot(userno,value,'o')
plt.plot(userno,gry,'o',color = 'red')
plt.ylim(-1,5)
plt.legend('2')
plt.show()        
    
    
    
noofgroups = 0    
for u in range(len(stableuniqgroup)):
    if(check_audio_level_uniqgroup(stableuniqgroup[u]) == 1):
        noofgroups += 1
        # no of uniquegroups based on audio level checking
        
        
no = 0    
for u in range(len(stablegroup)):
    if(check_audio_level_uniqgroup(stablegroup[u]) == 1):
        no += 1
        
         # no of groups based on audio level checking
        
