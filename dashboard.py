from datetime import datetime
from utilities import student_id_creator
import json 

def dashboard_choice(userName):
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
   
def studentInfo(userName):
    print()
    print(f"""{datetime.strftime(datetime.now(), "%Y, %B %d, %H:%M:%S")}""")
    with open(f"user_details.json","r") as rf:
        student_info=rf.read()
        pyStudents=json.loads(student_info)
        currentStudent = ""
        for student in pyStudents:
            if student['Student Name'] == userName:
                currentStudent = student
    
        for key, value in currentStudent.items():
            print(f"{key}: {value}")
        print()

def courseTaken():
    return 1

def checkResult():
    return 1