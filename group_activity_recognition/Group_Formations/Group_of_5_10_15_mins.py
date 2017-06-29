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
    for p in range(1,len(textlines[i])-1):  # storing groups formed
        group[i].append((textlines[i][p]))    
        
      
        
gr = group[0]
for ip in range(1,len(group)):
    gr += group[ip]
                
unique_group = list(set(gr))



def cummulative_diff(li):
    p = [0]
    for j in range(1,len(li)):
        p.append(li[j] - li[j-1])
    return p 

# appending time index and the group formed at that time in a list
def group_time(uniquegroup):          
    uniqtime = [] 
    for gr in range(len(group)): 
        for br in range(len(group[gr])):
            
            if(group[gr][br] == uniquegroup):
                uniqtime.append(time[gr])
    return uniqtime
    
# finding the time indices at which the group occurs

stable_group5 = []
for g in range(len(unique_group)):

    t =  (cummulative_diff(group_time(unique_group[g])))
    if(t.count(1) > 5):
        #print t
        stable_group5.append(unique_group[g])
        
# Checking for groups who have spend time for about 5 minutes


print(stable_group5[2])


stable_group10 = []
for g in range(len(unique_group)):

    t =  (cummulative_diff(group_time(unique_group[g])))
    if(t.count(1) > 10):
        #print t
        stable_group10.append(unique_group[g])
        
        
print(stable_group10[0])

stable_group15 = []
for g in range(len(unique_group)):

    t =  (cummulative_diff(group_time(unique_group[g])))
    if(t.count(1) > 15):
        #print t
        stable_group15.append(unique_group[g])
        
print(stable_group15[3])
