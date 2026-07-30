"""
CGPA Planner
------------
File: cgpa_planner.py

Features
--------
✔ Add Semester
✔ Semester Credits
✔ Semester GPA
✔ Calculate Current CGPA
✔ Predict Future CGPA
✔ Required GPA Calculation
✔ Academic Summary
✔ Display Semester Records
"""


class CGPAPlanner:

    def __init__(self):

        self.semesters = []

    # ----------------------------------
    # Add Semester
    # ----------------------------------
    def add_semester(self,
                     semester,
                     credits,
                     gpa):

        record = {

            "Semester": semester,
            "Credits": credits,
            "GPA": gpa,
            "Quality Points":
                credits * gpa

        }

        self.semesters.append(record)

        return record

    # ----------------------------------
    # Current CGPA
    # ----------------------------------
    def current_cgpa(self):

        if not self.semesters:
            return 0

        total_quality = sum(

            item["Quality Points"]

            for item in self.semesters

        )

        total_credits = sum(

            item["Credits"]

            for item in self.semesters

        )

        return round(
            total_quality / total_credits,
            2
        )

    # ----------------------------------
    # Predict Future CGPA
    # ----------------------------------
    def predict_cgpa(self,
                     future_credits,
                     expected_gpa):

        total_quality = sum(

            item["Quality Points"]

            for item in self.semesters

        )

        total_credits = sum(

            item["Credits"]

            for item in self.semesters

        )

        total_quality += (
            future_credits *
            expected_gpa
        )

        total_credits += future_credits

        return round(
            total_quality /
            total_credits,
            2
        )

    # ----------------------------------
    # Required GPA
    # ----------------------------------
    def required_gpa(self,
                     target_cgpa,
                     future_credits):

        total_quality = sum(

            item["Quality Points"]

            for item in self.semesters

        )

        total_credits = sum(

            item["Credits"]

            for item in self.semesters

        )

        if future_credits == 0:
            return 0

        required = (

            (
                target_cgpa *
                (total_credits + future_credits)
            )

            - total_quality

        ) / future_credits

        return round(
            required,
            2
        )

    # ----------------------------------
    # Summary
    # ----------------------------------
    def summary(self):

        total_credits = sum(

            item["Credits"]

            for item in self.semesters

        )

        return {

            "Semesters":
                len(self.semesters),

            "Credits":
                total_credits,

            "Current CGPA":
                self.current_cgpa()

        }

    # ----------------------------------
    # Display Semester
    # ----------------------------------
    def display_record(self,
                       record):

        print("\n========== SEMESTER ==========\n")

        for key, value in record.items():

            print(f"{key:<18}: {value}")

    # ----------------------------------
    # Display All Semesters
    # ----------------------------------
    def display_records(self):

        if not self.semesters:

            print("\nNo semester records.")

            return

        print("\n========== SEMESTERS ==========\n")

        for index, record in enumerate(

                self.semesters,
                start=1):

            print(f"Semester {index}")

            print("-" * 35)

            for key, value in record.items():

                print(f"{key:<18}: {value}")

            print()

    # ----------------------------------
    # Display Summary
    # ----------------------------------
    def display_summary(self):

        report = self.summary()

        print("\n========== SUMMARY ==========\n")

        for key, value in report.items():

            print(f"{key:<20}: {value}")


# ----------------------------------
# Example
# ----------------------------------

if __name__ == "__main__":

    planner = CGPAPlanner()

    while True:

        print("\n1. Add Semester")
        print("2. View Semesters")
        print("3. Current CGPA")
        print("4. Predict Future CGPA")
        print("5. Required GPA")
        print("6. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            semester = input(
                "Semester Name: "
            )

            credits = float(
                input(
                    "Credits: "
                )
            )

            gpa = float(
                input(
                    "Semester GPA: "
                )
            )

            record = planner.add_semester(
                semester,
                credits,
                gpa
            )

            planner.display_record(
                record
            )

        elif choice == "2":

            planner.display_records()

        elif choice == "3":

            planner.display_summary()

        elif choice == "4":

            future_credits = float(
                input(
                    "Future Credits: "
                )
            )

            expected_gpa = float(
                input(
                    "Expected GPA: "
                )
            )

            prediction = planner.predict_cgpa(
                future_credits,
                expected_gpa
            )

            print(
                f"\nPredicted CGPA : {prediction}"
            )

        elif choice == "5":

            target = float(
                input(
                    "Target CGPA: "
                )
            )

            future = float(
                input(
                    "Future Credits: "
                )
            )

            required = planner.required_gpa(
                target,
                future
            )

            print(
                f"\nRequired GPA : {required}"
            )

        elif choice == "6":

            print(
                "\nThank you for using CGPA Planner."
            )

            break

        else:

            print("\nInvalid choice.")