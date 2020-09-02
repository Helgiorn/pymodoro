#!/usr/bin/env python3
from win10toast import ToastNotifier
import time
import datetime as dt
import webbrowser

# Collect time information
time_now = dt.datetime.now()                                       
time_pomodoro = 25*60   #Duration of working time
delta_sec = 5*60        #Duration of break                                                        
time_delta = dt.timedelta(0,time_pomodoro)                        
time_future = time_now + time_delta                                                                                                
time_finish = time_now + dt.timedelta(0,time_pomodoro+delta_sec)
total_pomodoros = 0

toaster = ToastNotifier()
start_message = "Pomodoro Started @ " + time_now.strftime("%H:%M") + "\nTimer set for 25 mins."
break_message = "Time for a Break!\n" + "It is now "+time_now.strftime("%H:%M") + " hrs. \nTimer set for 5 mins."

def pomodoro_toaster(message):
    toaster.show_toast("Pymodoro", message, icon_path="./tomato_icon.ico")

def start_pomodoro():
    time_now = dt.datetime.now()
    time_future = time_now + dt.timedelta(0,time_pomodoro)
    time_finish = time_now + dt.timedelta(0,time_pomodoro+delta_sec)
    pomodoro_toaster(start_message)
    print("Pomodoro Initiated at: "+ time_now.strftime("%H:%M"))
    print("Pomodoro will finish at : "+ time_future.strftime("%H:%M"))
    print("Pomodoro break will finish at : "+ time_finish.strftime("%H:%M"))
    #Optional, open noisli
    #webbrowser.open('https://www.noisli.com/s/96927ffffb')

start_pomodoro()
# Main script
while True:
    if time_now < time_future:
        time_left = time_future - time_now
        print (time_left)

    elif time_future <= time_now <= time_finish:
        print('Break time!')
        pomodoro_toaster(break_message)
        #The code can take a break as well
        time.sleep(20)
    else:
        pomodoro_toaster("Break Finished.\nGo to shell to start a new Pomodoro!")
        usr_ans = input("Timer has finished. \nWould you like to start another pomodoro? \nY/N:  ")
        total_pomodoros += 1
        if usr_ans == "Y":
            start_pomodoro()
            continue
        elif usr_ans == "N":
            print("Thank you!")
            break
    time.sleep(20)
    time_now = dt.datetime.now()
    timenow = time_now.strftime("%H:%M")