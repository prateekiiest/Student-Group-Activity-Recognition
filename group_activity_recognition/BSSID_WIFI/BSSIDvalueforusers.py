
"""
This code is used to process files for about 57 users on the basis of their wifi data
"""
from datetime import datetime
import csv
import os

### Importing the modules

# Function for converting the time value in the csv files to Year-Month-Day Format
def year(value):

    yeartime = datetime.fromtimestamp(int(value)).strftime('%Y:%m:%d')
    return yeartime

# Function for converting the time value in the csv files to Hours-Minutes-Seconds format
def timevalue(value):
    time = datetime.fromtimestamp(int(value)).strftime('%H:%M:%S')
    return time

# --------------------------------------------------------------------------------------------------------------

##--- Main part of the Program--------------------------

# Creating a string of user ids '00 , 01, 02, 03, O4, 05 ................. 59 '
na = [str(i) for i in range(60)]
for i in range(len(na)):
    if(len(str(na[i])) == 1):
        na[i] = '0' + na[i]

# CSV Files had no user_ids 06, 11, 21 ,26, 28, 29, 37, 38, 40, 48, 55
NOFILES = ['06','11','21','26','28','29','37','38','40','48','55']

for flname in range(len(na)):
    if na[flname] not in NOFILES:   ## Handling exception if no files of the above unavailable user_ids were detected
        filename = 'wifi\wifi'+ '_u' + na[flname] + '.csv'
        lines= []
        with open(filename) as f:               ## Opening the CSV files
            reader = csv.reader(f, delimiter=' ')
            for row in reader:
                lines.append(row)         ### Reading through lines from individual a csv file

        ## line[] contains a list of the LINES of the CSV file
        time =[]
        Year = []
        NElines = []   # NELines denotes the non-empty lines in the csv file
        for i in range(1,len(lines)):
            if(lines[i] != [] ):
                NElines.append(lines[i])
                Year.append(year(int(lines[i][0][0:10])))
        ## Year list contains all the dates of that particular CSV file
        ## UniqueYear contains distinct dates of that particular file, unlike Year which contains some repetitions in its dates
        UniqueYear = list(set(Year))
       
        p = 'User' + str(na[flname])
        os.makedirs(p)
        # Make directory of name User00, User01, ........ User59


        UniqueYear.sort()  # Sort UniqueYear numerically
        Year.sort()    # Sort Year numerically

        for i in range(len(UniqueYear)):  # Loop through the UniqueYear
            #UniqueYear[i][5:7] = Month -> 04
            #UniqueYear[i][8:11] = Day  -> 05                    EXAMPLE = 2013-04-05
            #UniqueYear[i][0:4] = Year  -> 2013

            name =  p +  '\ ' + 'wifi_u'+ na[flname] + '_' + UniqueYear[i][5:7] +   UniqueYear[i][8:11] +  UniqueYear[i][0:4] +'.txt'
            # name = p\wifi_u(user_ids)_monthdayyear.txt

            fil = open(name, 'a')   # Open textfile with name = directory_name\wifi_u(user_ids)_monthdayyear.txt
            fil = open(name,'w')   # Open the textfile for writing

            timetext = []  # Extract the time section from the line
            BSSID = []  # Extract the BSSID no. from the line
            level = [] # Extract the level from the line

            for j in range(len(Year)): # Loop through the whole Year
                if(Year[j] == UniqueYear[i]): # If a match occurs then update the corresponding line's time, BSSID and level values

                    # --------------EXPLANATION  -------------------------------------------------------------------------------------
                    # NElines[j][0][0:10] - Extracting the time values from the csv file. Since each such number in the time column is of length 11, so we are slicing the first 11 characters.
                    # NElines[j][0][0:10][0:2] - Hour Part    , NElines[j][0][0:10][3:5] - Minute Part
                    # BSSID = NElines[j][0][11: 17+11] , Since Each BSSID values start after the first 11 characters(time value) and has a fixed length = 17 characters
                    # level values start after 34 characters and have a length of 3 characters. So level =  NElines[j][0][34:38]

                    timetext.append(str( (int(timevalue(NElines[j][0][0:10])[0:2]))*60 +  int(timevalue(NElines[j][0][0:10])[3:5])))
                    BSSID.append(NElines[j][0][11: 17+11])
                    level.append(NElines[j][0][34:38])


            ptim = timetext  # Copying the time section to ptim
            bs = BSSID   # Copying the BSSID nos to bs
            lve = level  # Copying the level to lve

        ## uniquetime contains distinct time(Hours-Minutes) of that particular file, unlike ptim which contains some repetitions in its time values
            uniquetime = list(set(ptim))

            for h  in range(len(uniquetime)):
                uniquetime[h] = int(uniquetime[h])

            uniquetime.sort()
            ## Sort the uniquetime numerically

            listoflines = []  # Lines to be written in the file
            for d in range(len(uniquetime)):
                t = uniquetime[d]     ## Loop through all the distinct time
                xc = ''
                for g in range(len(ptim)):

                    if(str(t) == ptim[g]):  # Check for matching for time with the values in ptim
                        if(bs[g] not in xc): # to check if the same BSSID value is not repeated
                            xc+= (',' + bs[g]+ ',' + lve[g])  # then append the BSSID and the level value to the end of the line



                listoflines.append('\n'+str(t)+xc)


            fil.writelines(listoflines)  # write the corresponding content in to the file
            fil.close()  # close the text file


        f.close()   # close the csv file
