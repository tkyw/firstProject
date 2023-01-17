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

def register_page():
    print("What is your name?")
    newName=input()
    while True:
        print("What is your password?")
        newPassword=input()
        print("Please enter again to confirm your password.")
        confirmPassword=input()   
        if newPassword==confirmPassword:
            print("Successfully registered")
            record_user(newName, newPassword)
            break
        else:
            print("Please enter your password correctly")

def record_user(newName, newPassword):
    with open("users.txt", "a") as wf:
        wf.write(f"{newName}, {newPassword}\n") 