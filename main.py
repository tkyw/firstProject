from utilities import get_info, check_password, register_page, record_user

def login_page():
    logined_in = False
    while True:
        userName=input("Enter your username: ")
        getusers=get_info("users")
        if userName in getusers:
            password = getusers[userName]
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
            break
            
def dashboard():
    print("Welcome!")

def main():
    while True:
        print("1. Login\n2. Register\n3. Close")
        choice = int(input("Enter your choice -> "))
        if choice == 1:
            courses = get_info("courses") 
            login_page()
            dashboard()
        elif choice == 2:
            register_page()
        elif choice == 3:
            break
        else: 
            print("invalid choice🤬🤬")


if __name__ == "__main__":
    main()
   









































































