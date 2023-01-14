#!/usr/bin/python3

from random import shuffle

rest_queue = []
soldier_out = [[] for i in range(7)]
soldier_in = [[] for i in range(7)]

commander_rest_queue = []
commander_out = [[] for i in range(7)]
commander_in = [[] for i in range(7)]

days = ['ראשון', 'שני', 'שלישי', 'רביעי', 'חמישי', 'שישי', 'שבת']

def good_day(day_str):
    return (day_str >= '1' and day_str <= '7')

def init_queues():
    global rest_queue
    global commander_rest_queue
    
    Q1 = input('לטעון רשימה מהקובץ? (כן/לא)')
    if Q1 == 'כן':
        f = open('guarding_list.rest_queue.txt', 'r')
        string = f.read()
        f.close()
        rest_queue = eval(string)
        
        f = open('guarding_list.commander_rest_queue.txt', 'r')
        string = f.read()
        f.close()
        commander_rest_queue = eval(string)
    else:
        commander = input('הכנס מפקדים(זהו לסיום הקלט)')
        while commander != 'זהו':
            if commander == "":
                commander = input('שם ריק, נא הכנס שם אחר')
            elif commander not in commander_rest_queue:
                commander_rest_queue.append(commander)
                commander = input('')
            else:
                commander = input('השם כבר נמצא ברשימת המפקדים')
            
        soldier = input('הכנס חיילים(זהו לסיום הקלט)')
        while soldier != 'זהו':
            if soldier == "":
                soldier = input('שם ריק, נא הכנס שם אחר')
            elif soldier not in commander_rest_queue:
                if soldier not in rest_queue:
                    rest_queue.append(soldier)
                    soldier = input('')
                else:
                    soldier = input('השם כבר נמצא ברשימת החיילים')
            else:
                soldier = input('השם כבר נמצא ברשימת המפקדים')
    
    print(rest_queue)
    print(commander_rest_queue)

def add_come_and_go():
    print('הוסף יציאות (החיילים ירדו מהרשימה בשעה 14).')
    print('דוגמה ליציאה: ישראל י, 3. ישראל י יוצא ביום שלישי')
    print('כרגיל, זהו לסיום')
    line = input('')
    while line != 'זהו':
        if line == "":
            line = input('שורה ריקה, נא הכנס שורה אחרת')
            continue
        
        split_arr = line.split(', ')
        if len(split_arr) == 1:
            split_arr = line.split(',')
            if len(split_arr) == 1:
                line = input('לא מצליח לפרק את השורה, נא הכנס שוב')
                continue
        
        dday = split_arr[1]
        if not good_day(dday):
            line = input('יום לא טוב, נא הכנס שוב')
            continue
        
        soldier = split_arr[0]
        if soldier in commander_rest_queue:
            commander_out[int(dday) - 1].append(soldier)
        elif soldier in rest_queue:
            soldier_out[int(dday) - 1].append(soldier)
        else:
            line = input('שם לא טוב, נא הכנס שוב')
            continue
        
        line = input('')
    
    print('הוסף הגעות (החיילים יכנסו לרשימה בשעה 22).')
    print('דוגמה להגעה: ישראל י, מ, 4. ישראל י צטרף ביום רביעי לסד"כ מפקדים (ח עבור חפשי"ם)')
    print('כרגיל, זהו לסיום')
    line = input('')
    while line != 'זהו':
        if line == "":
            line = input('שורה ריקה, נא הכנס שורה אחרת')
            continue
        
        split_arr = line.split(', ')
        if len(split_arr) < 3:
            split_arr = line.split(',')
            if len(split_arr) < 3:
                line = input('לא מצליח לפרק את השורה, נא הכנס שוב')
                continue
        
        dday = split_arr[2]
        if not good_day(dday):
            line = input('יום לא טוב, נא הכנס שוב')
            continue
        
        role = split_arr[1]
        is_commander = False
        if role == 'מ':
            is_commander = True
        elif role != 'ח':
            line = input('תפקיד לא טוב (ח או מ), נא הכנס שוב')
            continue
        
        if is_commander:
            commander_in[int(dday) - 1].append(split_arr[0])
        else:
            soldier_in[int(dday) - 1].append(split_arr[0])
        
        line = input('')

