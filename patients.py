import os

prescription={
    "Serial":[],
    "name":[],
    "age":[],
    "gender":[],
    "medicine":[],
    "tests":[]
}
file_name="serials.txt"
prescription_file="prescription.txt"

def load_prescription_data():
    if not os.path.exists(file_name):
        return
    
    with open(prescription_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue

def patient_check():
    serial_num=input("Inter The Serial NO. ")

    with open (file_name,"r",encoding="utf-8") as f:
        for line in f:
                line = line.strip()
                if line == "":
                    continue

                serial_no, name, age, gender, contact, reason = line.split(",")
                
                if serial_num in serial_no:
                    print (f"Name = {name.capitalize()}\nAge = {age}\nGender = {gender.capitalize()}\nContact = {contact}\nReason = {reason.capitalize()}")

                    return (f"Name = {name.capitalize()}\nAge = {age}\nGender = {gender.capitalize()}\nContact = {contact}\nReason = {reason.capitalize()}")
        if serial_num not in serial_no:    
            print ("Something is rong in your Serial NO.")

def patient_prescription():
    serial = input("Enter patient serial: ")

    with open (file_name,"r",encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue

            serial_no, name, age, gender, contact, reason = line.split(",")
                
            if serial in serial_no:
                patient_name=name
                patient_age=age
                patient_gender=gender
                break
        
        print("Patient not found")
        