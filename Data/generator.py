# Devices:
# sensorMotion0, sensorMotion1
# sensorTemp0, sensorTemp1
# sensorMagnet0, sensorMagnet1

#|ID     |Location   |
#|-------|-----------|
#|0      |Fridge     |
#|1      |Freezer    |

import sys
import json
import random

f = open("./events.json", "w")
sys.stdout = f


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

state = {"sensorMotion0" : { "status" : 0 }, 
         "sensorMotion1" : { "status" : 0 }, 
         "sensorTemp0" : { "temp" : 0, "tempDif" : 0 }, 
         "sensorTemp1" : { "temp" : 0, "tempDif" : 0 }, 
         "sensorMagnet0" : { "status" : 0 }, 
         "sensorMagnet1" : { "status" : 0 } }

def print_state(state):
    print('{',end=' ')
    for k,v in state.items():
        print(json.dumps(k),' : ',sep='', end='')
        print(json.dumps(v), end='')
        if(k!='sensorMagnet1'):
            print(', ',end='')
    if (days.index(day) == 6 and hour==23 and mins==45):
        print('}')
    else:
        print('},')
    return

def sensorMotion0(state): # Motion sensor in the Fridge | 8:00 - 17:00 on weekdays & 10:00 - 14:00 on weekends
    state["sensorMotion0"]["status"] = 0
    if days.index(day) <= 4: 
        if ((hour + mins/60) >= 8 and (hour + mins/60) < 17 ):
            state["sensorMotion0"]["status"] = int((random.randint(0, 100) > 50 ))
    else:
        if ((hour + mins/60) >= 10 and (hour + mins/60) < 14 ):
            state["sensorMotion0"]["status"] = int((random.randint(0, 100) > 70 ))

def sensorMotion1(state): # Motion sensor in the Freezer | 8:00 - 17:00 on weekdays & 10:00 - 14:00 on weekends
    state["sensorMotion1"]["status"] = 0
    if days.index(day) <= 4: 
        if ((hour + mins/60) >= 8 and (hour + mins/60) < 17 ):
            state["sensorMotion1"]["status"] = int((random.randint(0, 100) > 60 ))
    else:
        if ((hour + mins/60) >= 10 and (hour + mins/60) < 14 ):
            state["sensorMotion1"]["status"] = int((random.randint(0, 100) > 80 ))


def sensorTemp(state): # Temperature changes
    prev_temp_0 = state["sensorTemp0"]["temp"]
    prev_temp_1 = state["sensorTemp1"]["temp"]

    state["sensorTemp0"]["temp"] = int(10 - 0.75*( abs(hour - 13.5 + mins/60)))
    state["sensorTemp1"]["temp"] = int(-3 - 0.75*( abs(hour - 13.5 + mins/60)))
    state["sensorTemp0"]["tempDif"] = state["sensorTemp0"]["temp"] - prev_temp_0
    state["sensorTemp1"]["tempDif"] = state["sensorTemp1"]["temp"] - prev_temp_1
    if((days.index(day) == 0) and hour==0 and mins==0):
        state["sensorTemp0"]["tempDif"] = 0
        state["sensorTemp1"]["tempDif"] = 0


def sensorMagnet0(state): # Fridge Door | 8:00 - 17:00 on weekdays & 10:00 - 14:00 on weekends
    state["sensorMagnet0"]["status"] = 0
    if days.index(day) <= 4: 
        if ((hour + mins/60) >= 8 and (hour + mins/60) < 17 ):
            state["sensorMagnet0"]["status"] = int((random.randint(0, 100) > 50 ))
    else:
        if ((hour + mins/60) >= 10 and (hour + mins/60) < 14 ):
            state["sensorMagnet0"]["status"] = int((random.randint(0, 100) > 70 ))


def sensorMagnet1(state): # Freezer Door | 8:00 - 17:00 on weekdays & 10:00 - 14:00 on weekends
    state["sensorMagnet1"]["status"] = 0
    if days.index(day) <= 4: 
        if ((hour + mins/60) >= 8 and (hour + mins/60) < 17 ):
            state["sensorMagnet1"]["status"] = int((random.randint(0, 100) > 60 ))
    else:
        if ((hour + mins/60) >= 10 and (hour + mins/60) < 14 ):
            state["sensorMagnet1"]["status"] = int((random.randint(0, 100) > 80 ))

        
prev_state = state.copy()
print('{')
for day in days:
    for hour in range(24):
        for mins in range(0,60,15):
            if(hour<10):
                print('"2023-10-',days.index(day)+17, ' 0', hour,':', sep='', end='')
            else:
                print('"2023-10-',days.index(day)+17, ' ', hour,':', sep='', end='')
            if(mins==0):
                print('0',mins,':00":',sep='',end='')
            else:
                print(mins,':00":',sep='',end='')

            sensorMotion0(state)
            sensorMotion1(state)
            sensorTemp(state)
            sensorMagnet0(state)
            sensorMagnet1(state)
            print_state(state)
            prev_state = state.copy()
print('}')
f.close()
