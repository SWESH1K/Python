
class Patient:
    def __init__(self,name: str,age: int,gender: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.appointed_doctor = None
        self.appointments = []

    def appoint_doctor(self,doctor):
        self.appointed_doctor = doctor

    def add_appointment(self, doctor,date, time):
        self.appointments.append((doctor,date,time))

    def get_appointments(self):
        return self.appointments
    
    def get_details(self):
        return {
            "Name":self.name,
            "Age":self.age,
            "Gender":self.gender
        }
        
class Doctor:
    def __init__(self,name: str,specialization: str,charge: int):
        self.name = name
        self.specialization = specialization
        self.charge = charge

class HospitalManagement:
    def __init__(self) -> None:
        self.patients = [Patient("John",24,"male")]
        self.doctors = []
        self.all_appointments = []

    def add_patient(self,patient):
        self.patients.append(patient)

    def add_doctor(self,doctor):
        self.doctors.append(doctor)

    def add_appointment(self,patient,doctor,date,time):
        patient.add_appointment(doctor,date,time)

    def get_patient_details(self,patient):
        for key,value in patient.get_details().items():
            print(f"{key}:{value}")

    def get_appointments(self,patient):
        appointments = patient.get_appointments()
        self.get_patient_details(patient)
        i=1
        print("Appointments:")
        for doctor,date,time in appointments:
            print(f"{i}, Doctor:{doctor.name}-{doctor.specialization} --> Date:{date} --> Time:{time} --> Amount to pay: {doctor.charge}Rs")
            i+=1
        print()

def print_menu():
    print("Hospital Management System".center(40,"-"))
    options = ["Add patient","Add doctor","Add appointment", "Get patient details", "Get patient appointments","Exit"]
    for key,value in enumerate(options):
        print(f"{key+1},{value}")
    choice = input("Please enter the choice: ")
    return int(choice)

def main():

    hms = HospitalManagement()
    # while(1):
    #     choice = print_menu()
    #     if(choice==6):
    #         break
    #     match choice:
    #         case 1:
    #             name = input("Please enter the patient name: ")
    #             # for patient in hms.patients: print(patient.name)
    #             for patient in hms.patients:
    #                 if patient.name == name:
    #                     print("Patient already exists!")
    #                     continue
    #             age = int(input("Please enter the age of patient: "))
    #             gender = input("Please enter the gender of patient: ")
    #             hms.add_patient(Patient(name,age,gender))
    #             print("Patient added Successfully!")
    #         case 2:
    #             doctor_name = input("Please enter the doctor name: ")
    #             for doctor in hms.doctors:
    #                 if(doctor.name == doctor_name):
    #                     print("Doctor already exists!")
    #                     continue
    #             specialization = input("Please enter the doctor specialization: ")
    #             fees = int(input("Please enter the doctor fees: "))
    #             hms.add_doctor(Doctor(doctor_name,specialization,fees))
    #             print("Doctor added successfully!")
    #         case 3:
    #             patient = input("Please enter the patient name: ")
    #             if(patient not in hms.patients): print("Patient not found!");continue
    #             doctor = input("Please enter the doctor name: ")
    #             if(doctor not in hms.doctors): print("Doctor not found!");continue
    #             date = input("Please enter the date: ")
    #             time = input("Please enter the time: ")
    #             hms.add_appointment(patient,doctor,date,time)
    #         case 4:
    #             patient = input("Please enter the patient name: ")
    #             if(patient not in hms.patients): print("Patient not found!");continue
    #             hms.get_patient_details(patient)
    #         case 5:
    #             patient = input("Please enter the patient name: ")
    #             if(patient not in hms.patients): print("Patient not found!");continue
    #             hms.get_patient_details(patient)
    #         case _:
    #             print("Please enter the valid input!")
    
    John = Patient("John",24,"male")
    hms.add_patient(John)
    doctor1 = Doctor("Alex","Pysciartist",5_000)
    doctor2 = Doctor("Jack", "Neurosurgeon",9_000)
    hms.add_doctor(doctor1)
    hms.add_appointment(John,doctor1,"24/12/2024","10:30")
    hms.add_appointment(John,doctor2,"24/12/2024","9:00")
    hms.get_appointments(John)

if __name__ == "__main__":
    main()