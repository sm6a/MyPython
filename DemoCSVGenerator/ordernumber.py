import csv
import datetime
import random

initdate = datetime.datetime(2021, 1, 1, 0, 0, 0)
basetemp = -10

#Area name
ra = [1,2,3,4,5]
ca = [1,2,3]
#csvbasedir = '/Users/sotaro/Documents/CSV'
csvbasedir = 'C:/temp'

# csv header
fieldnames = ['ordernumber', 'starttime', 'endtime']

# csv data
with open(csvbasedir+'/BITestData/occupation.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fieldnames)

    for ri in ra:
        for ci in ca:
            offset = random.uniform(0,0.2)
            mydate = initdate
            myhours = 0
            while mydate < datetime.datetime.now():
                #mesuredate = initdate + datetime.timedelta(days=passeddays)
                mydate = initdate + datetime.timedelta(hours=myhours*24)
                row = ['ROW'+str(ri).zfill(3)+'-C'+str(ci).zfill(2), mydate.date(),round(random.uniform(0.3,0.8)+offset)]
                writer.writerow(row)
                myhours += 1
                writer.writerow()
                # to do 
                # generate order number 
                # random start time and end time
