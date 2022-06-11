import re

#Function for registration
def register():
    db=open("database.txt",'r')
    d = []
    f = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    #Email/Username Validation
    un = input("Create E-mail/Username:")
    pattern1 = "[\w._%-+]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}"
    result1 = re.findall(pattern1,un)
    if un in d:
        print("Username Already Exists!\nTry Again")
        register()
    elif result1:
        pass
    else:
        print("Invalid Email/Username\nEmail/Username should contain @ followed by . and must not start with number or special character\nTry Again!")
        register()

    #Password Validation
    pw = input("Create Password:")
    pattern2 = "^.*(?=.{5,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@?#$%^&+=]).*$"
    result2 = re.findall(pattern2,pw)
    if result2:
        db = open("database.txt","a")
        db.write(un+", "+pw+"\n")
        print("You Have Been Registered Successfully!")
        exit()
    else:
        print("Password should have minimum length 5 and maximum length 16 and must contain ONE SPECIAL CHARACTER, ONE DIGIT, ONE UPPERCASE and ONE LOWERCASE character")
        register()


#Function for login
def login():
    db = open("database.txt",'r')
    d = []
    f = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
        data = dict(zip(d, f))
        username = input("Enter your Username/Email-id: ")
        if username in d:
            password = input("Enter your Password: ")
            if password == data[username]:
                print("Login success")
                print("Hi,",username)
                exit()
            else:
                print("Password incorrect")
                forget()
        else:
            print("Username doesn't exist\nRegister First!")
            register()

#Function for forget password or creating a new one
def forget():
    db = open("database.txt", 'r')
    d = []
    f = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    n=int(input("Do you wish to retrieve your old password or set new one?\n1. Retrieve\n2. Create new one\n"))
    if n==1:
        uname=input("Enter your username: ")
        if uname in d:
            print("Hi! "+uname+"\nYour Password is "+data[uname]+"\n")
        else:
            print(uname+" doesn't exist!\nRegister First!")
            register()

    elif n==2:
        un=input("Enter your Username: ")
        if un in d:
            pw=input("Enter your new password: ")
            pattern2 = "^.*(?=.{5,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@?#$%^&+=]).*$"
            result2 = re.findall(pattern2, pw)
            if result2:
                data[un] = pw
                db = open("database.txt", "w")
                for i, j in data.items():
                    db.write(i + ", " + j + "\n")
                print("Your Password has been Changed Successfully!")
            else:
                print("Password should have minimum length 5 and maximum length 16 and must contain ONE SPECIAL CHARACTER, ONE DIGIT, ONE UPPERCASE and ONE LOWERCASE character")
                forget()
        else:
            print(un+" doesn't exist!\nRegister First!")
            register()

#Function for Home Page
def home():
    option=int(input("************HOME*****************\n1. Login\n2. Registration\n3. Exit\n*********************************\n"))
    if option==1:
        login()
    elif option==2:
        register()
    elif option==3:
        exit()
home()