def save_queues(final_day):
    finish_shin_gimel()
    finish_siyoor()
    finish_machsom()
    print(f'ראשון בתור (ש"ג 2-6) הוא {rest_queue[0]}')
    f = open(f'guarding_list.rest_queue.{final_day}.txt', 'w')
    f.write(str(rest_queue))
    f.close()
    
    f = open(f'guarding_list.commander_rest_queue.{final_day}.txt', 'w')
    f.write(str(commander_rest_queue))
    f.close()

#--------------------ש"ג------------------------
new_shin_gimel_hours = [2, 6, 10, 14, 18, 22]
shin_gimel_guard = None
def finish_shin_gimel():
    global shin_gimel_guard
    if shin_gimel_guard is not None:
        rest_queue.append(shin_gimel_guard)

def how_many_in_shin_gimel(day, hour):
    if hour in new_shin_gimel_hours:
        return 1
    else:
        return 0

def new_shin_gimel(day, hour):
    global shin_gimel_guard
    shin_gimel_guard = shuffle_array.pop(0)
    
    print(f'ש"ג: יום {days[day]} שעה {hour}: {shin_gimel_guard}.')
    #print(f'shin_gimel: day {days[day]} hour {hour}: {shin_gimel_guard}.')

#--------------------סיור------------------------
new_siyoor_hours = [6, 14, 22]
siyoor_guards = []
def finish_siyoor():
    global siyoor_guards
    if siyoor_guards != []:
        commander_rest_queue.append(siyoor_guards.pop(0))
        while siyoor_guards != []:
            rest_queue.append(siyoor_guards.pop(0))

def how_many_in_siyoor(day, hour):
    if hour in new_siyoor_hours:
        return 2
    else:
        return 0

def new_siyoor(day, hour):
    global siyoor_guards
    siyoor_guards.append(commander_rest_queue.pop(0))
    for _ in range(2):  
        siyoor_guards.append(shuffle_array.pop(0))
        
    print(f'סיור: יום {days[day]} שעה {hour}: {siyoor_guards}.')
    #print(f'siyoor: day {days[day]} hour {hour}: {siyoor_guards}.')

#--------------------מחסום------------------------
new_machsom_hours = [6, 14, 22]
machsom_guards = []
def finish_machsom():
    global machsom_guards
    if machsom_guards != []:
        commander_rest_queue.append(machsom_guards.pop(0))
        while machsom_guards != []:
            rest_queue.append(machsom_guards.pop(0))

def how_many_in_machsom(day, hour):
    if hour not in new_machsom_hours:
        return 0
    elif day == 7 and hour == 14:
        return 4
    elif hour != 22 and day != 7:
        return 3
    else:
        return 2

def new_machsom(day, hour):
    global machsom_guards
    machsom_guards.append(commander_rest_queue.pop(0))
    for _ in range(how_many_in_machsom(day, hour)):
        machsom_guards.append(shuffle_array.pop(0))
    
    print(f'מחסום: יום {days[day]} שעה {hour}: {machsom_guards}.')
    #print(f'machsom: day {days[day]} hour {hour}: {machsom_guards}.')

#--------------------יזומה------------------------
yezooma_hours = [[] for i in range(7)]
yezooma_guards = []
def add_yezooma():
    global yezooma_hours
    print('הוסף יזומות צפויות לרשימה')
    print('דוגמה ליזומה: 1, 18. יזומה ביום ראשון, מתחילה בשעה 18.')
    print('מניחים כרגע סד"כ של 1+3 ועד 4 שעות. אתה יודע כבר איך מסיימים')
    line = input('')
    while line != 'זהו':
        if line == "":
            line = input('שורה ריקה, נא הכנס שורה אחרת')
            continue
        
        split_arr = line.split(', ')
        if len(split_arr) == 1:
            split_arr = line.split(',')
            if len(split_arr) == 1:
                line = input('לא מצליח לפרק את השורה, נא הכנס שוב')
                continue
        
        dday = split_arr[0]
        if not good_day(dday):
            line = input('יום לא טוב, נא הכנס שוב')
            continue
        
        dhour = split_arr[1]
        try:
            hour = int(dhour)
        except ValueError:
            line = input('שעה לא טובה, נא הכנס שוב')
            continue
        
        if hour >= 24:
            line = input('שעה לא טובה, נא הכנס שוב')
            continue
        
        yezooma_hours[int(dday) - 1].append(hour)
        
        line = input('')

