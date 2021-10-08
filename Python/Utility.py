from datetime import datetime
from shutil import copy
import os 

LOG_FILENAME = "Log.txt"

def WriteToLogFile(eventLog):
    eventLog.CreatedOn = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

    try:
        with open(LOG_FILENAME, "a") as f:
            f.write(str(eventLog) + '\n')
        print(eventLog)
    except IOError as err:
        print("Could not print to Log.txt:\t" + err.strerror + "  |  " + eventLog)

def ValidInteger(value):
    try:
        value = int(value)
    except:
        print("Please select an integer value.")


# def ConvertWordFilesToText():
#     src = r"C:\Users\jon.wilson\source\repos\QuizApp\Source"
#     dst = r"C:\Users\jon.wilson\source\repos\QuizApp\Destination"
#     for filename in os.listdir(src):
#         src = src + "\\" + filename
#         filename = filename.replace("docx", "txt")
#         dst = dst + "\\" + filename
#         copy(src, dst)        
#         src = r"C:\Users\jon.wilson\source\repos\QuizApp\Source"
#         dst = r"C:\Users\jon.wilson\source\repos\QuizApp\Destination"