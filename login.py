import msvcrt

user_dict = []

with open("user.txt","r") as file:
    for line in file:
        new_list=[]
        line_list=line.split(",")
        for i in line_list:
            i=i.strip()
            new_list.append(i)
        user_dict.append(new_list)


def login(username, password):
    for user in user_dict:
        if user[0] == username:      
            if user[1] == password:  
                role = user[2]
                print(f"\nWelcome {username}, your role is {role}.")
                return role
            else:
                print("❌ Incorrect password!")
                return False
    
    print("❌ Username not found!")
    return False


def input_password(prompt="Password: "):
    print(prompt, end="", flush=True)
    password = ""
    
    while True:
        ch = msvcrt.getch()

        if ch in {b'\r', b'\n'}:  
            print()
            break
        
        elif ch == b'\x08':  
            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        
        else:
            password += ch.decode("utf-8")
            print("*", end="", flush=True)

    return password
