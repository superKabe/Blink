from win10toast import ToastNotifier
from time import sleep
import setproctitle

notif = ToastNotifier()
setproctitle.setproctitle('Blink')

def startNotif():
    notif.show_toast(
        "Look in the distance and Blink",
        "Focus on a distant object for at least 20 seconds",
        duration = 5,
        icon_path = "eye_icon.ico",
        threaded = True,
    )

def endNotif():
        notif.show_toast(
        "Done", "Time to Refocus",
        duration = 5,
        icon_path = "eye_icon.ico",
        threaded = True,
    )

def main():
    sleep(30*60)
    startNotif()
    sleep(20)
    endNotif()
    main()

if __name__ == '__main__':
    main()
