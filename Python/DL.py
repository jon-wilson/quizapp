from sqlite3.dbapi2 import DatabaseError
import sys
import sqlite3
from contextlib import closing
from Models import *
from datetime import datetime

conn = None

def Connect(userId):
    global conn 
    if not conn:
        if sys.platform == "win32":
            DB_FILE = "/sqlite/SWEG-3301.db"
            try:
                conn = sqlite3.connect(DB_FILE)                
                LogEvent(EventLog(0, 2, "Successful connection established.", userId))
                conn.row_factory = sqlite3.Row
            except IOError as err:
                print("There was an error connecting to the database!  Please contact your system administrator.")
                
def Close():
    if conn:
        conn.close()

def Initialize_Answer(row):
    return Answer(row["ID"], row["QuestionID"], row["Answer"], row["Correct"])

def Initialize_User(row):
    return User(row["ID"], row["FirstName"], row["LastName"], row["UserName"], row["HashedPassword"], row["Salt"])

def get_categories():
    query = '''SELECT categoryID, name as categoryName
               FROM Category'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    categories = []
    # for row in results:
    #     categories.append(make_category(row))
    return categories

def get_category(category_id):
    query = '''SELECT categoryID, name AS categoryName
               FROM Category WHERE categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        row = c.fetchone()

    # category = make_category(row)
    # return category

def LogEvent(eventLog):
    sql = '''INSERT INTO EventLog (TypeID, Description, UserID, CreatedOn) VALUES (?, ?, ?, ?)'''
    eventLog.CreatedOn = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

    try:
        with closing(conn.cursor()) as c:
            c.execute(sql, (eventLog.TypeID, eventLog.Description, eventLog.UserID, eventLog.CreatedOn))
            conn.commit()
            print(eventLog)    
    except IOError as err:
        print("CURSOR ERROR: Could not insert record to LogEvent table:\t" + eventLog)
