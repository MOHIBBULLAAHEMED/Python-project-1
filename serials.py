import os

patients = {
    "serial_no": [],
    "patient_name": [],
    "age": [],
    "gender": [],
    "contact": [],
    "reason": []
}

file_name = "serials.txt"

def load_serials_data():
    if not os.path.exists(file_name):
        return
    with open (file_name,"r",encoding="utf-8") as f:
        for line in f:
                line = line.strip()
                if line == "":
                    continue

                serial_no, name, age, gender, contact, reason = line.split(",")

                patients["serial_no"].append(int(serial_no))
                patients["patient_name"].append(name)
                patients["age"].append(age)
                patients["gender"].append(gender)
                patients["contact"].append(contact)
                patients["reason"].append(reason)

def next_serial():
    if len(patients["serial_no"]) == 0:
        return 1
    return max(patients["serial_no"]) + 1

def save_data():
    with open(file_name, "w", encoding="utf-8") as f:
        for i in range(len(patients["serial_no"])):
            f.write(
                str(patients["serial_no"][i]) + "," +
                patients["patient_name"][i] + "," +
                patients["age"][i] + "," +
                patients["gender"][i] + "," +
                patients["contact"][i] + "," +
                patients["reason"][i] + "\n"
            )

def add_serials():
    serial_no= next_serial()
    print(f"\nAuto Assigned Serial No: {serial_no}")

    name = input("Patient Name: ").lower()
    age = age_check()
    gender = gender_check()
    contact = input("Contact: ")
    reason = input("Reason: ")

    patients["serial_no"].append(serial_no)
    patients["patient_name"].append(name)
    patients["age"].append(age)
    patients["gender"].append(gender)
    patients["contact"].append(contact)
    patients["reason"].append(reason)

    save_data()
    print("✔ Patient added successfully!\n")

def age_check():
    while True:
        age = input("Age: ")
        if age.isdigit():
            return age
        else:
            print("❌ Invalid Input! Age must be a number.\n")

def gender_check():
    while True:
        print('''
Choose Gender:
1. Male
2. Female
3. Custom
''')
        g = input("Enter option (1/2/3): ")
        if g=="1":
            return "Male"
            
        elif g=="2":
            return "" \
            "Female"
        elif g=="3":
            return "Custom"
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

def show_all():
    print("\n=== All Patients ===")
    for i in range(len(patients["serial_no"])):
        print(
            patients["serial_no"][i], "-",
            patients["patient_name"][i], "-",
            patients["age"][i], "-",
            patients["gender"][i], "-",
            patients["contact"][i], "-",
            patients["reason"][i]
        )
    print()

def delet_serial():
    serial_no=input("inter your Serial Number: ")

    if serial_no.isdigit():
        serial_no = int(serial_no)
    else:
        print("❌ Invalid serial number!\n")
        return
    
    if serial_no in patients["serial_no"]:
        i=patients["serial_no"].index(serial_no)

        for j in patients:
            patients[j].pop(i)
    
        save_data()
        print("✔ Patient deleted successfully!\n")
    else:
        print("❌ Serial not found!\n")


def serials_manage():
    while True:
        print('''
1. Delete Patient
2. Show All Patients
3. Exit''')

        choice = input("Choose an option: ")
        if choice=="1":
            delet_serial()
        elif choice=="2":
            show_all()
        elif choice=="3":
            break
        else:
            print("Invalid choice! Try again.\n")
            
load_serials_data()