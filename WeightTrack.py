import datetime
import csv
from datetime import date


commandLineArt="-"*50


today=date.today()

#returns the differnece in days between two different dates.
def days_between_dates(data):

    date1=data[0][0]
    date2=data[-1][0]
    return abs(date2-date1).days


#returns weight lost so far
def weight_lost(data):
    startWeight=float(data[0][1])
    currentWeight=float(data[-1][1])
    return startWeight-currentWeight

def weight_days_ratio(weight,days):
    return weight/days

def calculate_goal_date(ratio,weight,goalWeight):
    daysNeed=(weight-goalWeight)/ratio

    return daysNeed

def SaveData(data):
    with open("data.csv",'w+') as f:
        wr=csv.writer(f)
        for item in data:
            wr.writerow([item[0].isoformat(),item[1]])
        f.close()

def NewWeightEntry(weight,records):
    dataFormat=[today, weight]
    records.append(dataFormat)
    SaveData(records)

def LoadData():
    data=[]
    with open("data.csv") as f:
        csv_f=csv.reader(f)
        for row in csv_f:
            row_data=[datetime.datetime.strptime(row[0],"%Y-%m-%d").date(),
                     row[1]]


            data.append(row_data)
        f.close()
    return data



def GetWeight():
    weight=None
    while (weight==None):
        userInput=input("Enter weight:")
        try:
            weight=float(userInput)
            break

        except ValueError:
            print("That's not a valid number!")
    return weight

def GetGoal():
    goal=None
    while (goal==None):
        userInput=input("Whats your goal weight? :")
        try:
            goal=float(userInput)
            break

        except ValueError:
            print("That's not a valid number!")
    return goal



def main():
    recordData=LoadData()
    currentWeight=GetWeight()
    goalWeight=GetGoal()

    NewWeightEntry(currentWeight,recordData)
    print("Added new weight...")

    daysTotal=days_between_dates(recordData)
    print("Retrieved days...")

    weightLost=weight_lost(recordData)
    print("Retrieved weight lost...")
    ratio=weight_days_ratio(weightLost,daysTotal)
    print("Calcuated ratio...")

    daysUntillGoal=calculate_goal_date(ratio,currentWeight,goalWeight)
    dateOfGoal=today+datetime.timedelta(days=daysUntillGoal)

    print("\n"
          "%s\n"
          "Start Date: %s\n"
          "Today is: %s\n"
          "You have lost: %slbs\n"
          "That's %slbs a day!\n\n"
          "To reach your goal weight of %s,\n"
          "It should take %s days (%s)\n"
          "%s" %(commandLineArt, recordData[0][0].isoformat(),today,weightLost,ratio,goalWeight,daysUntillGoal,dateOfGoal,commandLineArt))




main()