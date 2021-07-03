import csv
import datetime
import random

initdate = datetime.datetime(2021, 1, 1, 0, 0, 0)
basetemp = -10

#Area name
areas = ['Frozen-A', 'Frozen-B', 'Frozen-C']

csvbasedir = '/Users/sotaro/Documents/CSV'
#Scsvbasedir = 'C:/temp'

# csv header
fieldnames = ['area', 'timestamp', 'temperature']

# csv data
with open(csvbasedir+'/BITestData/tempmonitor.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fieldnames)

    for area in areas:

        if area.endswith('C'):
            offset = 0.5
        else:
            offset = 0
        
        mydate = initdate
        myhours = 0
        while mydate < datetime.datetime.now():
            #mesuredate = initdate + datetime.timedelta(days=passeddays)
            mydate = initdate + datetime.timedelta(hours=myhours)
            measuredtemp = round(basetemp + random.uniform(-3, 1.5), 4)+offset
            row = [area, mydate, measuredtemp]
            writer.writerow(row)
            myhours += 1
