import BL
import DL

userId = 1
looping = True
DL.DbConnect(userId)
while looping:
    looping = BL.ExecuteUserChoice(BL.Display_Menu(), userId)
DL.DbClose(userId)