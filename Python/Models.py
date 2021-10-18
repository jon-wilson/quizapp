class Answer:
    def __init__(self, ID=0, QuestionID=0, Answer="", Correct=False):
        self.ID = ID
        self.QuestionID = QuestionID
        self.Answer = Answer
        self.Correct = Correct

class EventLog:
    def __init__(self, ID=0, TypeID=0, Message ="", UserID=0, CreatedOn=""):
        self.ID	= ID
        self.TypeID	= TypeID
        self.Message = Message
        self.UserID	= UserID
        self.CreatedOn = CreatedOn

    def __str__(self):
        return "TypeID: {}, Message: {}, UserID: {}, CreatedOn: {}".format(self.TypeID, self.Message, self.UserID, self.CreatedOn)

class Lookup:
    def __init__(self, ID=0, ShortName="", LongName = "", Note = "", Answers = None):
        self.ID = ID
        self.ShortName = ShortName
        self.LongName = LongName
        self.Note = Note
        self.Answers = Answers

class Question:
    def __init__(self, ID=0, Chapter=0, Question="", TypeID="", lstAnswers = []):
        self.ID	= ID        
        self.Chapter = Chapter
        self.Question = Question
        self.TypeID	= TypeID
        self.lstAnswers = lstAnswers

    def __str__(self):
        return "Chapter: {}, Question: {}, TypeID: {}".format(self.Chapter, self.Question, self.TypeID)
        
class User:
    def __init__(self, ID=0, FirstName ="", LastName = "", HashedPassword = "", Salt = ""):
        self.ID = ID
        self.FirstName = FirstName
        self.LastName = LastName
        self.HashedPassword = HashedPassword
        self.Salt = Salt   
