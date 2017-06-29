import matplotlib.pyplot as plt


'''
for May 20 - 25
'''
date = ['May 25','May 24','May 23','May 22','May 21','May 20']

for num in date:

    string = num

    f = open('project26.txt')
# Checking for the above dates in the file project26.txt

    contents = f.read()

# dividing one minute (60 seconds) into 4 parts -> 0,1,2,3
    timedict = {'00': 0, '15' : 1, '30' : 2, '45' :3}



    p=0


    timelist = []
    for k in range(len(contents) - 6):  # Checking for Lines containing that particular date
        if(string == contents[k:k+6]):
            z = (contents[k+7:k+6+9])
            exp = timedict[z[6:8]] + (4 * int(z[3:5])) + (4 * 60 * int(z[0:2]))  # Extracting time from the line and calculating it in minutes
            timelist.append(exp)  
            p += 1  


    # Similar as above
    # Plotting for different dates



    totallist = [0 for k in range(5760)]

    for h in range(len(timelist)):
        totallist[timelist[h]] = 1




    plt.bar([b for b in range(len(totallist))],[totallist[v] for v in range(len(totallist))])

    plt.xlabel('Data Points through the whole day of' + num)
    plt.ylabel('Probability of Available Data')
    plt.show()

    percentage = (p)/(5760*1.0)
    print(percentage)
    # Calculating the percentage

    f.close() 