def finish_yezooma(day, hour):
    global yezooma_guards
    if yezooma_guards != []:
        commander_rest_queue.append(yezooma_guards.pop(0))
        while yezooma_guards != []:
            rest_queue.append(yezooma_guards.pop(0))
        
        yezooma_hours[day].remove(hour)

def how_many_in_yezooma(day, hour):
    if hour in yezooma_hours[day]:
        return 3
    else:
        return 0

def new_yezooma(day, hour):
    global yezooma_guards
    global yezooma_hours
    yezooma_guards.append(commander_rest_queue.pop(0))
    for _ in range(3):
        yezooma_guards.append(shuffle_array.pop(0))
    print(f'יזומה: יום {days[day]} שעה {hour}: {yezooma_guards}.')
    #print(f'yezooma: day {days[day]} hour {hour}: {yezooma_guards}.')
    
    actual_day = day
    yezooma_hours[actual_day].remove(hour)
    finish_hour = hour + 4
    if finish_hour >= 24:
        finish_hour -= 24
        actual_day += 1
        if actual_day >= 7:
            actual_day -= 7
    
    yezooma_hours[actual_day].append(finish_hour)

#--------------------------
shuffle_array = []
def create_list(start_day, days_to_run):
    global shuffle_array
    day_index = start_day - 1
    
    for day in range(days_to_run):
        actual_day = (day + day_index) % 7
        for hour in range(24):
            #משחרר ש"ג סיור ומחסום לפי סדר הבאסה
            if hour in new_shin_gimel_hours:
                finish_shin_gimel()
            if hour in new_siyoor_hours:
                finish_siyoor()
            if hour in yezooma_hours[actual_day]:
                finish_yezooma(actual_day, hour)
            if hour in new_machsom_hours:
                finish_machsom()
            
            if hour == 14:
                for commander in commander_out[actual_day]:
                    commander_rest_queue.remove(commander)
                for soldier in soldier_out[actual_day]:
                    rest_queue.remove(soldier)
            if hour == 22:
                for commander in commander_in[actual_day]:
                    commander_rest_queue.insert(0, commander)
                for soldier in soldier_in[actual_day]:
                    rest_queue.insert(0, soldier)
            
            #מושך חיילים מרשימת ההמתנה ומערבב כדי לגוון במשימות
            needed_soldiers = how_many_in_yezooma(actual_day, hour) + how_many_in_machsom(actual_day, hour) + how_many_in_siyoor(actual_day, hour) + how_many_in_shin_gimel(actual_day, hour)
            for _ in range(needed_soldiers):
                shuffle_array.append(rest_queue.pop(0))
            shuffle(shuffle_array)
            
            #מקצה מחסום סיור וש"ג בשביל קצת ערבוב
            if hour in new_machsom_hours:
                new_machsom(actual_day, hour)
            if hour in yezooma_hours[actual_day]:
                new_yezooma(actual_day, hour)
            if hour in new_siyoor_hours:
                new_siyoor(actual_day, hour)
            if hour in new_shin_gimel_hours:
                new_shin_gimel(actual_day, hour)
            
            if len(shuffle_array) != 0:
                print(f'len(shuffle_array) = {len(shuffle_array)}')

if __name__ == '__main__':
    init_queues()
    
    curr_day_str = input('מאיזה יום מתחילים? [1-7]')
    while not good_day(curr_day_str):
        curr_day_str = input('יום לא טוב, תנסה שוב')
    curr_day = int(curr_day_str)
    
    length_str = input('לכמה ימים הרשימה? [1...]')
    while not (length_str >= '1' and length_str <= '99'):
        length_str = input('לא טוב, תנסה שוב')
    length = int(length_str)
    
    add_come_and_go()
    add_yezooma()
    create_list(curr_day, length)
    save_queues((curr_day + length - 1) % 7)