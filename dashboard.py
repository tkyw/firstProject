from datetime import datetime
import json 
from utilities import get_current_student_info

def dashboard_choice(userName:str)-> None:
    print(f"Welcome Back! {userName}")
    while True:
        print("What section do you want to continue?")
        print("Option 1: Student Info (enter 1)\nOption 2: Course Taken (enter 2)\nOption 3: Check Result (enter 3)\nOption 4: Logout (enter 4)")
        option=int(input())
        if option==1:
            studentInfo(userName)
        elif option==2:
            courseTaken()
        elif option==3:
            checkResult()
        elif option==4:
            print("\nWish you have a nice day. Bye!🙌🙌\n")
            break
   
def studentInfo(userName: str) -> None:
    print()
    print(f"""{datetime.strftime(datetime.now(), "%Y, %B %d, %H:%M:%S")}""")
    currentUserDetails, index = get_current_student_info(userName)
    for key, value in currentUserDetails.items():
        print(f"{key}: {value}")
    print()

def courseTaken():
    return 1

def checkResult():
    return 1