# Hospital Emergency Ward
#
# Uses a Priority Queue (Min Heap)
#
# Severity:
# 1 = Most Critical
# 10 = Least Urgent
#
# Heap Tuple:
# (severity, arrival_order, name, age)

import heapq

class EmergencyWard:

    def __init__(self):

        self.heap = []

        self.arrival_order = 0

    def admit(self, name, age, severity):

        self.arrival_order += 1

        patient = (
            severity,
            self.arrival_order,
            name,
            age
        )

        heapq.heappush(self.heap, patient)

        print(
            f"Admitted: {name} "
            f"(Severity {severity})"
        )

    def treat_next(self):

        if not self.heap:
            print("No patients waiting")
            return

        severity, order, name, age = heapq.heappop(
            self.heap
        )

        print(
            f"Treating: {name}, "
            f"Age {age} "
            f"(Severity {severity})"
        )

    def show_waiting(self):

        if not self.heap:
            print("No patients waiting")
            return

        print("\nWaiting Patients:")

        waiting_list = sorted(self.heap)

        for index, patient in enumerate(
                waiting_list, start=1):

            severity, order, name, age = patient

            print(
                f"{index}. "
                f"{name}  "
                f"Age {age}  "
                f"Severity: {severity}"
            )

def main():

    ward = EmergencyWard()

    ward.admit("Rahul", 45, severity=3)

    ward.admit("Priya", 28, severity=1)

    ward.admit("Arjun", 60, severity=7)

    ward.admit("Meena", 35, severity=1)


    ward.treat_next()
    ward.treat_next()

    ward.show_waiting()

main()