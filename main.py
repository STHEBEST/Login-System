import json 
import base64

# Sign up or login
welcome = input(""" Welcome to PyMaster's login system
Would you like to Sign up or login:
1. Sign up
2. Login
Please Enter a valid choice: """)




if welcome == "Sign up":

    account_info = {}
    
    with open("database.json", "r") as f:
        accounts = json.load(f)

    account_info["username"] = input("Please Enter a Username: ")
    account_info["password"] = input("Please Enter a Password: ")
    
    pwd = account_info["password"].encode("ascii")
    account_info["password"] = str(base64.b64encode(bytes(pwd)))[2:-1]
    accounts.append(account_info)

    with open("database.json", "w") as f:
        json.dump(accounts, f, indent=4)
        
    print("Account has been Successfully Added")


elif welcome == "Login":
    uname = input("Please enter your Username: ")
    pwd = input("Please Enter your Password: ")

    account_info = {}
    correct = False

    with open("database.json", "r") as f:
        users = json.load(f)

    for user in users:
        apwd = str(base64.b64decode(user["password"]))[2:-1]

        if uname == user["username"] and pwd == apwd:
            correct = True
            break

    if correct:
        print("You have successfully Logged in")
        print(f"Welcome {uname}!")
    else:

        print("Your Username or Password Is Incorrect. Please try again")
else:
    print("Please Type 'Sign up' or 'Login'")




