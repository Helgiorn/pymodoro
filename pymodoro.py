from win10toast import ToastNotifier
import time
import datetime as dt

# Collect time information
time_now = dt.datetime.now()                                       
time_pomodoro = 1*20                                                          
time_delta = dt.timedelta(0,time_pomodoro)                        
time_future = time_now + time_delta                                     
delta_sec = 1*20                                                           
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

start_pomodoro()
# Main script
while True:
    if time_now < time_future:
        print('Still in pomomode')
    elif time_future <= time_now <= time_finish:
        print('Break time!')
        pomodoro_toaster(break_message)
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