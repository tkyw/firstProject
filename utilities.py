from os.path import exists
import json
from datetime import datetime

def get_info(filename: str) -> dict:  # users
    with open(f"{filename}.txt", "r") as rf:
        items = [line.strip() for line in rf.readlines() if line.strip() != "" and line.strip() != "."]
        infos = {}
        for item in items:
            splittedItem = item.split(",") # [key, value]
            key = splittedItem[0]
            value = splittedItem[1].strip()
            # infos[key] = int(value) if filename == 'courses' else value
            if filename == "courses":
                infos[key] = int(value)
            elif filename == "users":
                infos[key] = value
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

def record_user(newName, newPassword):
    with open("users.txt", "a") as wf:
        wf.write(f"{newName}, {newPassword}\n") 

def record_user_details(newName, newPassword, age, email):
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

def check_user_existence(userName, getUsers):
    return userName in getUsers

def student_id_creator(userName):
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
            id_ = (("0" * (num_zeros -1)) + str(num_student + 1))[-3:]
            student_id = f"Fin{year}{month}{id_}"
            return student_id