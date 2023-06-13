from win10toast import ToastNotifier
from time import sleep
import setproctitle
import os
import sys


notif = ToastNotifier()
setproctitle.setproctitle('Blink')

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS # type: ignore
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def startNotif():
    notif.show_toast(
        "Look 20m in the distance",
        "Focus on a distant object for 20 seconds and blink 20 times",
        duration = 5,
        icon_path = resource_path('eye_icon.ico'),
        threaded = True,
    )

def endNotif():
        notif.show_toast(
        "Done", "Time to Refocus",
        duration = 5,
        icon_path = resource_path('eye_icon.ico'),
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
