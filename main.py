from utilities import get_info, check_password, record_user,record_user_details,check_user_existence,student_id_creator
from dashboard import dashboard_choice

def register_page():
    correctName = False
    while True:
        getUsers=get_info("users")
        if not correctName:
            print("What is your name?")
            newName=input() 
            correctName = True
        print("What is your password?")
        newPassword=input()
        print("Please enter again to confirm your password.")
        confirmPassword=input()   
        if newPassword==confirmPassword:
            if not check_user_existence(newName, getUsers):
                print("Enter your age:")
                age=int(input())
                print("Enter your email: ")
                email=input()
                record_user(newName, newPassword)
                record_user_details(newName, newPassword, age, email)
                print("\n Successfully registered\n")
                print("This is your student id:\n"+ student_id_creator(newName))
                break
            else:
                print("User Name exists!! Enter a new name...")
                correctName = False
                continue
        else:
            print("Please enter your password correctly")

def login_page():
    logined_in = False
    while True:
        userName=input("Enter your username: ")
        getUsers=get_info("users")
        if check_user_existence(userName, getUsers):
            password = getUsers[userName]
            chances = 3
            logined_in = bool(check_password(password, chances))
        else:
            print("You are not the member yet.Do you want to register? If yes, then type 1, else type 2")
            register=int(input())
            if register==1:
                register_page()
            elif register==2:
                pass
        if logined_in:
            return userName


def main():
    while True:
        print("1. Login\n2. Register\n3. Close")
        choice = int(input("Enter your choice -> "))
        if choice == 1:
            courses = get_info("courses") 
            userName = login_page()
            dashboard_choice(userName)
        elif choice == 2:
            register_page()
        elif choice == 3:
            break
        else: 
            print("invalid choice🤬🤬")


if __name__ == "__main__":
    main()






































































