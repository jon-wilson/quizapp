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

def SaveQuestionAnswersToDB(question, userId):
    questionSql = '''SET NOCOUNT ON; 
                    DECLARE @ID int; 
                    EXEC [dbo].[ins_Question] ?,?,?, @ID OUTPUT; 
                    SELECT @ID;'''

    answerSql = '''EXECUTE [dbo].[ins_Answer] ?, ?, ?'''

    try:
        with closing(conn.cursor()) as c:
            c.execute(questionSql, question.Chapter, question.Question, int(question.TypeID))
            row = c.fetchone()
            question.ID = row[0]
            conn.commit()

        with closing(conn.cursor()) as c:
            for answer in question.lstAnswers:
                c.execute(answerSql, question.ID, answer.Answer, answer.Correct)                
                conn.commit()
    except Exception:        
        WriteToLogFile(EventLog(0, 12, "Failed to persist question and answer(s): {} to the database".format(question), userId))

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
