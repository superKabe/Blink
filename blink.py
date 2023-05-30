from win10toast import ToastNotifier
from time import sleep
import setproctitle

notif = ToastNotifier()
setproctitle.setproctitle('Blink')

def startNotif():
    notif.show_toast(
        "Look 20m in the distance",
        "Focus on a distant object for 20 seconds and blink 20 times",
        duration = 5,
        icon_path = 'build/eye_icon.ico',
        threaded = True,
    )

def endNotif():
        notif.show_toast(
        "Done", "Time to Refocus",
        duration = 5,
        icon_path = 'build/eye_icon.ico',
        threaded = True,
    )

def main():
    startNotif()
    sleep(25)
    endNotif()
    sleep(30*60)
    main()

if __name__ == '__main__':
    main()
