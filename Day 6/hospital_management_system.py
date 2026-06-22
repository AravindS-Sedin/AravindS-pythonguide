# Hospital Management System

# Real-World App: Apollo / Practo / MediBuddy

# Concepts:
# - Classes & Objects
# - Inheritance
# - Encapsulation
# - Private Attributes (__)
# - @property
# - Composition
# - Method Calls Between Objects

# Features:
# - Person is the base class
# - Doctor and Patient inherit from Person
# - All attributes are private
# - Hospital manages doctors and patients
# - Book appointments
# - Find doctors by specialization
# - Generate daily summary
# - Generate billing report

class Person:

    def __init__(self, name, age, contact):
        self.__name = name
        self.__age = age
        self.__contact = contact

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def contact(self):
        return self.__contact


class Doctor(Person):

    def __init__(self, name, age, contact,
                 specialization, fee):

        super().__init__(name, age, contact)

        self.__specialization = specialization
        self.__fee = fee

    @property
    def specialization(self):
        return self.__specialization

    @property
    def fee(self):
        return self.__fee


class Patient(Person):

    def __init__(self, name, age, contact):

        super().__init__(name, age, contact)

        self.__appointments = []

    def book_appointment(self, doctor):

        self.__appointments.append({
            "doctor": doctor.name,
            "specialization": doctor.specialization,
            "fee": doctor.fee
        })

    @property
    def appointments(self):
        return self.__appointments


class Hospital:

    def __init__(self, name):

        self.name = name
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def find_doctor(self, specialization):

        for doctor in self.doctors:

            if doctor.specialization.lower() == specialization.lower():
                return doctor

        return None

    def book_appointment(self, patient, doctor):

        patient.book_appointment(doctor)

        print(
            f"Appointment booked for "
            f"{patient.name} with Dr. {doctor.name}"
        )

    def daily_summary(self):

        print("\n----- DAILY SUMMARY -----")

        print(f"Doctors  : {len(self.doctors)}")
        print(f"Patients : {len(self.patients)}")

        total_appointments = 0

        for patient in self.patients:
            total_appointments += len(patient.appointments)

        print(f"Appointments : {total_appointments}")

    def billing_report(self, patient):

        print("\n----- BILLING REPORT -----")
        print(f"Patient : {patient.name}")

        total = 0

        for appt in patient.appointments:

            print(
                f"Dr. {appt['doctor']} "
                f"({appt['specialization']}) "
                f"- Rs.{appt['fee']}"
            )

            total += appt["fee"]

        print("--------------------------")
        print(f"Total Bill : Rs.{total}")


def main():

    hospital = Hospital("Apollo Hospital")

    d1 = Doctor(
        "Rajesh",
        45,
        "9876543210",
        "Cardiology",
        1000
    )

    d2 = Doctor(
        "Priya",
        38,
        "9876543211",
        "Dermatology",
        800
    )

    p1 = Patient(
        "Aravind",
        25,
        "9876543222"
    )

    hospital.add_doctor(d1)
    hospital.add_doctor(d2)

    hospital.add_patient(p1)

    doctor = hospital.find_doctor("Cardiology")

    if doctor:
        hospital.book_appointment(p1, doctor)

    hospital.daily_summary()

    hospital.billing_report(p1)


if __name__ == "__main__":
    main()