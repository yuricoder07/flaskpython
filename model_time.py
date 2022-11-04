import random

time=["Raunak Mondal: Dev Ops",
"Yuri Subramaniam: Chief Backend Developer",
"Harsha Jai: Frontend Developement",
"Tanay Patel: Scrum Master",
"Sachit Prasad: Secondary Backend Developer"]

def getTime():
    print(time)

def getRandomTime():
    print(random.choice(time))

def getSpecificTime(i):
    print(time[i])

def getFirstTime():
    print(time[0])

def getLastTime():
    print(time[time.len()-1])

def formatTime():
    for i in time:
        print(i)

