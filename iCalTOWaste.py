import csv
import time
import datetime

#Make output CSV Files

def MakeFiles(data):
    input_file = open('Calendars.csv', 'r')
    data = csv.reader(input_file)
    for line in data:
        [Calendar,WeekStarting,GreenBin,Garbage,Recycling,YardWaste,ChristmasTree] = line
        if Calendar == "Calendar":
            data.next()
        else:
            subject = ["Subject"]
            startDate = ["Start Date"]
            allDay = ["All Day Event"]
            description = ["Description"]
            new_line = subject + startDate + allDay + description
            csv.writer(open((Calendar +'.csv'), 'w')).writerow(new_line)

#Write Solid Waste Calendars to file.
            
def WriteCal():
    input_file = open('Calendars.csv', 'r') 
    data = csv.reader(input_file)
    for line in data:
        [Calendar,WeekStarting,GreenBin,Garbage,Recycling,Yardwaste,ChristmasTree] = line
        
        if Calendar == "Calendar":
            data.next()
        else:
            day = datetime.datetime.strptime(WeekStarting, '%m/%d/%Y')
            dw = {"M": 7, "T":8, "W":9, "R":10, "F":11, "S":12}
            allDay = ["True"]
            if ChristmasTree != "0":
                subject = ["Christmas Tree/Garbage Day"]
                description = ["In addition to Garbage and Green Bin waste, Christmas tree collection occurs Today. When placing your tree out for collection, please remove all decorations, tinsel, etc and do not place out in any type of bag"]
                startDate = day + datetime.timedelta(dw[ChristmasTree] - day.weekday())
                startDate = [datetime.datetime.strftime(startDate, "%m/%d/%Y")]
            elif Recycling != "0":
                subject = ["Recycling Day"]
                description = ["Put out Recycling and Green Bin waste! For more information on what can be recycled click here: http://www.toronto.ca/garbage/bluebin.htm"]
                startDate = day + datetime.timedelta(dw[Recycling] - day.weekday())
                startDate = [datetime.datetime.strftime(startDate, "%m/%d/%Y")]
            elif Garbage != "0" and ChristmasTree == "0":
                subject = ["Garbage Day"]
                description = ["Put out Garbage, Yard and Green Bin waste! Find basic sorting information here: http://app.toronto.ca/wes/winfo/search.do"]
                startDate = day + datetime.timedelta(dw[Garbage] - day.weekday())
                startDate = [datetime.datetime.strftime(startDate, "%m/%d/%Y")]
            
            new_line = subject + startDate + allDay + description
            csv.writer(open((Calendar +'.csv'), 'a')).writerow(new_line)
            print new_line

MakeFiles()
WriteCal()
