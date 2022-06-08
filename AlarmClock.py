from datetime import datetime
from turtle import rt
import webbrowser
import random

f = open("RandomAlarms.txt", "rt")
alarms = []
for x in f:
    alarms.append(x)
f.close()

def validateTime(time):
    if len(time) != 11:
        return False
    else:
        try:
            if int(time[0:2]) > 12 or int(time[0:2]) < 0:
                return False
            elif int(time[3:5]) > 59 or int(time[3:5]) < 0:
                return False
            elif int(time[6:8]) > 59 or int(time[6:8]) < 0:
                return False
            else:
                return True
        except:
            return False

alarmTime = input("Please enter the time for your alarm as HH:MM:SS AM/PM: ")
while True:
    if validateTime(alarmTime):
        print("Setting alarm for ", alarmTime)
        break
    alarmTime = input("That input was invalid. Please enter the time for your alarm as HH:MM:SS AM/PM: ")

alarmHour = alarmTime[0:2]
alarmMin = alarmTime[3:5]
alarmSec = alarmTime[6:8]
alarmPeriod = alarmTime[9:].upper()

now = datetime.now()

currentHour = now.strftime("%I")
currentMin = now.strftime("%M")
currentSec = now.strftime("%S")
currentPeriod = now.strftime("%p")

while True:
    if alarmHour == currentHour:
        if alarmMin == currentMin:
            if alarmSec == currentSec:
                if alarmPeriod == currentPeriod:
                    while True:
                        url = random.randint(0, len(alarms) - 1)
                        try:
                            webbrowser.open(alarms[url], new=2)
                            break
                        except:
                            pass
                    break
    now = datetime.now()
    currentHour = now.strftime("%I")
    currentMin = now.strftime("%M")
    currentSec = now.strftime("%S")
    currentPeriod = now.strftime("%p")
