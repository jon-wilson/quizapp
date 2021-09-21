import DL
from Models import *

def Display_Title():
    print("The Quiz ETL Application")
    print()    
    input("Click enter to start the ETL process...")

def main():
    Display_Title()
    DL.Connect(1)
    DL.Close()
    print("Bye!")

if __name__ == "__main__":
    main()