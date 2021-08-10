import time 
from plyer import notification

while True:
    notification.notify(
        title = "ALERT!!",
        message = "Take a breake! It has been an hour !!!",
        timeout = 15
    )
    time.sleep(3600)