DROP TABLE EventLog
DROP TABLE Answers
DROP TABLE Questions
DROP TABLE Users
DROP TABLE KeyValues
CREATE TABLE KeyValues (
  ID int NOT NULL identity,
  ShortName char(8) NOT NULL unique,
  LongName nvarchar(50) NOT NULL unique,
  Description varchar(255) NULL,
  PRIMARY KEY (ID)
) 
GO

insert  into KeyValues(ShortName,LongName, Description) values 
('ConnFail','System Connection Failure','User failed to connect to the database'),
('ConnSucc','System Connection Success','User successfully connected to the database');
GO

CREATE TABLE Questions (
  ID int NOT NULL identity,
  Chapter int NOT NULL,
  Question nvarchar(800) NOT NULL unique,
  TypeID int NOT NULL,
  PRIMARY KEY (ID),
  FOREIGN KEY (TypeID) REFERENCES KeyValues (ID)
)
GO

CREATE TABLE Users (
  ID int NOT NULL identity,
  FirstName varchar(50) NOT NULL,
  LastName varchar(50) NOT NULL,
  UserName nvarchar(225) NOT NULL unique,
  HashedPassword nvarchar(max) NOT NULL,
  Salt nvarchar(1000) NOT NULL,
  PRIMARY KEY (ID),
)
GO

insert  into users(FirstName,LastName,UserName,HashedPassword,Salt) values 
('Jon','Wilson','jon.wilson@aerialelectric.com','awred2132','qwewasedwee'),
('Ritcher','Saint-Preux','ritcher.saintpreux@aerialelectric.com','2112312','2134errwe');
GO

CREATE TABLE Answers (
  ID int NOT NULL identity,
  QuestionID int NOT NULL,
  Answer nvarchar(800) NOT NULL UNIQUE,
  Correct bit NOT NULL,
  PRIMARY KEY (ID),
  FOREIGN KEY (QuestionID) REFERENCES Questions (ID)
)
GO

CREATE TABLE Eventlog (
  ID int NOT NULL identity,
  TypeID int NOT NULL,
  Description nvarchar(max) NOT NULL,
  UserID int NOT NULL,
  CreatedOn datetime NOT NULL,
  PRIMARY KEY (ID),
  FOREIGN KEY (TypeID) REFERENCES KeyValues (ID),
  FOREIGN KEY (UserID) REFERENCES Users (ID)
)