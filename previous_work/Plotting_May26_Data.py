import matplotlib.pyplot as plt
'''
for May 26
'''
string = 'May 26'

# reading from project26.txt file which contains data on May 26
f = open('project26.txt')
contents = f.read()
# reading from project30.txt file which contains data on May 26
f2 = open('project30.txt')
contents2 = f2.read()
# dividing a minute (60 seconds) into 4 parts -> 0,1,2,3
timedict = {'00': 0, '15' : 1, '30' : 2, '45' :3}


# For project26.txt
p=0
timelist = []
for k in range(len(contents) - 6):
    if(string == contents[k:k+6]):  # string = May 26 is unique and has length 6. So we extract 6 letter word where word - May 26
        z = (contents[k+7:k+6+9])
        exp = timedict[z[6:8]] + (4 * int(z[3:5])) + (4 * 60 * int(z[0:2]))  # After the string we have the time section
        timelist.append(exp)   # We calculate the hours,and minutes of the given time and append it.
        p += 1
        
# p - indicates the number of available data points        


# For project30.txt
d = 0
for k in range(len(contents) - 6):
    if(string == contents2[k:k+6]):
        z = (contents2[k+7:k+6+9])    # Similar as above
        exp = timedict[z[6:8]] + (4 * int(z[3:5])) + (4 * 60 * int(z[0:2]))
        timelist.append(exp)
        d += 1     
        
# d - indicates the number of available data points            
        
totallist = [0 for k in range(5760)]


for h in range(len(timelist)):
    totallist[timelist[h]] = 1

    # totallist = denotes the time points through out the day
          
plt.bar([b for b in range(len(totallist))],[totallist[v] for v in range(len(totallist))])
plt.xlabel('Data Points through the whole day')
plt.ylabel('Probability of Available Data')
plt.show()

percentage = (p+d)/(5760*1.0)

#percentage = 3.107%
# percentage = denotes the percentage of data points available on the day
print(percentage)

f.close()
f2.close()
