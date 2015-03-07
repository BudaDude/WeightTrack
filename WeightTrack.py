import datetime
from datetime import date

startWeight=370
startDate=date(2015,1,1)

goalWeight=300

commandLineArt="-"*50

#returns the differnece in days between two different dates.
def days_between_dates(date1,date2):
    return abs(date2-date1).days


#returns weight lost so far
def weight_lost(currentWeight):
    return startWeight-currentWeight

def weight_days_ratio(weight,days):
    return weight/days
def calculate_goal_date(ratio,weight,today):
    daysNeed=0
    while (weight > goalWeight):
        weight-=ratio
        daysNeed+=1
    return daysNeed

def main():
    today=date.today()
    daysTotal=days_between_dates(startDate,today)
    currentWeight=int(input("Enter Current Weight: "))
    weightLost=weight_lost(int(currentWeight))
    ratio=weight_days_ratio(weightLost,daysTotal)

    daysUntillGoal=calculate_goal_date(ratio,currentWeight,today)
    dateOfGoal=today+datetime.timedelta(days=daysUntillGoal)

    print("\n"
          "%s\n"
          "Start Date: %s\n"
          "Today is: %s\n"
          "You have lost: %slbs\n"
          "That's %slbs a day!\n\n"
          "To reach your goal weight of %s,\n"
          "It should take %s days (%s)\n"
          "%s" %(commandLineArt, startDate,today,weightLost,ratio,goalWeight,daysUntillGoal,dateOfGoal,commandLineArt))




main()