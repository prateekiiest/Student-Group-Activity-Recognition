% matplotlib inline
import matplotlib.pyplot as plt
'''
for May 26
'''
string = 'May 30'
# Reading from file project30.txt which contains data on May 30
f2 = open('project30.txt')
contents = f2.read()
# dividing a minute (60 seconds) into 4 parts -> 0,1,2,3
timedict = {'00': 0, '15' : 1, '30' : 2, '45' :3}

p=0
timelist = []
for k in range(len(contents) - 6):  # string = May 30 is unique and has length 6. So we extract 6 letter word where word - May 30

    if(string == contents[k:k+6]):
        z = (contents[k+7:k+6+9])
        exp = timedict[z[6:8]] + (4 * int(z[3:5])) + (4 * 60 * int(z[0:2]))  # Extracting time part from each such line.
        timelist.append(exp)
        p += 1
        
        
# p = total no of available data points
totallist = [0 for k in range(5760)]

for h in range(len(timelist)):
    totallist[timelist[h]] = 1
  

 # totallist denotes data points = 1 if available, 0 if unavailable
    # timelist = time points through out the day

plt.bar([b for b in range(len(totallist))],[totallist[v] for v in range(len(totallist))])
plt.xlabel('Data Points through the whole day')
plt.ylabel('Probability of Available Data')
plt.show()

percentage = (p)/(5760*1.0)

# percentage =denotes percentage of available data points

print(percentage)

#f.close()
f2.close()
