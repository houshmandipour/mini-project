import datetime, time, playsound


hour = input("Enter hour : ")
min = input("Enter min : ")
sec = input("Enter sec : ")
set_alarm_timer = f"{hour} : {min} : {sec} "
while True:
    time.sleep(1)
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    split_alarm_time = set_alarm_timer.split(":")
    split_now_time = now.split(":")
    if int(split_now_time[0]) == int(split_alarm_time[0]):
        if int(split_now_time[1]) == int(split_alarm_time[1]):
            if int(split_now_time[2]) == int(split_alarm_time[2]):
                print("Time to wake up")
                playsound('/alarm.mp3')  # for playing note.mp3 file
                break
