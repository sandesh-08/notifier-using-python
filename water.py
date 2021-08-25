import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="!!! DRINK WATER !!!",
            message="Water, a substance composed of the chemical elements hydrogen and oxygen and existing in gaseous, liquid, and solid states. It is one of the most plentiful and essential of compounds",
            timeout=5
        )
        time.sleep(60)

       # IN ORDER TO RUN ANY OF SUCH PROGRAMME IN BACKGRUND JUST RUN COMMAND "pythonw.exe  .\main.py" 
        #THIS COMMAND WILL WORK EVEN AFTER CLOSING THESE TERMIALS
        #AND TO STOP THESE PROGRAMMES GO TO TASK MANAGER