from login import login, input_password
from serials import add_serials, serials_manage
from drugs import drugs_manage
from patients import patient_check,patient_prescription,show_prescription,old_prescriptions


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
    while True:
        print("""
==== Doctor Panel ====
1. Check Patient
2. Prescription Panel
3. Show Old Prescriptions
4. Exit
""")
        choice = input("Choose an option: ")

        if choice == "1":
            patient_check()

        elif choice == "2":
            while True:
                print("""
--- Prescription Panel ---
1. Add Prescription
2. Show Prescription
3. Back
""")
                sub_choice = input("Choose an option: ")

                if sub_choice == "1":
                    patient_prescription()
                elif sub_choice == "2":
                    show_prescription()
                elif sub_choice == "3":
                    break
                else:
                    print("⚠ Invalid choice! Try again.\n")

        elif choice == "3":
            old_prescriptions()

        elif choice == "4":
            print("Exiting Doctor Panel...\n")
            break

        else:
            print("⚠ Invalid choice! Try again.\n")