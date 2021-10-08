import os
from pyodbc import lowercase
import DL
from Models import EventLog
from Utility import ValidInteger

def Display_Menu():
    while(True):
        
        print("*"*30)
        print("The Quiz ETL Application")
        print("-"*30)    
        print()
        print("1.\tLoad quiz into database")
        print("q.\tQuit the program")    
        print()
        print("-"*30)    
        print()        
        userChoice = input("Please choose a menu item:  ")

        if(userChoice.lower() == 'q' or ValidInteger(userChoice)):
            return userChoice

        #Clear terminal
        os.system('cls||clear')
    
def ExecuteUserChoice(userChoice, userId):
    if userChoice.lower() == 'q':
        print("Goodbye!")
        return False
    elif userChoice.lower() == 1:
        LoadQuiz(userId)
    else:
        DL.LogEvent(EventLog(0, 6, "Unknown user choice", userId))
        return False
    
    return True

def LoadQuiz(userId):
    return True