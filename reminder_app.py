import time
from plyer import notification      #pip install plyer

class Reminder:
    def __init__(self):
        self.title1 = input("What do you want to get notified about?")
        self.msg1 = input("Please enter the message you want to display on the screen.")
        self.set_time = float(input("Please enter the duration in minutes.")) * 60

    def notification1(self):
        while True:
            notification.notify(title = self.title1, message = self.msg1, app_icon = "icon.ico", app_name = "Notification!", timeout = 5)
            time.sleep(self.set_time)

remind = Reminder()
remind.notification1()

