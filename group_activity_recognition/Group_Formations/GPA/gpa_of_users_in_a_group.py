import csv

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

stable_group5 = []
for g in range(len(unique_group)):

    t =  (cummulative_diff(group_time(unique_group[g])))
    if(t.count(1) > 5):
        #print t
        stable_group5.append(unique_group[g])

csvlines = []
with open('grades.csv', 'rb') as csvfile:
    
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
        csvlines.append(row)
        
        

for k in range(len(csvlines)):
    csvlines[k] = csvlines[k][0].split(",")
    
user_id = []    
for k in range(1,len(csvlines)):
    user_id.append(csvlines[k][0])
    
    
    
gpa = []
for k in range(1,len(csvlines)):
    gpa.append(float(csvlines[k][1]))
    
    
def gpa_finder(fg):
    gpauser = []
    for j in range(len(user_id)):
        
        if(user_id[j] in fg):
            gpauser.append(float(gpa[j]))
            
    return gpauser

# gpa finder greater than 3.5
def gpa_finder_greater35(fg):
    gpauser = {}
    for j in range(len(user_id)):
        if(user_id[j] in fg):
            #print(user_id[j])
            if(gpa[j] > 3.5):
                gpauser[user_id[j]] = (float(gpa[j]))
            else:
                gpauser = {}
    return gpauser

# gpa finder greater than 3
def gpa_finder_greater3(fg):
    gpauser = {}
    for j in range(len(user_id)):
        if(user_id[j] in fg):
            #print(user_id[j])
            if(gpa[j] > 3):
                gpauser[user_id[j]] = (float(gpa[j]))
            
    return gpauser
            


more35 = 0
for o in range(len(stable_group5)):
    
    if(all(i >= 3.5 for i in gpa_finder(stable_group5[o])) == True):
        more35 += 1   


more3 = 0
for o in range(len(stable_group5)):
    if(all(i >= 3 for i in gpa_finder(stable_group5[o])) == True):
        more3 += 1
   
   
    
# 31 May    
#4 attended among 24 above 3 gpa
#3 attended among 15 above 3.5 gpa)
    
    
# 0413 2013
# 14 out of 24 3 toppers  
# 7 out of 15 attended 3.5 toppers    
    
 
