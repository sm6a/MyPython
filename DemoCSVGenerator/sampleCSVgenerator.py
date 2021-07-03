import csv
import datetime
import random

initdate = datetime.datetime(2020, 1, 1, 0, 0, 0)
basetemp = -10

#Area name
destinations = ['shop-A', 'shop-B', 'shop-C','shop-D', 'shop-E']

# csv header
fieldnames = ['destination', 'date', 'arrivedtime']

# csv data
with open('C:/temp/BITestData/deliveredtime.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fieldnames)

    for destination in destinations:
        
        mydate = initdate
        myhours = 0
        while mydate < initdate + datetime.timedelta(days=365):
            #mesuredate = initdate + datetime.timedelta(days=passeddays)
            mydate = initdate + datetime.timedelta(hours=myhours*24)
            hourandom = int(random.uniform(6, 8))
            minuterandom = int(random.uniform(00, 59))
            row = [destination, mydate.date(), str(hourandom).zfill(2)+':'+str(minuterandom).zfill(2)]
            writer.writerow(row)
            myhours += 1
