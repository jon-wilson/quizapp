from genericpath import isfile
import os
import DL
from Models import Answer, EventLog, Question
import Utility

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

        if(userChoice.lower() == 'q' or Utility.ValidInteger(userChoice, True)):
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
    chapter = 1
    try:
        for file in fileNames:
            DL.LogEvent(EventLog(0, 9, "Reading file: {}".format(file), userId))
            with open(file, "r") as f:
                SaveQuestionAnswersToDB(ParseQuestionAnswers(chapter, f.readlines()), userId)    
            chapter += 1
    except:
        DL.LogEvent(EventLog(0, 10, "Error reading a file withing the directory", userId))
        return False

def ParseQuestionAnswers(chapter, textFile):
    lstQuestions = list()  
    questionType = "13"
    question = Question(0, chapter, "", questionType, list())

    for line in textFile:
        if DetectNewSection(line.strip()):
            questionType = GetNewSection(line.strip())
            question.TypeID = questionType
        elif DetectQuestion(line):   
            question.Question = GetText(line)
        elif questionType == "13" and DetectAnswerOption(line):
            question.lstAnswers.append(GetAnswerOption(line))
        elif DetectAnswer(line):            
            if questionType == "13":
                question.lstAnswers[GetAnswerLine(line, questionType)].Correct = 1
            else:
                question.lstAnswers.append(Answer(0, 0, GetAnswerLine(line, questionType), 1))
            lstQuestions.append(question)    
            question = Question(0, chapter, "", questionType, list())

    return lstQuestions  

def DetectNewSection(text):
    return text in ["Multiple Choices", "True/False", "Short Answer"]

def GetNewSection(text):
    if text == "Multiple Choices":
        return "13"
    elif text == "True/False":
        return "14"
    elif text == "Short Answer":
        return "15"
        
def DetectQuestion(text):
    splitText = text.split(".")
    return Utility.ValidInteger(splitText[0], False)

def GetText(text):    
    text = text.replace("\n", "")
    splitText = text.split(".")
    return splitText[1].strip()

def DetectAnswerOption(text):    
    splitText = text.split(".")
    return len(splitText[0]) == 1 and splitText[0].isalpha()

def GetAnswerOption(text):    
    splitText = text.split(".")
    return Answer(0, 0, splitText[1].strip(), 0)

def DetectAnswer(text):
    splitText = text.split(":")
    return splitText[0] == "Ans"

def GetAnswerLine(text, questionType):     
    answerKey = {"a": 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4}
    text = text.replace("\n", "")
    splitText = text.split(":")

    if questionType == "13":
        return answerKey[splitText[1].strip()]
    else:
        return splitText[1].strip()

def SaveQuestionAnswersToDB(lstQuestions, userId):
    for question in lstQuestions:
        DL.SaveQuestionAnswersToDB(question, userId)
  

                