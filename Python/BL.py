from genericpath import isfile
import os
import DL
from Models import EventLog, Question
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
    elif userChoice.lower() == '1':
        fileNames = GetQuizzes(userId)
        SaveQuizzesToDB(fileNames, userId)
    else:
        DL.LogEvent(EventLog(0, 6, "Unknown user choice", userId))
        return False
    
    return True

def GetQuizzes(userId):
    lstFiles = list()
    filePath = input("\nEnter the filepath of the directory that contains the quiz(zes) to be loaded into the database:  ")    
    try:
        DL.LogEvent(EventLog(0, 7, "Reading directory for files.", userId))
        for fileName in os.listdir(filePath): 
            splitFile = os.path.splitext(fileName)
            if splitFile[1] == ".txt":
                lstFiles.append(filePath + "\\" + fileName)
    except:
        DL.LogEvent(EventLog(0, 8, "Error reading the directory", userId))

    return lstFiles

def SaveQuizzesToDB(fileNames, userId):
    try:
        for file in fileNames:
            DL.LogEvent(EventLog(0, 9, "Reading file: {} ...".format(file), userId))
            with open(file, "r") as f:
                SaveQuestionAnswersToDB(ParseQuestionAnswers(f.readlines()))    
    except:
        DL.LogEvent(EventLog(0, 10, "Error reading a file withing the directory", userId))

def ParseQuestionAnswers(fileText):
    raise NotImplementedError
    
def SaveQuestionAnswersToDB(lstQuestions):
    raise NotImplementedError

                