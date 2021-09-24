from datetime import datetime

LOG_FILENAME = "Log.txt"

def WriteToLogFile(eventLog):
    eventLog.CreatedOn = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

    try:
        with open(LOG_FILENAME, "a") as f:
            f.write(str(eventLog) + '\n')
    except IOError as err:
        print("Could not print to Log.txt:\t" + err.strerror + "  |  " + str(eventLog))