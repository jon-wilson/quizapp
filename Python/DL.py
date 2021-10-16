from Utility import WriteToLogFile
from Models import *
from datetime import datetime
import pyodbc 
from contextlib import closing

conn = None
credentials = 'Driver={SQL Server Native Client 11.0}; Server=RES-0203002; Database=sweg-3301; uid=sweg3301-agent;pwd=sweg3301-agent-1;'

def DbConnect(userId):
    global conn 
    if not conn:
        try:                
            conn = pyodbc.connect(credentials)
            LogEvent(EventLog(0, 2, "Successful connection established.", userId))
        except:            
            WriteToLogFile(EventLog(0, 1, "Failed to connect to the database", userId))
                
def DbClose(userId):
    if conn:
        LogEvent(EventLog(0, 5, "Closing database connection.", userId))
        conn.close()

def SaveQuestionAnswersToDB(question):
    sql = '''EXECUTE [dbo].[ins_Question] ?, ?, ?, ?'''

    # try:
    #     with closing(conn.cursor()) as c:
    #         c.execute(sql, eventLog.TypeID, eventLog.Message, eventLog.UserID, eventLog.CreatedOn)
    #         conn.commit()
    # except Exception:
    #     eventLog.Message = "CURSOR ERROR: Could not insert record to LogEvent table:\t"

    raise NotImplementedError

def LogEvent(eventLog):
    sql = '''EXECUTE [dbo].[ins_EventLog] ?, ?, ?, ?'''
    eventLog.CreatedOn = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with closing(conn.cursor()) as c:
            c.execute(sql, eventLog.TypeID, eventLog.Message, eventLog.UserID, eventLog.CreatedOn)
            conn.commit()
    except:
        eventLog.Message = "CURSOR ERROR: Could not insert record to LogEvent table:\t"
    
    WriteToLogFile(eventLog)
