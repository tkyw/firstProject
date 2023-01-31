from os.path import exists
import json
from datetime import datetime

user_filename = "user_details.json"

def split_comma(items: list, filename: str) -> dict:
    infos = {} 
    # print(items)
    for item in items:
        # print(item)
        splittedItem = item.split(",") # [key, value]
        key = splittedItem[0]
        value = splittedItem[1].strip()            
        if filename == "courses":
            infos[key] = int(value)
        elif filename == "users":
            infos[key] = value
        # print(infos)
    return infos

def get_info(filename: str):  # users
    infos = ""
    with open(f"{filename}.txt", "r") as rf:
        contents = [item.strip() for item in rf.readlines() if item.strip() != ""]
        if "." not in contents:
            print("here is user")
            print("-"* 40)
            items = [content for content in contents if content.strip() != ""]
            infos = split_comma(items, "users")
        else:
            print("here is courses")
            print("-"* 40)
            items, item = [], []
            for content in contents:
                is_dot = False
                if content == ".":
                    is_dot = True
                if not is_dot:
                    item.append(content)
                    if content == contents[-1]:
                        items.append(item)
                else:
                    items.append(item)
                    item = []
            print(items)
            print("-" * 50)
            infos = [split_comma(item, "courses") for item in items]
    return infos


    

def check_password(correctPassword: str, chances: int) -> None:
    for chance in range(chances):
        if chance == 0:
            inputPassword=input("Enter your password: ")
        else:
            inputPassword=input("Wrong Password, You have {} chance(s) more, Enter your password again: ".format(chances-chance))
        if correctPassword == inputPassword:        
            return 1
        if chance == chances-1:
            print("Wrong Password, You are not allowed to access anymore!!😡😡")
    return 0

def record_user(newName:str, newPassword:str)-> None:
    with open("users.txt", "a") as wf:
        wf.write(f"{newName}, {newPassword}\n") 

def record_json(json_writer, content):
    json_data = json_wrtier.dumps(content)
    json_writer.write(json_data)

def record_user_details(newName:str, newPassword:str, age:str, email:str)-> None:
    filename = "user_details.json"
    info = {
                "Student Name" : newName,
                "Age": age,
                "Password": newPassword,
                "Email" : email,
                "Student ID": student_id_creator(newName)
            }
    if not exists(filename):
        with open(filename, "w") as wf:
            details = []
            details.append(info)
            json_details = json.dumps(details)
            wf.write(json_details)
    else:
        with open(filename, 'r') as rf:
            str_details = rf.read()
            details = json.loads(str_details)
            details.append(info)
            with open(filename, 'w') as wf:
                json_details = json.dumps(details)
                wf.write(json_details)

def update_details(index: int, latestDetails: dict):
    users = get_all_users()
    users[index] = latestDetails
    json_details = json.dumps(users)
    with open(user_filename) as wf:
        wf.write(json_details)

def check_user_existence(userName:str, getUsers:list)-> bool:
    return userName in getUsers

def student_id_creator()-> str:
    filename = "user_details.json"
    date = datetime.now()
    year, month = str(date.year)[-2:], datetime.strftime(date, "%m")
    if not exists(filename):
        return f"{year}{month}1"
    else:
        with open(filename,"r") as rf:
            sDetails = rf.read()
            details = json.loads(sDetails)
            num_student = len(details)
            num_zeros = len(str(num_student))  # '0' * (num_zeros -1)
            id_ = (("0" * (num_zeros -1)) + str(num_student + 1))[-num_zeros:]
            student_id = f"Fin{year}{month}{id_}"
            return student_id

def append_courses(currentUser):

    filename = "courses.txt" # file name 
    all_courses = get_info(filename)
    currentUserDetails, index = get_current_student_info(currentUser)
    courses = currentUserDetails.get("courses")
    if courses is None:
        courses = {}
        courses['Y1S1'] = all_courses[0]
        currentUserDetails['courses'] = courses
        update_details(index, currentUserDetails)
    else:
        num_courses = len(courses)
        year = 1
        if num_courses < 3:
            sem = num_courses + 1
        else:
            sem = 1
        if num_courses % 3 == 0:
            year += num_courses / 3
        courses[f"Y{year}S{sem}"] = courses[num_courses]
        currentUserDetails['courses'] = courses
        update_details(index, currentUserDetails)
        

def get_current_student_info(currentUser: str) -> tuple:
    filename="user_details.json"
    current_user=""
    with open (filename,"r") as rf:
        app_course=rf.read()
        appended_course=json.loads(app_course)
        for index, course in enumeate(appended_course):
            if course["Student Name"]==currentUser:
                current_user=course
    return current_user, index

def get_all_users():
    filename="user_details.json"
    with open (filename,"r") as rf:
        str_users=rf.read()
        users=json.loads(str_users)
    return users

