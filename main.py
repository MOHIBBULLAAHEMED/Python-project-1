from login import login, input_password
from serials import add_serials, serials_manage
from drugs import drugs_manage
from patients import patient_check


while True:
    username = input("Enter Username: ")
    password = input_password("Enter Password: ")

    role = login(username, password)

    if role:
        break

print("\n✔ Logged in successfully!\n")

if role == "Manager":
    while True:
        print('''
==== Manager Panel ====
1. Taking Serial
2. Managing Serial
3. Managing Drugs & Selling Info
4. Exit
''')
        
        choice = input("Choose an option: ")

        if choice == "1":
            add_serials()

        elif choice == "2":
            serials_manage()

        elif choice == "3":
            drugs_manage()

        elif choice == "4":
            print("Exiting...\n")
            break

        else:
            print("Invalid choice! Try again.\n")
elif role == "Doctor":
    patient_check()