import os
import ast
from datetime import datetime  # 🔹 DateTime এর জন্য

prescription = {
    "Serial": [],
    "name": [],
    "age": [],
    "gender": [],
    "medicine": [],
    "tests": [],
    "datetime": []  # 🔹 DateTime field added
}

file_name = "serials.txt"
prescription_file = "prescription.txt"

# ========== 🔹 MEDICINE PANEL ==========
def medicine_input_menu():
    medicines = []

    while True:
        print('''
==== Medicine Input Panel ====
1. Add New Medicine
2. Show All Added Medicines
3. Finish & Return
''')
        choice = input("Choose an option: ")

        if choice == "1":
            med_name = input("Enter medicine name: ")
            dose = input("Dose (e.g. 3/day): ")
            days = input("Days (e.g. 5days): ")

            med_entry = [med_name, dose, days]
            medicines.append(med_entry)
            print("✔ Medicine Added!\n")

        elif choice == "2":
            print("\n=== Added Medicines ===")
            for med in medicines:
                print(med)
            print()

        elif choice == "3":
            return medicines

        else:
            print("❌ Invalid choice! Try again.\n")

# ========== 🔹 TEST PANEL ==========
def test_input_menu():
    tests = []

    while True:
        print('''
==== Test Input Panel ====
1. Add New Test
2. Show All Tests
3. Finish & Return
''')
        choice = input("Choose an option: ")

        if choice == "1":
            test_name = input("Enter test name: ")
            tests.append(test_name)
            print("✔ Test Added!\n")

        elif choice == "2":
            print("\n=== Added Tests ===")
            for t in tests:
                print("-", t)
            print()

        elif choice == "3":
            return tests

        else:
            print("❌ Invalid choice! Try again.\n")

# ========== 🔹 SAVE PRESCRIPTION ==========
def save_prescription():
    with open(prescription_file, "a", encoding="utf-8") as f:
        for i in range(len(prescription["Serial"])):
            med_text = str(prescription["medicine"][i])
            test_text = str(prescription["tests"][i])
            datetime_text = prescription["datetime"][i]  # 🔹 include datetime

            line = (
                f"{prescription['Serial'][i]}-"
                f"{prescription['name'][i]}-"
                f"{prescription['age'][i]}-"
                f"{prescription['gender'][i]}-"
                f"{med_text}-"
                f"{test_text}-"
                f"{datetime_text}\n"
            )
            f.write(line)

# ========== 🔹 PRESCRIPTION ENTRY ==========
def patient_prescription():
    serial = input("Enter patient serial: ")
    found = False

    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue

            serial_no, name, age, gender, contact, reason = line.split(",")

            if serial == serial_no:
                found = True
                medicine = medicine_input_menu()
                tests = test_input_menu()
                now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")  # 🔹 current datetime

                # Store in dictionary
                prescription["Serial"].append(serial_no)
                prescription["name"].append(name)
                prescription["age"].append(age)
                prescription["gender"].append(gender)
                prescription["medicine"].append(medicine)
                prescription["tests"].append(tests)
                prescription["datetime"].append(now)  # 🔹 add datetime

                save_prescription()
                print("\n✔ Prescription Saved Successfully!\n")
                break

    if not found:
        print("❌ Patient not found\n")

# ========== 🔹 SHOW PRESCRIPTION ==========
def show_prescription():
    patient_name = input("Enter patient name: ").strip()

    with open(prescription_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            serial_no, name, age, gender, med_str, test_str, dt_str = line.split("-")
            medicine = ast.literal_eval(med_str)
            tests = ast.literal_eval(test_str)

            if patient_name.lower() == name.lower():
                print("===== Prescription =====")
                print(f"Serial: {serial_no}")
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Gender: {gender}")
                print(f"Date & Time: {dt_str}")  # 🔹 show datetime

                if not medicine:
                    print("\nMedicines:",end="")
                    print("None")
                else:
                    print("\nMedicines:")
                    for med in medicine:
                        print(f"- {med[0]} | Dose: {med[1]} | Days: {med[2]}")

                if not tests:
                    print("\nTests:",end="")
                    print("None")
                else:
                    print("\nTests:")
                    for t in tests:
                        print(f"- {t}")

                print("========================\n")

    if patient_name.lower() != name.lower():
        print("❌ Patient not found!")

def old_prescriptions():

    patient_name=input("Patient Name: ")
    current_serial=input("Current Name: ")

    if not os.path.exists(prescription_file):
        print("❌ No prescriptions saved yet.")
        return

    found_any = False

    with open(prescription_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            try:
                serial_no, name, age, gender, med_str, test_str, dt_str = line.split("-")
                medicine = ast.literal_eval(med_str)
                tests = ast.literal_eval(test_str)
            except Exception as e:
                print(f"⚠ Error reading line: {line}\n{e}")
                continue

            # Check if name matches AND not the current prescription
            if patient_name.lower() == name.lower() and serial_no != current_serial:
                found_any = True
                print("===== Previous Prescription =====")
                print(f"Serial: {serial_no}")
                print(f"Name: {name}")
                print(f"Age: {age}")
                print(f"Gender: {gender}")
                print(f"Date & Time: {dt_str}")

                if not medicine:
                    print("\nMedicines: None")
                else:
                    print("\nMedicines:")
                    for med in medicine:
                        print(f"- {med[0]} | Dose: {med[1]} | Days: {med[2]}")

                if not tests:
                    print("\nTests: None")
                else:
                    print("\nTests:")
                    for t in tests:
                        print(f"- {t}")

                print("===============================\n")

    if not found_any:
        print(f"❌ No previous prescriptions found for {patient_name}.")

def patient_check():
    patient_id=input("Patient ID: ")

    with open(file_name,"r",encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue

            serial_no, name, age, gender, contact, reason = line.split(",")

            if patient_id == serial_no:
                print(f"Serial NO:{serial_no}\nName:{name.capitalize()}\nAge:{age}\nGender:{gender.capitalize()}\nReason:{reason.capitalize()}")
        if patient_id != serial_no:
            print(f"❌ No previous prescriptions found for {patient_id}.")