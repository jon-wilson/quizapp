class Answer:
    def __init__(self, ID=0, QuestionID=0, Answer="", Correct=0, TypeID=0):
        self.ID = ID
        self.QuestionID = QuestionID
        self.Answer = Answer
        self.Correct = Correct
        self.TypeID = TypeID


class EventLog:
    def __init__(self, ID=0, TypeID=0, Description="", UserID=0, CreatedOn=""):
        self.ID	= ID
        self.TypeID	= TypeID
        self.Description = Description
        self.UserID	= UserID
        self.CreatedOn = CreatedOn

    def __str__(self):
        return "ID: {}, TypeID: {}, Description: {}, UserID: {}, CreatedOn: {}".format(self.ID, self.TypeID, self.Description, self.UserID, self.CreatedOn)

class Lookup:
    def __init__(self, ID=0, ShortName="", LongName = "", Description = "", Answers = None):
        self.ID = ID
        self.ShortName = ShortName
        self.LongName = LongName
        self.Description = Description
        self.Answers = Answers

class Question:
    def __init__(self, ID=0, Chapter=0, Question="", TypeID=0):
        self.ID	= ID        
        self.Chapter = Chapter
        self.Question = Question
        self.TypeID	= TypeID

class User:
    def __init__(self, ID=0, FirstName ="", LastName = "", HashedPassword = "", Salt = ""):
        self.ID = ID
        self.FirstName = FirstName
        self.LastName = LastName
        self.HashedPassword = HashedPassword
        self.Salt = Salt   