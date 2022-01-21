from email import message
from socket import timeout
import time
from turtle import title
from plyer import notification

while(True):
    notification.notify(
        title = "Productivity Reminder!",
        message = "Hope You Are Building Your Capacity!",
        app_icon = "icons8_notification.ico",
        timeout = 10
    )
    
    time.sleep(10)