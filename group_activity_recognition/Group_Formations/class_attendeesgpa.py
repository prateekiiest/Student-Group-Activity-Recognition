import csv
csvlines = []

# reading the gpa value file
with open('grades.csv', 'rb') as csvfile:
    
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
        csvlines.append(row)
        
        

for k in range(len(csvlines)):
    csvlines[k] = csvlines[k][0].split(",")
    
user_id = []    
for k in range(1,len(csvlines)):
    user_id.append(csvlines[k][0])
    
# appending the user_ids in a list    
    
gpa = []
for k in range(1,len(csvlines)):
    gpa.append(float(csvlines[k][1]))   
# appending the gpa values in a list

gpavalue = {}
for i in range(len(user_id)):
    gpavalue[user_id[i]] = gpa[i]
# matching user_id to his/her gpa    
    
def gpa_finder(fg):
    gpauser = []
    for j in range(len(user_id)):       
        if(user_id[j] in fg):
            gpauser.append(float(gpa[j]))      
    return gpauser
    
    
for g in range(len(classmembers)):
    if classmembers[g] in user_id:
        print(gpavalue[ classmembers[g]])
