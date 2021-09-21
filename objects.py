from _typeshed import Self


class Answer:
    def __init__(self, ID=0, QuestionID=0, Answer="", Correct=0, TypeID=0):
        self.ID = ID
        self.QuestionID = QuestionID
        self.Answer = Answer
        self.Correct = Correct
        self.TypeID = TypeID

class Lookup:
    def __init__(self, ID=0, ShortName="", LongName = "", Description = "", Answers = None):
        self.ID = ID
        self.ShortName = ShortName
        self.LongName = LongName
        self.Description = Description
        self.Answers = Answers

